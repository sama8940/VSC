# ライブラリのインポート
import sqlite3 
import datetime

# カスタムアダプター、カスタムコンバーターの作成と登録
sqlite3.register_adapter(datetime.date, lambda d: d.isoformat())
sqlite3.register_converter("DATE", lambda s: datetime.date.fromisoformat(s.decode("utf-8")))

# データベースへの接続（ない場合は作成）
db_name = 'booking.db'
conn = sqlite3.connect(db_name)
print(db_name + 'を作成しました。')

# カーソルオブジェクトの取得
cur = conn.cursor()

# Employees テーブルの生成
cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
               id TEXT PRIMARY KEY,
               name TEXT NOT NULL,
               email TEXT NOT NULL UNIQUE,
               password TEXT NOT NULL);""");
print('Employeesテーブルを作成しました。')
conn.commit()

# Employees データの入力
cur.execute("""INSERT INTO Employees
               (id, name, email, password)
               VALUES
('100123', '田中 太郎', 'tanaka.taro@example.com', 'taro_1234'),
('200123', '佐藤 花子', 'sato.hanako@example.com', 'hanako_1234'),
('300123', '高橋 次郎', 'takahashi.jiro@example.com', 'jiro_1234');""")
conn.commit()

# Employees データの表示
print('Employees')
for row in cur.execute("""SELECT * FROM Employees;"""):
  print(row)

# Rooms テーブルの生成
cur.execute("""CREATE TABLE IF NOT EXISTS Rooms (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL UNIQUE);""");
print('Roomsテーブルを作成しました。')
conn.commit()

# Rooms データの入力
cur.execute("""INSERT INTO Rooms
               (name)
               VALUES
               ('会議室 A'),
               ('会議室 B'),
               ('会議室 C');""")
conn.commit()

# Rooms データの表示
print('Rooms')
for row in cur.execute("""SELECT * FROM Rooms;"""):
  print(row)


# Reservations テーブルの生成
cur.execute("""CREATE TABLE IF NOT EXISTS Reservations (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               employee_id TEXT NOT NULL,
               room_id TEXT NOT NULL,
               date TEXT NOT NULL,
               check_in TEXT NOT NULL,
               check_out TEXT NOT NULL,
               purpose TEXT);""");
print('Reservationsテーブルを作成しました。')
conn.commit()

# Reservations データの入力
cur.execute("""INSERT INTO Reservations (
               employee_id, room_id, date, check_in, check_out, purpose)
               VALUES
('100123', 1, '2025-07-14', '9:00', '12:00', '新規プロジェクト、キックオフ'),
('100123', 1, '2025-07-14', '13:00', '14:00', '新製品お披露目会'),
('100123', 2, '2025-07-14', '13:00', '14:00', 'A社と打ち合わせ'),
('200123', 2, '2025-07-16', '10:00', '11:00', 'B社と打ち合わせ'),
('300123', 2, '2025-07-17', '16:00', '18:00', 'Bプロジェクト、レビュー'),
('300123', 3, '2025-07-17', '10:00', '11:00', 'C社と打ち合わせ');""")
conn.commit()

# Reservations データの表示
print('Reservations')
for row in cur.execute("""SELECT * FROM Reservations;"""):
  print(row)

# 接続の切断
conn.close()
