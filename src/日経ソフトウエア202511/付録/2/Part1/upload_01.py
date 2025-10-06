import streamlit as st

st.title("テキストファイルビューア")

# ファイルのアップロード
uploaded_file = st.file_uploader("テキストファイルを選択してください")

# ファイルがアップロードされていれば実行
if uploaded_file is not None:
  # テキストファイルの内容を読み込む
  content = uploaded_file.read().decode("utf-8")
  # 内容の表示
  st.text_area("ファイルの内容", content, height=200)