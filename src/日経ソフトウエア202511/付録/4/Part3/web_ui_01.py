import streamlit as st
import sqlite3 
import datetime

# カスタムアダプター、カスタムコンバーターの作成と登録
sqlite3.register_adapter(datetime.date, lambda d: d.isoformat())
sqlite3.register_converter("DATE", lambda s: datetime.date.fromisoformat(s.decode("utf-8")))

db_name = 'booking.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

# ユーザー認証
def authenticate_user(email, password):
  cur.execute("""SELECT * 
                 FROM Employees
                 WHERE email = ? AND password = ?""",
                 (email, password))
  return cur.fetchone()

### ログイン画面 ###
if 'login' not in st.session_state:
  st.title('ログイン画面')
  with st.form('login_form'):
    email = st.text_input('メールアドレス')
    password = st.text_input('パスワード', type='password')
    submit_btn = st.form_submit_button('ログイン')

  if submit_btn:
    user = authenticate_user(email, password)
    if user:      # ログイン成功
      st.session_state.login = user # セッションにセット
      st.rerun()  # 会議室予約システム画面に切り替え
    else:
      st.error('メールアドレスまたはパスワードが間違っています。')

### 会議室予約システム画面 ###
elif st.session_state.login:
 st.title('予約画面')

# 接続の切断
conn.close()