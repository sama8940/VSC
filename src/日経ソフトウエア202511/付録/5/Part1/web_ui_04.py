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

# 接続の切断
conn.close()