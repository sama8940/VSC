import streamlit as st

st.title('Sessionカウンター')

count = 0
if 'count' not in st.session_state:
  # session_state.count（countがKey）に0を保存
  st.session_state.count = 0

bnt_1 = st.button('カウントボタン')

if bnt_1:
  # session_state.countの数値を1増やす
  st.session_state.count += 1

st.text(f'カウント：{st.session_state.count}')
