# 引数で指定された西暦がうるう年かどうかを判定する関数
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
    
    # メインプログラム
if __name__ == '__main__':
    days = 0
    for year in range(1,2020):
        if (leap_year(year)):
            days += 366
        else:
            days += 365
    print(days)
    print(days % 7)