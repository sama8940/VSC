import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

def update_test(sql_query):
    try:
        cur.execute(sql_query)
    except Exception as e:
        print(f'例外メッセージ: {e}')
    
    conn.commit()

# Column1が2の行のみ削除
sql = """DELETE FROM Test
        WHERE Column1 = 2;"""
update_test(sql)

for row in cur.execute("""SELECT * FROM Test;"""):
    print(row)

conn.close()

