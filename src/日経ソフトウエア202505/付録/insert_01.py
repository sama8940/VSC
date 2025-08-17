import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

# 行の追加と表示を行う関数
def insert_test(sql_query):
    cur.execute(sql_query)
    conn.commit()

# 列名を省略して1行追加
sql ="""INSERT INTO Test VALUES(1, 99, 'ABC', 'あいう');"""
insert_test(sql)

# NULLとDEFALUTを使って2行同日以下
sql = """INSERT INTO Test (Column1, Column2, Column3)
    VALUES
    (2, 100, 'DEF'),
    (3, NULL, 'GHI');"""
insert_test(sql)

for row in cur.execute("""SELECT * FROM Test;"""):
    print(row)

conn.close()
