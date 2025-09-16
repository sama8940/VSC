# 数列
seq = []

# 数列の要素をキー入力する
while True:
    s = input("数列の要素-->")
    # 「Enter」キーだけが押された場合は入力終了
    if s == "":
        break
    # 数列に追加する
    seq.append(int(s))

# 数列の内容を表示する
print(seq)

# 数列の要素数を得る
seq_len = len(seq)

# 目的の数をキー入力する
val = int(input("目的の数-->"))

# selの要素をすべてNoneで初期化する
sel = [None] * seq_len

# 判定結果をFalse（できない）にしておく
judge = False

# 要素の数だけ1を並べた2進数+1の値を作る
bit_max = 2 ** seq_len

# bit全探索を行う
for pat in range(bit_max):
    # ビットが1になっている数を足す
    sum = 0
    mask = 1
    for i in range(seq_len):
        if pat & mask != 0:
            sum += seq[i]
            sel[i] = True
        else:
            sel[i] = False
        mask <<= 1
    # 目的の数ができたら判定結果をTrueにして繰り返しを抜ける
    if sum == val:
        judge = True
        break

# 判定結果を表示する
if judge:
    print("できる")
    print(sel)
else:
    print("できない")