import sqlite3

# データベースへ接続
conn = sqlite3.connect('sample.db')

# カーソルオブジェクトの取得
cur = conn.cursor()

# Employeesテーブルの生成
cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    HireDate TEXT NOT NULL,
    Department TEXT NOT NULL);""");
print('Employeesテーブルを作成しました。')

# 接続の切断
conn.close()
