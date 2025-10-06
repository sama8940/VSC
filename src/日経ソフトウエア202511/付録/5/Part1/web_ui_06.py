import streamlit as st
import sqlite3 
import datetime

# カスタムアダプター、カスタムコンバーターの作成と登録
sqlite3.register_adapter(datetime.date, lambda d: d.isoformat())
sqlite3.register_converter("DATE", lambda s: datetime.date.fromisoformat(s.decode("utf-8")))

db_name = 'booking.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

hours = [f'{h}:00' for h in range(9, 18)]
colors = ['#FFFFFF' for _ in range(len(hours))]

# その日の予約時間の取得
def get_reserved_times_for_day(room_id, date):
  cur.execute("""SELECT check_in, check_out
                 FROM Reservations
                 WHERE room_id = ? and date = ?;""",
                 (room_id, date))
  return cur.fetchall()

# 入室可能時間の抽出
def get_check_in_hours(room_id, date):
  # 全入室時間のリスト
  in_hours = [f'{h}:00' for h in range(9, 18)]
  reserved_times = get_reserved_times_for_day(room_id, date)
  in_remove = []

  # 入室時間から削除するリストの生成
  for check_in, check_out in reserved_times:
    in_out = False
    # チェックインできないコマの抽出
    for i, h in enumerate(hours):
      if not in_out and h == check_in:
        in_out = True
      if in_out and h == check_out:
        in_out = False
      if in_out:  # 予約済みの時間
       in_remove.append(i)	# 削除リストに追加
       colors[i] = '#FFCCFF'	# コマに色を付ける

  # 削除リストを使い後ろから削除
  for i in sorted(in_remove, reverse=True):
    del in_hours[i]
  return in_hours

# 退室可能時間の抽出
def get_check_out_hours(check_in):
  # 全退室時間のリスト
  out_hours = [f'{h}:00' for h in range(10, 19)]
  chek_out_time = []
  in_out = False

  # 退室時間の選択肢リスト生成
  for i, h in enumerate(hours):
    if not in_out and hours[i] == check_in:
      chek_out_time.append(out_hours[i])
      in_out = True
    elif in_out and colors[i] == '#FFFFFF':
      chek_out_time.append(out_hours[i])
    elif in_out and colors[i] == '#FFCCFF':
      break
    if in_out and i == len(out_hours):
      chek_out_time.append(out_hours[i])
      break
  return chek_out_time

# サンプル社員
employee_id = '100123'
employee_name = '田中 太郎'

# 予約画面
st.title('会議室予約システム')
st.write(f'社員番号：{employee_id}　氏名：{employee_name}')

st.write('色がついている時間帯はすでに予約済みです。')
# コマ分のカラムを作成
# 入室時間(会議室：会議室 A、予約日：2025-07-14）
chek_in_hours = get_check_in_hours('1', '2025-07-14')

cols = st.columns(len(hours), gap = 'small')
for i, col in enumerate(cols):
  with col:
    # 1コマをHTML、CSSで描画
    st.markdown(f"""<div style=
      'background-color:{colors[i]};
       border: 1px solid #333;
       padding:15px;
       border-radius:10px;
       text-align:center;'>
       <span>{hours[i]}</span><br>
       </div><br>
       """, unsafe_allow_html = True)

# 入室時間
check_in = st.selectbox('入室時間を選んでください：', chek_in_hours)

# 退室時間
chek_out_hours = get_check_out_hours(check_in)
check_out = st.selectbox('退室時間を選んでください：', chek_out_hours)

# 接続の切断
conn.close()