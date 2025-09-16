import math

# 引数nが素数かどうか判定する関数の定義
def is_prime(n):
    # 1は素数ではない
    if (n == 1):
        return False

    # 2は素数である
    if (n == 2):
        return True
    
    # 2より大きい偶数は素数ではない
    if (n % 2 == 0):
        return False
    
    # 3は素数である
    if (n == 3):
        return True
    
    # 3から√nまでのすべての奇数で割ってみる
    div = 3 # 除数の初期値
    max = int(math.sqrt(n)) # 3からmaxまでで割ってみる
    while (div <= max):
        # 割り切れる数が見つかれば素数ではない
        if (n % div == 0):
            return False
        # 除数を2増やす（次の奇数に進める）
        div += 2

    # 割り切れる数が見つからなければ素数である
    return True

# 100以下のすべての素数を表示するプログラム
if __name__ == '__main__':
    # 100以下のすべての素数を表示する
    n = 1
    while (n <= 100):
        if (is_prime(n)):
            print(n, ", ", sep="", end="")
        n += 1
    print()