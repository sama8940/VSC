import sqlite3

# データベースへ接続
conn = sqlite3.connect('sample.db')

# カーソルオブジェクトの取得
cur = conn.cursor()

# execute関数を単独で呼び出す
cur.execute("""SELECT * FROM Employees;""")

# fetchall関数で全データを取り出す
rows = cur.fetchall()
print(rows)

# 接続の切断
conn.close()