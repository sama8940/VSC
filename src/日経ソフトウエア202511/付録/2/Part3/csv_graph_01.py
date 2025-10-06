import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title('CSVグラフ化ツール')

uploaded_file = st.file_uploader("CSVファイルのアップロード", type="csv")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, encoding='utf-8')
  st.write(df) # 読み込めているか確認用
