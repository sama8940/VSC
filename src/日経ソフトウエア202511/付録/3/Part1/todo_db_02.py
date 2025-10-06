import sqlite3

# 接続とカーソルオブジェクトの取得
conn = sqlite3.connect('todo.db')
cur = conn.cursor()

# id列が1の行にあるtask列を変更
cur.execute("""UPDATE Tasks
               SET task = 'クリーニングを出す'
               WHERE id = 1;""")
conn.commit()

# id列が2の行を削除
cur.execute("""DELETE FROM Tasks
               WHERE id = 2;""")
conn.commit()

# Tasksテーブルのデータを表示
cur.execute("""SELECT * FROM Tasks;""")
print(cur.fetchall())

# 接続の切断
conn.close()