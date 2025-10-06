import streamlit as st
import sqlite3

# データベースの初期化
conn = sqlite3.connect('todo.db')
cur = conn.cursor()

# Taskテーブルを生成する関数
def create_table():
  cur.execute("""CREATE TABLE IF NOT EXISTS Tasks (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 task TEXT NOT NULL);""")
  conn.commit()

# 新規タスクを追加する関数
# 引数 task：追加するタスク
def add_task(task):
  cur.execute("""INSERT INTO Tasks (task)
                 VALUES (?)""",
                 (task,))
  conn.commit()

# タスク一覧を取得する関数
def get_tasks():
  cur.execute("""SELECT * FROM Tasks""")
  return cur.fetchall()

# タスクを削除する関数
# 引数 task_id：削除するタスクのid
def delete_task(task_id):
  cur.execute("""DELETE FROM Tasks
                 WHERE id = ?""",
                 (task_id,))
  conn.commit()

# タスクを更新する関数
# 引数 task_id：更新するタスクのid
# 引数 new_task:更新する新しいタスク
def update_task(task_id, new_task):
  cur.execute("""UPDATE Tasks SET task = ?
                 WHERE id = ?""",
                (new_task, task_id))
  conn.commit()

# テーブルの生成
create_table()

### Streamlitのコード ###
st.title('ToDo アプリ')

# 新規タスクの追加
with st.form('new_form', clear_on_submit = True):
  new_task = st.text_input('新しいタスクを入力してください :', key = 'input_text')
  submitted = st.form_submit_button('追加')
if submitted:
  add_task(new_task)

# タスクの一覧表示と操作
tasks = get_tasks()
for task_id, task in tasks:
  col1, col2, col3 = st.columns([4, 1, 1],
                                gap = 'small',
                                border = True)
  with col1:
    if f'edit_{task_id}' in st.session_state:
      new_value = st.text_input(f'タスクを変更（ID: {task_id}）',
                                value = task,
                                key = f'edit_input_{task_id}')
      if col2.button('保存', key = f'save_{task_id}'):
        update_task(task_id, new_value)
        del st.session_state[f"edit_{task_id}"]
        st.rerun()
    else:
      st.text(task)
  if f'edit_{task_id}' not in st.session_state:
    with col2:
      if st.button('変更', key = f'edit_button_{task_id}'):
        st.session_state[f'edit_{task_id}'] = True
        st.rerun()
  with col3:
    if st.button('削除', key = f'delete_{task_id}'):
      delete_task(task_id)
      st.rerun()
