import streamlit as st

# セレクトボックス
side_1 = st.sidebar.selectbox('予約 < - > キャンセル', ['予約', 'キャンセル'])

# ラジオボタン
# side_1 = st.sidebar.radio('予約 < - > キャンセル', ['予約', 'キャンセル'])

if side_1 == '予約':
  st.title('会議室予約システム')

elif side_1 == 'キャンセル':
  st.title('予約キャンセル')
