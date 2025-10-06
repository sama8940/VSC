import streamlit as st
import pandas as pd

# サンプルデータ
df = pd.DataFrame({
  'X': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO'],	# Xデータ
  'Y_1': [100, 150, 100, 200, 175],		# Y_1データ
  'Y_2': [30, 10, 40, 20, 50]			# Y_2データ
})

# 折れ線グラフの描画
st.line_chart(
  data = df,			# データ
  x='X',			# Xデータのキー
  y=['Y_1', 'Y_2'],		# Yデータのキー
  x_label = 'X軸',		# Xのラベル
  y_label = 'Y軸', 		# Yのラベル
  color=['#FF0000', '#0000FF'],	# 線の色（複数ならリスト）
)
