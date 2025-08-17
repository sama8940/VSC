import sqlite3

try:
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    # Testテーブルの作成
    cur.execute("""CREATE TABLE Test(
            Column1 INTEGER PRIMARY KEY,
            Column2 INTEGER,
            Column3 TEXT UNIQUE,
            Column4 TEXT DEFAULT 'AAA' NOT NULL);""")
    
    print('Testテーブルを新規に作成しました。')

except sqlite3.OperationalError as e:
    print(f'CREATE TABLEに失敗しました。: {e}')

finally:
    conn.close()