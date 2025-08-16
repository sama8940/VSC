import sqlite3

# SQL文の実行と表示を行う関数
def row_print(sql_query):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    for row in cur.execute(sql_query):
        print(row)
    print() # 改行

    conn.close()

# WHERE句に使用例
print('Nameが「小林 健」と等しい行')
sql = """SELECT * FROM Employees WHERE Name = '小林 健';"""
row_print(sql)

print('EmployeeIDが4以上の行')
sql = """SELECT * FROM Employees WHERE EmployeeID >= 4;"""
row_print(sql)

print('Departmentが「営業部」以外の行')
sql = """SELECT * FROM Employees WHERE Department != '営業部';"""
row_print(sql)