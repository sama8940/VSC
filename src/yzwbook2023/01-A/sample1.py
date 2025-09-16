# 引数で指定された西暦がうるう年かどうかを判定するプログラム
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
# メインプログラム

if __name__ == "__main__":
    print(leap_year(2019))
    print(leap_year(2020))
    print(leap_year(2100))
    print(leap_year(2400))