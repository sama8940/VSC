# ソート前の配列a
a = [5, 3, 9, 3, 5]

# バケツの役割をする配列b
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 配列aの要素の値を配列bの要素番号に対応付けてカウントする
for data in a:
    b[data] += 1

# 配列bからカウントした分、要素を繰り返し配列aに取り出す
a = []
for idx, data in enumerate(b, start=0):
    for _ in range(data):
        a.append(idx)

# ソート後の配列aの内容を表示する
print(a)
