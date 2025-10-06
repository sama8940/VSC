import streamlit as st
tasks = dict([
 ('1', '牛乳を買う'),
 ('2', '洗濯をする'),
 ('3', '髪をきる')
])
for task_id, value in tasks.items():
  # 1行ごとに3つのカラムを作成
  col1, col2, col3 = st.columns([4, 1, 1],
                                gap = 'small',
                                border = True)
  with col1:  # 最初のカラムにタスクを表示
    st.text(tasks[task_id])
  with col2:  # 次のカラムに[変更 ]ボタンを表示
    st.button('変更 ', key = f'edit_button_{task_id}')
  with col3:  # 次のカラムに[削除 ]ボタンを表示
    st.button('削除 ', key = f'delete_{task_id}')