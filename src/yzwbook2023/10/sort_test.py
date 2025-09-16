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