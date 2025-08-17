import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

def in_rep_test(sql_query):
    try:
        cur.execute(sql_query)
    except Exception as e:
        print(f'例外メッセージ : {e}')

    conn.commit()

print('現時点のテーブル')
for row in cur.execute("""SELECT * FROM  Test;"""):
    print(row)

# データの追加
sql = """INSERT OR REPLACE INTO Test
        VALUES
        (6, 300, 'NMO', 'Orange');"""
in_rep_test(sql)

print('追加したデータの確認')
for row in cur.execute("""SELECT * FROM  TEST;"""):
    print(row)

print() # 改行

# Column1が1の行のデータを変更
sql = """INSERT OR REPLACE INTO Test
        VALUES
        (1, 100, 'xyz', 'Strawberry');"""
in_rep_test(sql)

print('変更したデータの確認')
for row in cur.execute("""SELECT * FROM Test;"""):
    print(row)
    
conn.close()