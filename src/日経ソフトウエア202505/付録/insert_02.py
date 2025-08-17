import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

def insert_test(sql_query):
    cur.execute(sql_query)
    conn.commit()
try:
# INTEGER型の列に「数字」を入れる
    sql = """INSERT INTO Test
            VALUES
            ('4', '99', 'JKL', 'あいう');"""
    insert_test(sql)

# TEXT型の列に「数値」を入れる  
    sql = """INSERT INTO Test
        VALUES
        (5, 200, 300, 400);"""
    insert_test(sql)
except:
    pass

for row in cur.execute("""SELECT * FROM Test;"""):
    print(row)

conn.close()