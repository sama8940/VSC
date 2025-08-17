import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

def update_test(sql_query):
    try:
        cur.execute(sql_query)
    except Exception as e:
        print(f'例外メッセージ: {e}')

conn.commit()

# Column1が2の行のColumn4を'Orange'に変更
sql = """UPDATE Test
        SET Column4 = 'Orange'
        WHERE Column1 = 2;"""
update_test(sql)

# Column1が4の行のColumn2を150に変更
# Column4も'Banana'に変更
sql = """UPDATE Test
        SET Column2 = 150,
        Column4 = 'Banana'
        WHERE Column1 = 4;"""
update_test(sql)

for row in cur.execute("""SELECT * FROM Test;"""):
    print(row)

conn.close()
