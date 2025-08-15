import sqlite3

# データベースへの接続
conn = sqlite3.connect('sample.db')

# カーソルオブジェクトの取得
cur = conn.cursor()


# SELECT文ですべてのデータを抽出
print('SELECT * FROM Employees;の実行')
for row in cur.execute("""SELECT * FROM Employees;"""):
    print(row)

# 接続の切断
conn.close()