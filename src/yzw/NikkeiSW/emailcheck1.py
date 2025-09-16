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

    # 状態を意味する定数
    INIT = 0 # 初期状態
    LOCAL_NOTDOT = 1 # ローカル部のドット以外の文字
    LOCAL_DOT = 2 # ローカル部のドット
    ATMART = 3 # @
    DOMAIN_NOTDOT = 4 # ドメイン部のドット以外の文字
    DOMAIN_DOT = 5 # ドメイン部のドット
    OK = 6 # OK
    NG = 7 # NG
    
    # 初期状態を設定する
    state = INIT
    
    # 文字列から1文字ずつ取り出して状態を遷移させる
    for c in s:
        # 初期状態
        if state == INIT:
            if isalphanum(c):
                state = LOCAL_NOTDOT
            else:
                state = NG
                break
        # ローカル部のドット以外の文字
        elif state == LOCAL_NOTDOT:
            if isalphanum(c):
                state = LOCAL_NOTDOT
            elif isdot(c):
                state = LOCAL_DOT
            elif isatmark(c):
                state = ATMART
            else:
                state = NG
                break
        # ローカル部のドット
        elif state == LOCAL_DOT:
            if isalphanum(c):
                state = LOCAL_NOTDOT
            else:
                state = NG
                break
        # @
        elif state == ATMART:
            if isalphanum(c):
                state = DOMAIN_NOTDOT
            else:
                state = NG
                break
        # ドメイン部のドット以外の文字
        elif state == DOMAIN_NOTDOT:
            if isalphanum(c):
                state = DOMAIN_NOTDOT
            elif isdot(c):
                state = DOMAIN_DOT
            elif isend(c):
                state = OK
            else:
                state = NG
                break
        # ドメイン部のドット
        elif state == DOMAIN_DOT:
            if isalphanum(c):
                state = DOMAIN_NOTDOT
            else:
                state = NG
                break
        # OK
        elif state == OK:
            break
        # NG
        elif state == NG:
            break
        # その他
        else:
            state = NG

    # 判定結果を返す
    return state == OK

# メインプログラム
if __name__ == '__main__':
    s = input("文字列-->")
    if (isemail(s)):
        print("メールアドレスです。")
    else:
        print("メールアドレスではありません。")