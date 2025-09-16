# 引数で指定された西暦がうるう年かどうかを判定する関数
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

# 引数で指定された年月の1日が何曜日かを返す関数
def day_of_week(year, month):
    # 1月と2月は、前年の13月と14月にする
    if month == 1 or month == 2:
        year -= 1
        month += 12

    # 日に1日を設定する
    day = 1

    # フェアフィールドの公式で経過日数を求める
    days = 31 + 28 + 365 * (year - 1) \
    + year // 4 - year // 100 + year // 400 \
    + (306 * (month + 1) // 10) - 122 + day

    # 日曜日～土曜日を0～6で返す
    return days % 7

# メインプログラム
if __name__ == '__main__':
    # 1月～12月の月の日数
    days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 年月をキー入力する
    year = int(input('year = '))
    month = int(input('month = '))

    # うるう年の場合は、2月の日数を29日にする
    if leap_year(year):
        days_of_month[2] = 29

    # 1日の曜日を取得する
    first_day = day_of_week(year, month)

    # 年月と曜日を表示する
    print(str(year) + '年' + str(month) + '月')
    print("日 月 火 水 木 金 土")

    # 1日の前に空白（１日あたり3文字）を表示する
    print(' ' * first_day * 3, end = '')

    # 日を表示する
    for day in (range(1, 1 + days_of_month[month])):
        # 2文字右詰＋空白1文字＝3文字で表示する
        print(format(day, '>2') + ' ', end = '')

        # 土曜日を表示したら改行する
        if (day + first_day - 1) % 7 == 6:
            print()

    # 最後にもう1度改行する
    print()