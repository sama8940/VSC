import streamlit as st
tasks = dict([
 ('1', '牛乳を買う'),
 ('2', '洗濯をする'),
 ('3', '髪をきる')
])
# 全部のタスクを表示
for task_id, value in tasks.items():
  st.text(tasks[task_id])
  st.button('変更 ')  # 2回目の表示でエラーになる
  st.button('削除 ')