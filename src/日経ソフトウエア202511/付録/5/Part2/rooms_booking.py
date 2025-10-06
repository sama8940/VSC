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

# IDから会議室名を取得
def get_room_name(room_id):
  cur.execute("""SELECT name FROM Rooms WHERE id = ?;""",(room_id,))
  return cur.fetchone()[0]

# 予約情報の追加
def add_reservation(employee_id, room_id, date, check_in, check_out, purpose):
  cur.execute("""INSERT INTO Reservations
                 (employee_id, room_id, date, check_in, check_out, purpose)
                 VALUES (?, ?, ?, ?, ?, ?);""",
                 (employee_id, room_id, date, check_in, check_out, purpose))
  conn.commit()

# 予約の削除
def delete_reservation(reservation_id):
  cur.execute("""DELETE FROM Reservations
                 WHERE id = ?;""",
                 (reservation_id,))
  conn.commit()

# ユーザー認証
def authenticate_user(email, password):
  cur.execute("""SELECT * 
                 FROM Employees
                 WHERE email = ? AND password = ?;""",
                 (email, password))
  return cur.fetchone()

# その日の予約済み時間の取得
def get_reserved_times_for_day(room_id, date):
  cur.execute("""SELECT check_in, check_out
                 FROM Reservations
                 WHERE room_id = ? and date = ?;""",
                 (room_id, date))
  return cur.fetchall()

# 社員の予約を取得
def get_reserved_for_employee(employee_id):
  cur.execute("""SELECT id, room_id, date, check_in, check_out, purpose
                 FROM Reservations
                 WHERE employee_id = ?;""",
                 (employee_id,))
  return cur.fetchall()  

# 予約状況コマに表示する時間
hours = [f'{h}:00' for h in range(9, 18)]
# 予約状況コマの背景色
colors = ['#FFFFFF' for _ in range(len(hours))]

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

### ログイン画面 ###
if 'login' not in st.session_state:
  st.title('会議室予約システム')
  with st.form('login_form'):
    email = st.text_input('メールアドレス')
    password = st.text_input('パスワード', type='password')
    submit_btn = st.form_submit_button('ログイン')
  if submit_btn:
    user = authenticate_user(email, password)
    if user:      # ログイン成功
      st.session_state.login = user
      st.rerun()  # 会議室予約システム画面に切り替え
    else:
      st.error('メールアドレスまたはパスワードが間違っています。')

### 会議室予約システム画面 ###
elif st.session_state.login:
  # サイドバーのラジオボタン
  side_1 = st.sidebar.radio('予約 < - > キャンセル', ['予約', 'キャンセル'])

### 予約画面 ###  
  if side_1 == '予約':
    st.title('会議室予約システム')
     # 予約者
    st.write(f'社員番号：{st.session_state.login[0]}　氏名：{st.session_state.login[1]}')
  
    # 予約会議室の選択
    rooms = get_rooms()
    select_room_name = [room[1] for room in rooms]
    room_name = st.selectbox('会議室を選択してください：', select_room_name)
    
    # 予約する日付
    date = st.date_input('予約日：')
    
    # コマ分のカラムを作成
    st.write('色がついている時間帯はすでに予約済みです。')
    chek_in_hours = get_check_in_hours(get_room_id(room_name), date)
    cols = st.columns(len(hours), gap = 'small')
    for i, col in enumerate(cols):
      with col:
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

    # 使用目的
    purpose = st.text_input('使用目的を入力してください：')
    if check_in == None or check_out == None:
      st.error('予約できません。')
    else:
      # 予約ボタン
      bnt_1 = st.button('予約')
      if bnt_1:
        add_reservation(st.session_state.login[0],
                  get_room_id(room_name), # 会議室名からIDを取得
                  date,
                  check_in,
                  check_out,
                  purpose)
        st.write('予約しました。')
        st.rerun()

### キャンセル画面 ###  
  elif side_1 == 'キャンセル':
    st.title('予約キャンセル')
    st.write(f'社員番号：{st.session_state.login[0]}　氏名：{st.session_state.login[1]}')
    reserved = get_reserved_for_employee(st.session_state.login[0])
    for r_id, room_id, date, check_in, check_out, purpose in reserved:
      col1, col2 = st.columns([4, 2], gap = 'small', border = True)
      with col1:
        col3, col4 = st.columns(2, gap = 'small')
        with col3: 
          st.write(f'予約ID：{r_id}　{get_room_name(room_id)}')
          st.write(f'入室時間：{check_in}')
        with col4:
          st.write(f'予約日：{date}')
          st.write(f'退出時間：{check_out}')
        st.write(f'使用目的：{purpose}')
      with col2:
        if st.button('キャンセル', key = f'delete_{r_id}'):
          delete_reservation(r_id)
          st.rerun()

# 接続の切断
conn.close()