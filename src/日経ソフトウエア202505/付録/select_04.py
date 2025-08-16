import sqlite3

# SQL文の実行と表示を行う関数
def row_print(sql_query):
    conn = sqlite3.connect('sample.db')
    cur = conn.cursor()

    for row in cur.execute(sql_query):
        print(row)
    print() # 改行

# WHERE句の使用例
print('Nameが「小林 健」ではない行')
sql = """SELECT * FROM Employees WHERE NOT Name = '小林 健';"""
row_print(sql)

print('EmployeeIDが4以上6未満の行')
sql = """SELECT * FROM Employees WHERE EmployeeID >= 4 AND EmployeeID < 6;"""
row_print(sql)

print('Departmentが「総務部」か「営業部」の行')
sql = """SELECT * FROM Employees WHERE Department in ('総務部','営業部')"""
row_print(sql)
