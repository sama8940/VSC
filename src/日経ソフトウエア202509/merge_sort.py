# 配列cをマージソートする関数
def merge_sort(c):
    # 配列Cの要素数を求める
    c_len = len(c)

    # 配列cの要素数が2個以上なら分割と統合を行う
    if c_len >= 2:
        # 分割する前側の配列aと後側の配列bの要素数を求める
        a_len = c_len // 2
        b_len = c_len - a_len

        # 要素数を合わせたサイズで配列aと配列bを用意する
        a = [None] * a_len
        b = [None] * b_len

        #配列cの前側の要素を配列aに格納する
        i = 0
        while i < a_len:
            a[i] = c[i]
            i += 1
        
        j = 0
        #配列cの後側の要素を配列bに格納する
        while j < b_len:
            b[j] = c[a_len + j]
            j += 1

        print(f"c={c}を\na={a}とb={b}に分割しました。\n")

        # 分割した箇所の前側の配列aに対して同じ処理を行う(再帰呼び出し)
        merge_sort(a)
        # 分割した箇所の後側の配列bに対して同じ処理を行う(再帰呼び出し)
        merge_sort(b)
        # 配列aと配列bを統合して配列cに格納する
        merge(a, b, c)

        print(f"a={a}とb={b}を統合して\nc={c}に格納しました。\n")

# 配列aと配列bを統合して配列cに格納する関数
def merge(a, b, c):
    # 配列aと配列bの要素数を求める
    a_len = len(a)
    b_len = len(b)

    # 配列aと配列bの先頭の要素を比べて、小さい方の要素を配列cに格納する
    i = 0
    j = 0
    while i < a_len and j < b_len:
        if a[i] < b[j]:
            c[i + j] = a[i]
            i += 1
        else:
            c[i + j] = b[j]
            j += 1
    # 配列aの要素に要素が残っていれば、そのままの順で配列cに格納する
    while i < a_len:
        c[i + j] = a[i]
        i += 1

    # 配列bの要素に要素が残っていれば、そのままの順で配列cに格納する
    while j < b_len:
        c[i + j] = b[j]
        j += 1

# メイン関数
def main():
    c = [5, 4, 6, 1, 3, 8, 7, 2]
    merge_sort(c)
    print(c)

# プログラムの起動時にメイン関数を呼び出す
if __name__ == "__main__":
    main()