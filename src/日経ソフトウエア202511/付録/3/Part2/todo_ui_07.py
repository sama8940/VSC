import streamlit as st
# tasksをセッションに入れておく
if "tasks" not in st.session_state:
  st.session_state.tasks = dict([
    ('1', '牛乳を買う'),
    ('2', '洗濯をする'),
    ('3', '髪をきる')
  ])
for task_id, value in st.session_state.tasks.items():
  col1, col2, col3 = st.columns([4, 1, 1],
                                gap = 'small',
                                border = True)
  with col1:
    st.text(st.session_state.tasks[task_id])
  with col2:
    st.button('変更 ', key = f'edit_button_{task_id}')
  with col3:
    # [削除 ]ボタンの表示
    if st.button('削除 ', key = f'delete_{task_id}'):
      # [削除 ]ボタンのクリックで同じtask_idの要素を削除
      del st.session_state.tasks[task_id]
      # 画面の更新
      st.rerun()