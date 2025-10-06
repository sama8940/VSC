import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

select_graph = ['折れ線グラフ', '棒グラフ']
select_color = ['red', 'blue', 'green']

st.title('CSVグラフ化ツール')

uploaded_file = st.file_uploader("CSVファイルのアップロード", type="csv")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, encoding='utf-8')
  # st.write(df) 
  with st.form('test_form'):
    input_1 = st.radio( 'グラフを選択してください：', select_graph )
    input_2 = st.selectbox( 'Y_1の色を選択してください：', select_color )
    input_3 = st.selectbox( 'Y_2の色を選択してください：', select_color )
    submit_btn = st.form_submit_button('表示')
    if submit_btn:
      st.text(f'Y_1の色：{input_2}')
      st.text(f'Y_2の色：{input_3}')
      if input_1 == '折れ線グラフ':
        st.text(input_1)
      else:	# 棒グラフ
        st.text(input_1)
