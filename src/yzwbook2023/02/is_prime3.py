import math

# 素数のリスト（グローバル変数）
p_list = None

# make_p_list関数の処理回数（グローバル変数）
count = 0

# 引数n以下の素数の一覧表を返す関数の定義
def make_p_list(n):
    # グローバル変数を参照する
    global p_list, count

    # 要素数n+1個の配列を作り、すべての要素をTrueで初期化する
    p_list = [True] * (n + 1)
    
    # 0は素数ではない
    p_list[0] = False
    
    # 1は素数ではない
    p_list[1] = False
    
    # 処理回数をカウントする
    count = 1
    
    # 素数pの倍数にTrueを設定する
    p = 2 # 2は素数である
    max = int(math.sqrt(n)) # 2から√nまでチェックする
    while (p <= max):
        # p_list[p]がTrueならpは素数である
        if (p_list[p]):
            # 素数pの倍数をFalseにする
            q = p * 2
            while (q <= n):
                p_list[q] = False
                q += p
                # 処理回数をカウントする
                count += 1
        p += 1

# 引数nが素数かどうか判定する関数の定義
def is_prime(n):
    # グローバル変数を参照する
    global p_list

    # 素数の一覧表を参照して素数を判定する
    return p_list[n]

# 100以下のすべての素数を表示するプログラム
if __name__ == '__main__':
    # 100以下の素数の一覧表を作成する
    make_p_list(100)

    # 100以下のすべての素数を表示する
    n = 1
    while (n <= 100):
        if (is_prime(n)):
            print(n, ", ", sep="", end="")
        n += 1
    print()

    # 処理回数を表示する
    print(f"処理回数 = {count}")