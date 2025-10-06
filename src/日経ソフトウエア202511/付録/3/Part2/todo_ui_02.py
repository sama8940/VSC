import streamlit as st

# form関数の引数に「clear_on_submit = True」を追加
with st.form('new_form', clear_on_submit = True):
  new_task = st.text_input('新しいタスクを入力してください :')
  submit_btn = st.form_submit_button('追加')

if submit_btn:
  st.text(f'「{new_task}」を追加しました。')
