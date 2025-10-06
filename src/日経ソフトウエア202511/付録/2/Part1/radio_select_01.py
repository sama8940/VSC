import streamlit as st

# 選択肢のリスト
select_item = ['選択肢_A', '選択肢_B', '選択肢_C']

# ラジオボタン
input_1 = st.radio( '選択してください：', select_item )
st.text(f'ラジオボタン:{input_1}')

# セレクトボックス
input_2 = st.selectbox( '選択してください：', select_item )
st.text(f'セレクトボックス:{input_2}')

# マルチセレクト
input_3 = st.multiselect( '選択してください：', select_item )
st.text(f'マルチセレクト:{input_3}')
