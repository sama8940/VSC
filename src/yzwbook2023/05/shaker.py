# ソートする配列
a = [1, 2, 3, 6, 5, 4, 7, 8, 9]

# 処理回数
count = 0

# ソート対象の先頭の添字
top = 0

# ソート対象の末尾の添字
tail = len(a) - 1

# ソート対象の要素が1個になるまで繰り返す
while top < tail:
    # 要素が交換されたことを示す変数swap_flagをFalseに設定する
    swap_flag = False
    # 比較位置
    index = top
    # 配列の先頭から末尾に向かって処理を繰り返す
    while index < tail:
        # 処理回数をカウントアップする
        count += 1
        # 隣り合った要素を比較する
        if a[index] > a[index + 1]:
            # 小さい方が前になるように交換する
            temp = a[index]
            a[index] = a[index + 1]
            a[index + 1] = temp
            # 最後に値が交換された位置を変数last_indexに設定する
            last_index = index
            # 値が交換されたのでswap_flagをTrueに設定する
            swap_flag = True
        # 比較する位置を1つ後ろに進める
        index += 1
    # 要素が交換されていなければ（ソートが完了していれば）処理を終了する
    if swap_flag == False:
        break
    # ソート対象の末尾を最後に値が交換された位置まで狭める
    tail = last_index
    # 要素が交換されたことを示す変数swap_flagをFalseに設定する
    swap_flag = False
    # 比較位置
    index = tail
    # 配列の末尾から先頭に向かって処理を繰り返す
    while index > top:
        # 処理回数をカウントアップする
        count += 1
        # 隣り合った要素を比較する
        if a[index - 1] > a[index]:
            # 小さい方が前になるように交換する
            temp = a[index]
            a[index] = a[index - 1]
            a[index - 1] = temp
            # 最後に値が交換された位置を変数last_indexに設定する
            last_index = index
            # 値が交換されたのでswap_flagをTrueに設定する
            swap_flag = True
        # 比較する位置を1つ前に進める
        index -= 1
    # 要素が交換されていなければ（ソートが完了していれば）処理を終了する
    if swap_flag == False:
        break
    # ソート対象の先頭を最後に値が交換された位置まで狭める
    top = last_index

# ソート後の配列の内容と処理回数を表示する
print(a)
print(count)