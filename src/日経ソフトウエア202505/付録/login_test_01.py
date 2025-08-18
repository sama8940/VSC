import sqlite3
import streamlit as st

# データベース接続
conn = sqlite3.connect('login_app.db')
cur = conn.cursor()

# ユーザーテーブルの作成
cur.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL);""")
conn.commit()

# ユーザー認証
def authenticate_user(username, password):
    cur.execute("""SELECT * FROM users
                WHERE username=? AND password=?""",
                (username, password))
    return cur.fetchone()

# ユーザー登録
def register_user(username, password):
    user = authenticate_user(username, password)
    if user:
        # すでに登録済みのユーザーです。
        pass
    else:
        cur.execute("""INSERT INTO users
                    (username, password)
                    VALUES (?, ?);""",
                    (username, password))
        conn.commit()

# テスト用ユーザーとパスワードを作成
register_user('ITO', '1234')
register_user('SATO', '1234')

# ブラウザ画面
st.title("ログインテスト")

with st.form('login_form'):
    username = st.text_input('ユーザーID')
    password = st.text_input('パスワード')
    submit_btn = st.form_submit_button('ログイン')

if submit_btn:
    user = authenticate_user(username, password)
    if user:
        st.success(f'{username}さん、ログイン成功です。')
    else:
        st.error('IDまたはパスワードが間違っています。')
