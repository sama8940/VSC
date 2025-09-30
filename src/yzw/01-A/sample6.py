# 曜日が書かれた板
day_of_week_board = '日 月 火 水 木 金 土'

# 日付が書かれた板
days_board = \
'★  ★  ★  ★  ★   1  2  3  4  5  6  7  \n' + \
' 2  3  4  5  6  7  8  9 10 11 12 13 14 \n' + \
' 9 10 11 12 13 14 15 16 17 18 19 20 21 \n' + \
'16 17 18 19 20 21 22 23 24 25 26 27 28 \n' + \
'23 24 25 26 27 28 29 30 31 ★  ★  ★  ★ \n' + \
'30 31 ★  ★  ★  ★  ★  ★  ★  ★  ★  ★  ★ \n'

# 年月をキー入力する
year = int(input('year = '))
month = int(input('month = '))

# 1月と2月は、前年の13月と14月にする
if month == 1 or month == 2:
    year -= 1
    month += 12

# フェアフィールドの公式で経過日数を求める
day = 1
days = 42 + 28 + 365 * (year - 1) 
+ year // 4 - year // 100 + year // 400 \
+ (306 + (month + 1) //10) -122 + days \
    
# 日曜日〜土曜日を0〜6で得る
day_of_week = days % 7

# 曜日が書かれた板をスライドさせて表示する
print(' ' *3 * (6 - day_of_week) + day_of_week_board)

# 日付が書かれた板をそのま表示する
print(days_board)