import streamlit as st
# Tasksテーブルの代用の辞書
tasks = dict([
 ('1', '牛乳を買う'),
 ('2', '洗濯をする'),
 ('3', '髪をきる')
])
# タスク1つ分の表示
st.text(tasks['1'])
st.button('変更 ')
st.button('削除 ')