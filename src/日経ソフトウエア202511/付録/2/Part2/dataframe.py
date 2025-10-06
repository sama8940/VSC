import streamlit as st
import pandas as pd

# 辞書（列ラベル（key）:データ（value）)
data = {
  'name': ['Taro', 'Hanako', 'Jiro'],
  'age': [15, 16, 15],
  'score': [80, 90, 60]
}

# 辞書をDataFrameに変換
df = pd.DataFrame(data)

# DataFrameの表示
st.write(df)
