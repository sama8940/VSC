import streamlit as st
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
    # [変更 ]ボタンがクリックされている
    if f'edit_{task_id}' in st.session_state:
      # テキストフィールドをcol1に表示
      new_value = st.text_input(f'タスクを変更（ID: {task_id}）',
                  value = st.session_state.tasks[task_id],
                  key = f'edit_input_{task_id}')
      # [変更 ]ボタンを[保存 ]ボタンに変更
      if col2.button('保存 ', key = f'save_{task_id}'):
        # 同じtask_idの要素を変更し画面を更新する
        st.session_state.tasks[task_id] = new_value
        # [変更 ]ボタンのクリック情報を削除
        del st.session_state[f"edit_{task_id}"]
        # 画面の更新
        st.rerun()
    # 通常のタスク表示
    else:
      st.text(st.session_state.tasks[task_id])
  # [変更 ]ボタンはまだクリックされていない
  if f'edit_{task_id}' not in st.session_state:
    with col2:
      # [変更 ]ボタンの表示
      if st.button('変更 ', key = f'edit_button_{task_id}'):
        # クリックで[変更 ]ボタンのクリック情報をTrueにする
        st.session_state[f'edit_{task_id}'] = True
        # 画面の更新
        st.rerun()
  with col3:
    # [削除 ]ボタンの表示
    if st.button('削除 ', key = f'delete_{task_id}'):
      # クリックで同じtask_idの要素を削除
      del st.session_state.tasks[task_id]
      # 画面の更新
      st.rerun()  