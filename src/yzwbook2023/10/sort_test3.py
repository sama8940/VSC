import random
import time
import copy
import sys

# a[idx1]とa[idx2]を交換する関数の定義
def swap(a, idx1, idx2):
    temp = a[idx1]
    a[idx1] = a[idx2]
    a[idx2] = temp

# 配列の内容が昇順にソートされていることをチェックする関数の定義
def is_asc_sorted(a):
    # 配列の要素数をnに得る
    n = len(a)
    # 隣同士の要素を比較することを繰り返す
    i = 1
    while i < n:
        # 昇順になっていない部分があればFalseを返す
        if (a[i - 1] > a[i]):
            return False
        i += 1
    # すべての部分が昇順になっていればTrueを返す
    return True

# 昇順で挿入ソートを行う関数の定義
def insertion_sort(a, left, right):
    # 挿入する要素の添字iの初期値を左端+1にする
    i = left + 1
    # 右端の要素まで挿入を繰り返す
    while i <= right:
        # 挿入する要素の現在位置をjに設定する
        j = i
        # 1つ前の要素 > 挿入する要素、であれば、両者を交換することを繰り返す
        while j > 0 and a[j - 1] > a[j]:
            # 1つ前の要素と挿入する要素を交換する
            temp = a[j - 1]
            a[j - 1] = a[j]
            a[j] = temp
            # 挿入する要素の現在位置を1つ前に進める
            j -= 1
        # 挿入する要素の添字iを次の要素に設定する
        i += 1

# 昇順でシェルソートを行う関数の定義
def shell_sort(a, left, right):
    # 間隔hの初期値を決める
    max = (right - left + 1) // 9
    h = 1
    while h <= max:
        h = h * 3 + 1

    # 間隔hを初期値から1まで徐々に狭めながら挿入ソートを繰り返す
    while h >= 1:
        # 以下は挿入ソートと同様
        i = h
        while i <= right:
            j = i
            while j > h - 1 and a[j - h] > a[j]:
                temp = a[j - h]
                a[j - h] = a[j]
                a[j] = temp
                j -= h
            i += 1
        # 間隔hを狭める
        h = (h - 1) // 3

# 配列を要素の大小で二分割して基準値の添字を返す関数の定義
def split_array(a, left, right):
    # 基準値（配列の中央の値）を配列の左端に配置する
    mid = (left + right) // 2
    swap(a, left, mid)

    # 基準値より小さい要素を前側に、大きい要素を後ろ側に配置する
    pivot_val = a[left] # 基準値の値をpivot_valに得る
    i = left + 1 # 前方からチェックする位置をiとする
    j = right # 後方からチェックする位置をjとする
    while (True):
        # チェックした要素が基準値より小さい限りiを後ろに進める
        while (i <= right and a[i] < pivot_val):
            i += 1
        # チェックした要素が基準値より大きい限りjを前に進める
        while (j >= left and a[j] > pivot_val):
            j -= 1
        # iとjが逆転または同じ要素を指していれば、要素の配置は完了である
        if (i >= j):
            break
        # 前側にある大きい要素と後ろ側にある小さい要素を交換する
        swap(a, i, j)
        # チェック位置を次に進める
        i += 1
        j -= 1

    # 配列の左端にある基準値を適切な位置に入れる
    swap(a, left, j)

    # 基準値の添字を返す
    return j

# 昇順でクイックソートを行う関数の定義
def quick_sort(a, left, right):
    # 配列の要素数が1個より大きければ以下を再帰呼び出しで繰り返す
    if (left < right):
        # 配列を要素の大小で二分割する
        pivot = split_array(a, left, right)
        
        # 分割した前側の配列に同じ処理を行う
        quick_sort(a, left, pivot - 1)

        # 分割した後ろ側の配列に同じ処理を行う
        quick_sort(a, pivot + 1, right)      

# メインプログラム
# 再帰呼び出しの上限回数を1万回に設定する（デフォルトは1000回）
sys.setrecursionlimit(10000)

# 値を重複させずに1～1000の範囲で要素数1000個の乱数を生成する
rand_data = random.sample(range(1, 1001), k=1000)

# 挿入ソートをテストする
a = copy.copy(rand_data) # 乱数の配列のコピーを生成する
left = 0 # 配列の先頭の添字を左端に設定する
right = len(a) - 1 # 配列の末尾の添字を右端に設定する
time1 = time.perf_counter() # 処理前の時間を得る
insertion_sort(a, left, right) # ソートを行う
time2 = time.perf_counter() # 処理後の時間を得る
# テスト結果を表示する
print("***** 挿入ソート *****")
print(f"ソート結果 = {is_asc_sorted(a)}") # 昇順にソートされている
# ことを確認する
print(f"ソート時間 = {time2 - time1}秒") # ソートの処理時間を求める
print()

# シェルソートをテストする
a = copy.copy(rand_data) # 乱数の配列のコピーを生成する
left = 0 # 配列の先頭の添字を左端に設定する
right = len(a) - 1 # 配列の末尾の添字を右端に設定する
time1 = time.perf_counter() # 処理前の時間を得る
shell_sort(a, left, right) # ソートを行う
time2 = time.perf_counter() # 処理後の時間を得る
# テスト結果を表示する
print("***** シェルソート *****")
print(f"ソート結果 = {is_asc_sorted(a)}") # 昇順にソートされている
                                         # ことを確認する
print(f"ソート時間 = {time2 - time1}秒") # ソートの処理時間を求める
print()

# クイックソートをテストする
sys.setrecursionlimit(10000) # 再帰呼び出しの上限を1万回に設定する
a = copy.copy(rand_data) # 乱数の配列のコピーを生成する
left = 0 # 配列の先頭の添字を左端に設定する
right = len(a) - 1 # 配列の末尾の添字を右端に設定する
time1 = time.perf_counter() # 処理前の時間を得る
quick_sort(a, left, right) # ソートを行う
time2 = time.perf_counter() # 処理後の時間を得る
# テスト結果を表示する
print("***** クイックソート *****")
print(f"ソート結果 = {is_asc_sorted(a)}") # 昇順にソートされている
                                          # ことを確認する
print(f"ソート時間 = {time2 - time1}秒") # ソートの処理時間を求める
print()
