import sqlite3

# データベースへ接続（無ければ生成）
conn = sqlite3.connect('todo.db')

# カーソルオブジェクトの取得
cur = conn.cursor()

# Tasksテーブルの生成
cur.execute("""CREATE TABLE IF NOT EXISTS Tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
task TEXT NOT NULL);""")
conn.commit()

# Tasksテーブルにデータを追加
cur.execute("""INSERT INTO Tasks (task) VALUES
               ('牛乳を買う'),
               ('洗濯をする'),
               ('髪をきる');""")
conn.commit()

# Tasksテーブルのデータを表示
cur.execute("""SELECT * FROM Tasks;""")
print(cur.fetchall())

# 接続の切断
conn.close()