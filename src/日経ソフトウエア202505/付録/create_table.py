import sqlite3

# データベースへ接続
conn = sqlite3.connect('sample.db')

# カーソルオブジェクトの取得
cur = conn.cursor()

# Employeesテーブルの作成
cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    HireDate TEXT NOT NULL,
    Department TEXT NOT NULL);""")
print ('Employeesテーブルを作成しました。')

# データの入力
cur.execute("""INSERT INTO Employees (Name, Email, HireDate, Department) VALUES
    ('田中 太郎', 'tanaka.taro@example.com', '2022-04-01', '営業部'),
    ('鈴木 一郎', 'suzuki.ichiro@example.com', '2021-05-15', '総務部'),
    ('佐藤 花子', 'sato.hanako@example.com', '2020-06-20', '人事部'),
    ('高橋 次郎', 'takahashi.jiro@example.com', '2023-01-10', '開発部'),
    ('伊藤 美咲', 'ito.misaki@example.com', '2019-11-25', '営業部'),
    ('中村 太一', 'nakamura.taichi@example.com', '2022-03-05', '経理部'),
    ('山本 久美子', 'yamoamoto.kumiko@example.com', '2018-08-30', '総務部'),
    ('小林 健', 'kobayashi.ken@example.com', '2021-12-01', '開発部'),
    ('加藤 明', 'kato.akira@example.com', '2020-07-07', '人事部'),
    ('松本 理恵', 'matsumoto.rie@example.com', '2017-09-14', '経理部');""")

# SELECT文ですべてのデータを抽出
for row in cur.execute("""SELECT * FROM Employees;"""):
    print(row)

# ここでコミット
conn.commit()

# 接続の切断
conn.close()