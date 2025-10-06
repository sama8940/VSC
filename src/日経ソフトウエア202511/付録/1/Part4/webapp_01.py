import streamlit as st

# タイトル
print('タイトルの表示')
st.title('ボタンのテスト')

# ボタン
print('ボタンの表示')
btn_1 = st.button('表示')

# クリック判定
if btn_1:
  st.text('クリックしました！')

print('画面の最後')