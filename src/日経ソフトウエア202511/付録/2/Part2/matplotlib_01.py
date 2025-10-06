import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# サンプルデータ
df = pd.DataFrame({
  'X': ['ABC', 'DEF', 'GHI', 'JKL', 'MNO'],  # Xデータ
  'Y_1': [100, 150, 100, 200, 175],          # Y_1データ
  'Y_2': [30, 10, 40, 20, 50]                # Y_2データ
})
# フォントを明示的に指定（ 例：MS Gothic）
plt.rcParams['font.family'] = 'MS Gothic'
# グラフ全体のオブジェクト(fig）と軸オブジェクト（ax）の取得
fig, ax = plt.subplots()
# 折れ線の描画（Y_1）
ax.plot(
  df['X'],         # X軸のデータ
  df['Y_1'],       # Y軸のデータ
  color = 'red',   # 線の色（レッド）
  marker = 'o',    # 各データ点に丸印（ ○）を付ける
  label = 'Y_1'    # 凡例の名前
)
# 折れ線の描画（Y_2）
ax.plot(
  df['X'],          # X軸のデータ
  df['Y_2'],        # Y軸のデータ
  color = 'green',  # 線の色（グリーン）
  marker='s',       # 各データ点に四角形（ □）を付ける
  label='Y_2'       # 凡例の名前
)
# グラフの装飾
ax.set_xlabel('X軸')      # X軸のラベル
ax.set_ylabel('Y軸の値')  # Y軸のラベル
ax.set_title('Xに対するY_1とY_2の折れ線グラフ')
ax.legend()    # 凡例（ データ種別）の自動生成
ax.grid(True)  # グリッド表示
# Streamlitで表示
st.pyplot(fig)