# ライブラリのインポート
import sqlite3

# データベースへの接続（ない場合は作成）
db_name = 'sample.db'
conn = sqlite3.connect(db_name)
print(db_name + 'を作成しました。')

# 接続の切断
conn.close()
