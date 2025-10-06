import streamlit as st
import sqlite3 
import datetime

# カスタムアダプター、カスタムコンバーターの作成と登録
sqlite3.register_adapter(datetime.date, lambda d: d.isoformat())
sqlite3.register_converter("DATE", lambda s: datetime.date.fromisoformat(s.decode("utf-8")))

db_name = 'booking.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

# 会議室データの取得
def get_rooms():
  cur.execute("""SELECT * FROM Rooms;""")
  return cur.fetchall()

# 会議室名からIDを取得
def get_room_id(room_name):
  cur.execute("""SELECT id FROM Rooms WHERE name = ?;""",(room_name,))
  return cur.fetchone()[0]

# 予約情報の追加
def add_reservation(employee_id, room_id, date, check_in, check_out, purpose):
  cur.execute("""INSERT INTO Reservations
                 (employee_id, room_id, date, check_in, check_out, purpose)
                 VALUES (?, ?, ?, ?, ?, ?);""",
                 (employee_id, room_id, date, check_in, check_out, purpose))
  conn.commit()

# サンプル社員
employee_id = '100123'
employee_name = '田中 太郎'

# 予約画面
st.title('会議室予約システム')
st.write(f'社員番号：{employee_id}　氏名：{employee_name}')

# 予約会議室の選択
rooms = get_rooms()
select_room_name = [room[1] for room in rooms]
room_name = st.selectbox('会議室を選択してください：', select_room_name)
st.write(f'選択した会議室：{room_name}')
    
# 予約する日付
date = st.date_input('予約日：')
st.write(f'選択した日付：{date}')

# コマに表示する時間
hours = [f'{h}:00' for h in range(9, 18)]

# 入室時間の選択肢
chek_in_hours = [f'{h}:00' for h in range(9, 18)]

# 退室時間の選択肢
chek_out_hours = [f'{h}:00' for h in range(10, 19)]

# コマの背景色（白）
colors = ['#FFFFFF' for _ in range(len(hours))]

st.write('色がついている時間帯はすでに予約済みです。')
# コマ分のカラムを作成
cols = st.columns(len(hours), gap = 'small')
for i, col in enumerate(cols):
  with col:

    # 1コマをHTML、CSSで描画
    # background-color：背景色を指定
    # border：1px幅、実線、濃いグレーの境界線
    # padding：内側の余白をすべての方向に15px
    # border-radius：四隅を10px分、角丸
    # text-align：テキストを中央揃え
    # <span>{hours[i]}</span>：時間表示
    # unsafe_allow_html = True：markdown関数にHTMLを記述
    st.markdown(f"""<div style=
      'background-color:{colors[i]};
       border: 1px solid #333;
       padding:15px;
       border-radius:10px;
       text-align:center;'>
       <span>{hours[i]}</span><br>
       </div><br>
       """, unsafe_allow_html = True)

# 入室時間の選択
check_in = st.selectbox('入室時間を選んでください：', chek_in_hours)
st.write(f'選択した入室時間：{check_in}')

# 退室時間の選択
check_out = st.selectbox('退室時間を選んでください：', chek_out_hours)
st.write(f'選択した退室時間：{check_out}')

# 使用目的の入力
purpose = st.text_input('使用目的を入力してください：')
st.write(f'入力した使用目的：{purpose}')

# 予約ボタン
bnt_1 = st.button('予約')
if bnt_1:
  add_reservation(employee_id,
                  get_room_id(room_name), # 会議室名からIDを取得
                  date,
                  check_in,
                  check_out,
                  purpose)
  st.write('予約しました。')

  # Reservations 追加データ確認用表示
  print('Reservations')
  for row in cur.execute("""SELECT * FROM Reservations;"""):
    print(row)

  st.rerun()

# 接続の切断
conn.close()