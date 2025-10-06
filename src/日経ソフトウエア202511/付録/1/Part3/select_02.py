import sqlite3 

# SQL文の実行と表示を行う関数
def row_print(sql_query):
  conn = sqlite3.connect('sample.db')
  cur = conn.cursor()

  for row in cur.execute(sql_query):
    print(row)
  print() # 改行

  conn.close()

# HireDateが'2020-01-01'以降の人
# HireDateで降順'表示
sql = """SELECT *
         FROM Employees
         WHERE HireDate > '2020-01-01'
         ORDER BY HireDate DESC;"""
row_print(sql)
