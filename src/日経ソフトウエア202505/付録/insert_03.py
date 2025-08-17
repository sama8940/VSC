import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

def insert_test(sql_query):
    try:
        cur.execute(sql_query)
    except Exception as e:
        print(f'例外メッセージ : {e}')

# Column1に、すでにある「1」を追加してみる
sql = """INSERT INTO Test
        VALUES
        (1, 99, 'NMO', 'BBB');"""
insert_test(sql)

# Column4にNULLを入れてみる
sql = """INSERT INTO Test
        VALUES
        (6, 300, 'PQR', NULL);"""
insert_test(sql)

for row in cur.execute("""SELECT * FROM Test;"""):
    print(row)

conn.close()