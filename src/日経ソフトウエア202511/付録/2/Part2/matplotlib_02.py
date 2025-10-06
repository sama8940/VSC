import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# サンプルデータ
df = pd.DataFrame({
  'X': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO'],	# Xデータ
  'Y_1': [100, 150, 100, 200, 175],		# Y_1データ
  'Y_2': [30, 10, 40, 20, 50]			# Y_2データ
})

# フォントを明示的に指定（例：MS Gothic）
plt.rcParams['font.family'] = 'MS Gothic'

# X軸の目盛り位置
x = np.arange(len(df['X'])) # 整数の配列で生成

# 棒の幅
width = 0.35

# グラフ全体のオブジェクト(fig）と軸オブジェクト（ax）の取得
fig, ax = plt.subplots()

# 棒グラフの描画（Y_1）
ax.bar(
  x - width/2,		# X軸のデータ（半分幅のバーを左寄せ配置）
  df['Y_1'],		# Y軸のデータ
  color = 'red',	# 線の色（レッド）
  width = width,	# 棒の幅
  label = 'Y_1')	# 凡例の名前

# 棒グラフの描画（Y_2）
ax.bar(
  x + width/2,		# X軸のデータ（半分幅のバーを右寄せ配置）
  df['Y_2'],		# Y軸のデータ
  color = 'green',	# 線の色（グリーン）
  width = width,	# 棒の幅
  label='Y_2'		# 凡例の名前
)

# グラフの装飾
ax.set_xlabel('X軸')		# X軸のラベル
ax.set_ylabel('Y軸の値')	# Y軸のラベル
ax.set_title('Xに対するY_1とY_2の棒グラフ')
ax.set_xticks(x)		# X軸の目盛り位置
ax.set_xticklabels(df['X'])	# X軸の目盛りラベル
ax.legend()			# 凡例（データ種別）の自動生成
ax.grid(True)			# グリッド表示

# Streamlitで表示
st.pyplot(fig)
