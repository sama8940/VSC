import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 折れ線グラフの描画
def line_graph(color_1, color_2):
  plt.rcParams['font.family'] = 'MS Gothic'
  fig, ax = plt.subplots()
  ax.plot(df['X'], df['Y_1'], color = color_1, marker = 'o', label = 'Y_1')
  ax.plot(df['X'], df['Y_2'], color = color_2, marker='s', label='Y_2')
  ax.set_xlabel('X軸')
  ax.set_ylabel('Y軸の値')
  ax.set_title('Xに対するY_1とY_2の折れ線グラフ')
  ax.legend()
  ax.grid(True)
  st.pyplot(fig)

# 棒グラフの描画
def bar_graph(color_1, color_2):
  plt.rcParams['font.family'] = 'MS Gothic'
  x = np.arange(len(df['X']))
  width = 0.35
  fig, ax = plt.subplots()
  ax.bar(x - width/2, df['Y_1'],color = color_1, width = width, label = 'Y_1')
  ax.bar(x + width/2, df['Y_2'],color = color_2, width = width, label='Y_2')
  ax.set_xlabel('X軸')
  ax.set_ylabel('Y軸の値')
  ax.set_title('Xに対するY_1とY_2の棒グラフ')
  ax.set_xticks(x)
  ax.set_xticklabels(df['X'])
  ax.legend()
  ax.grid(True)
  st.pyplot(fig)

select_graph = ['折れ線グラフ', '棒グラフ']
select_color = ['red', 'blue', 'green']

st.title('CSVグラフ化ツール')

uploaded_file = st.file_uploader("CSVファイルのアップロード", type="csv")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, encoding='utf-8')
  with st.form('test_form'):
    input_1 = st.radio( 'グラフを選択してください：', select_graph )
    input_2 = st.selectbox( 'Y_1の色を選択してください：', select_color )
    input_3 = st.selectbox( 'Y_2の色を選択してください：', select_color )
    submit_btn = st.form_submit_button('表示')
    if submit_btn:
      if input_1 == '折れ線グラフ':
  	    line_graph(input_2, input_3)
      else:		# 棒グラフ
        bar_graph(input_2, input_3)
