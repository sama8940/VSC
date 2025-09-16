# ソートする配列
import random
a = list(range(1, 101))
random.shuffle(a)

# 処理回数
count = 0

# ソート対象の先頭の添字
top = 0

# ソート対象の末尾の添字
tail = len(a) - 1

# 間隔の初期サイズ
gap = len(a)

# 間隔を狭める割合
NARROW_RATE = 1.3

# 要素が交換されたことを示す変数swap_flagをFalseに設定する
swap_flag = False

# ソートが完了するまで繰り返す
while gap > 1 or swap_flag == False:
    # 間隔を狭める
    gap = int(gap / NARROW_RATE)

    # 間隔が0なら、間隔を1にする
    if gap == 0:
        gap = 1
    # 間隔が9または10なら、間隔を11にする
    elif gap == 9 or gap == 10:
        gap = 11

    swap_flag = True
    index = 0
    while index + gap <= tail:
        # 処理回数をカウントアップする
        count += 1
        # 間隔分だけ離れた要素を比較する
        if a[index] > a[index + gap]:
            # 小さい方が前になるように交換する
            temp = a[index]
            a[index] = a[index + gap]
            a[index + gap] = temp
            swap_flag = False
        # 比較する位置を1つ後ろに進める
        index += 1

# ソート後の配列の内容と処理回数を表示する
print(a)
print(count)