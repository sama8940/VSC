import streamlit as st
tasks = dict([
 ('1', '牛乳を買う'),
 ('2', '洗濯をする'),
 ('3', '髪をきる')
])
for task_id, value in tasks.items():
  st.text(tasks[task_id])
  # 各ボタンのkeyにユニークな値を指定
  st.button('変更 ', key = f'edit_button_{task_id}')
  st.button('削除 ', key = f'delete_{task_id}')