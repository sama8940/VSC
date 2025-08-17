import sqlite3

# SQL文の実行と表示を行う関数
def row_print(sql_query):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    for row in cur.execute(sql_query):
        print(row)
    print() # 改行

    conn.close()

# データベース保有するテーブルの一覧
sql = """SELECT name FROM sqlite_master WHERE type='table';"""
row_print(sql)