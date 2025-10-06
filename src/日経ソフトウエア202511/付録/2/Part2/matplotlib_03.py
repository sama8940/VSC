import streamlit as st
import matplotlib.pyplot as plt

# データの用意
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 25, 25]
colors = ['gold', 'skyblue', 'lightcoral', 'lightgreen']
explode = (0.1, 0, 0, 0)  # 最初の要素を少し強調表示

# フォントを明示的に指定（例：MS Gothic）
plt.rcParams['font.family'] = 'MS Gothic'

# Matplotlibで円グラフを作成
fig, ax = plt.subplots()
ax.pie(sizes,
 labels=labels,
 colors=colors,
 explode=explode, 
 autopct='%1.1f%%',
 shadow=True,
 startangle=90)

ax.set_title('カテゴリ別の割合')
ax.axis('equal')  # 円を真円にするため

# Streamlitで描画
st.pyplot(fig)