import streamlit as st

# text_input関数のテスト
new_task = st.text_input('新しいタスクを入力してください :')

# button関数のテスト
if st.button('追加'):
  st.text(f'「{new_task}」を追加しました。')
