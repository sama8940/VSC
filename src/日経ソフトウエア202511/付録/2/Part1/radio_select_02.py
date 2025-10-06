import streamlit as st

# 選択肢のリスト
select_item = ['選択肢_A', '選択肢_B', '選択肢_C']

# with句を使いフォームにまとめる
# form関数の引数「'test_form'」は、このフォームに付けた名前
with st.form('test_form'):
  # ラジオボタン
  input_1 = st.radio( '選択してください：', select_item )
  # セレクトボックス
  input_2 = st.selectbox( '選択してください：', select_item )
  # マルチセレクト
  input_3 = st.multiselect( '選択してください：', select_item )
  # ボタンは、サブミットボタン
  submit_btn = st.form_submit_button('表示')

# サブミットボタンがクリックされていたら
if submit_btn:
  st.text(f'ラジオボタン:{input_1}')
  st.text(f'セレクトボックス:{input_2}')
  st.text(f'マルチセレクト:{input_3}')
