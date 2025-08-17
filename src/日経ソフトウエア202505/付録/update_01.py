import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

def update_test(sql_query):
    try:
        cur.execute(sql_query)
    except Exception as e:
        print(f'例外メッセージ: {e}')
    
    conn.commit()

# Column4をすべて'Apple'に変更
sql = """UPDATE Test
        SET Column4 = 'Apple';"""
update_test(sql)

for row in cur.execute("""SELECT * FROM Test;"""):
    print (row)

conn.close()
