import streamlit as st
import sqlite3 
import datetime

# カスタムアダプター、カスタムコンバーターの作成と登録
sqlite3.register_adapter(datetime.date, lambda d: d.isoformat())
sqlite3.register_converter("DATE", lambda s: datetime.date.fromisoformat(s.decode("utf-8")))

db_name = 'booking.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

# 社員の予約情報を取得
def get_reserved_for_employee(employee_id):
  cur.execute("""SELECT id, room_id, date, check_in, check_out, purpose
                 FROM Reservations
                 WHERE employee_id = ?;""",
                 (employee_id,))
  return cur.fetchall()

# IDから会議室名を取得
def get_room_name(room_id):
  cur.execute("""SELECT name FROM Rooms WHERE id = ?;""",(room_id,))
  return cur.fetchone()[0]

# 予約情報の削除
def delete_reservation(r_id):
  cur.execute("""DELETE FROM Reservations
                 WHERE id = ?;""",
                 (r_id,))
  conn.commit()

# サンプル社員
employee_id = '100123'
employee_name = '田中 太郎'

### キャンセル画面 ###  
st.title('予約キャンセル')
st.write(f'社員番号：{employee_id}　氏名：{employee_name}')

# 田中 太郎の予約情報を取得
reserved = get_reserved_for_employee(employee_id)

if not reserved:
  st.write('会議室の予約情報はありません。')
else:
  for r_id, room_id, date, check_in, check_out, purpose in reserved:
    col1, col2 = st.columns([4, 2], gap = 'small', border = True)

    # 予約情報の表示
    with col1:
      col3, col4 = st.columns(2, gap = 'small')
      with col3: 
        st.write(f'予約ID：{r_id}　{get_room_name(room_id)}')
        st.write(f'入室時間：{check_in}')
      with col4:
        st.write(f'予約日：{date}')
        st.write(f'退出時間：{check_out}')
      st.write(f'使用目的：{purpose}')

    # キャンセルボタンの表示と予約情報の削除
    with col2:
      if st.button('キャンセル', key = f'delete_{r_id}'):
        delete_reservation(r_id)
        st.rerun()

# 接続の切断
conn.close()