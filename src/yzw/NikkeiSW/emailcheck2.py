# 大小の英字、数字ならTrueを返す関数
def isalphanum(c):
    return "0" <= c <= "9" or "A" <= c <= "Z" or \
    "a" <= c <= "z"

# ドットならTrueを返す関数
def isdot(c):
    return c == "."

# @ならTrueを返す関数
def isatmark(c):
    return c == "@"

# 末尾を意味する$ならTrueを返す関数
def isend(c):
    return c == "$"

# 文字列がメールアドレスの形式ならTrueを返す関数
def isemail(s):
    # 文字列に末尾を意味する$を付加する
    s += "$"

    # リストで状態遷移表を表現する
    table = [
    [1, 7, 7, 7, 7],
    [1, 2, 3, 7, 7] ,
    [1, 7, 7, 7, 7],
    [4, 7, 7, 7, 7],
    [4, 5, 7, 7, 6],
    [4, 7, 7, 7, 7],
    [8, 8, 8, 8, 8],
    [8, 8, 8, 8, 8]
    ]

    # 初期状態を状態遷移表の列に対応させて設定する
    state = 0

    # 文字列から1文字ずつ取り出して状態を遷移させる
    for c in s:
        # 文字の種類を状態遷移表の列の添字に対応させる
        if isalphanum(c):
            col = 0
        elif isdot(c):
            col = 1
        elif isatmark(c):
            col = 2
        elif isend(c):
            col = 4
        else:
            col = 3

        # 状態を遷移させる
        state = table[state][col]
        
        # OKまたはNGなら終了する
        if state == 6 or state == 7:
            break
    
    # 判定結果を返す
    return state == 6

# メインプログラム
if __name__ == '__main__':
    s = input("文字列-->")
    if (isemail(s)):
        print("メールアドレスです。")
    else:
        print("メールアドレスではありません。")