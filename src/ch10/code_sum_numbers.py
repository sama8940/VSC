# 配列から合計値を計算する

def sum_numbers(s):
    try:
        a, b, c = map(int, s.split(','))
        return a + b + c
    except ValueError:
        return 'error'
    