# 数列
seq = []

# 数を選んだらTrueに、選ばなかったらFalseにする
sel = []

# 関数が呼び出された回数
counter = 0

# メモ（memo[num][val]にssp_func(num, val)の戻り値をメモする）
memo = [[None] * 100] * 100

# 数列の先頭からnum個まででvalが作れればTrue、作れなければFalseを返す関数
def ssp_func(num, val):
    # グローバル宣言
    global seq, sel, counter, memo

    # 関数が呼び出されたことを表示する
    print(f"ssp_func({num}, {val})が呼び出されました。")
    
    # 関数が呼び出された回数をカウントする
    counter += 1
    
    # numが0の場合（どの要素も使わない場合）
    if num == 0:
        if val == 0: # valが0なら「できる」と判定する
            return True # 判定結果としてTrue（できる）を返す
        else: # そうでないなら「できない」と判定する
            return False # 判定結果としてFalse（できない）を返す
        
    # メモがある場合
    if memo[num][val] is not None:
        return memo[num][val] # 再帰呼び出しをせずにメモの内容を返す
    
    # 末尾のseq[num - 1]を選ばない場合
    # 先頭からnum-1個まででvalができるなら「できる」
    if ssp_func(num - 1, val): # 再帰呼び出し
        sel[num - 1] = False # 要素の位置にFalse（選ばない）を設定する
        memo[num][val] = True # 戻り値をメモする
        return True
    # 末尾のseq[num - 1]を選ぶ場合
    # 先頭からnum-1個まででval - seq[num-1]ができるなら「できる」
    elif ssp_func(num - 1, val - seq[num - 1]): # 再帰呼び出し
        sel[num - 1] = True # 要素の位置にTrue（選ぶ）を設定する
        memo[num][val] = True # 戻り値をメモする
        return True # 判定結果としてTrue（できる）を返す
    
    # 上記のどれにも該当しないなら「できない」
    memo[num][val] = False # 戻り値をメモする
    return False # 判定結果としてFalse（できない）を返す

# メインプログラム
if __name__ == '__main__':
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
    
    # selの要素をすべてNoneで初期化する
    sel = [None] * len(seq)
    
    # 目的の数をキー入力する
    val = int(input("目的の数-->"))

    # 判定結果を表示する
    if ssp_func(len(seq), val):
        print("できる")
        print(sel)
    else:
        print("できない")

    # 関数が呼び出された回数を表示する
    print(f"{counter}回")