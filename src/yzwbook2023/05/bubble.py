# ソートする配列
a = [78, 34, 56, 12]

# 処理回数
count = 0

# ソート対象の末尾の添字
tail = len(a) - 1

# ソート対象の要素が1個になるまで繰り返す
while tail > 0:
    # 隣り合った要素を比較する位置の添字
    index = 0
    # ソート対象の末尾まで繰り返す
    while index < tail:
        # 処理回数をカウントアップする
        count += 1
        # 隣り合った要素を比較する
        if a[index] > a[index + 1]:
            # 小さい方が前になるように交換する
            temp = a[index]
            a[index] = a[index + 1]
            a[index + 1] = temp
        # 比較する位置を1つ後ろに進める
        index += 1
    # ソート対象を1つ前に狭める
    tail -= 1
# ソート後の配列の内容と処理回数を表示する
print(a)
print(count)