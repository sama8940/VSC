INF = float("inf") # 無限大
dp = [] # リストdp
dp2 = [] # 【改造】リストdp2

# 動的計画法でコイン問題を解く関数の定義
def dynamic(coin_list, m, n):
    # 2次元リストdpを作成する
    global dp
    dp = [[None for _ in range(0, n + 1)] for _ in range(0, m + 1)]

    # 【改造】2次元リストdp2を作成する
    global dp2
    dp2 = [[None for _ in range(0, n + 1)] for _ in range(0, m + 1)]

    # 硬貨のリストの先頭に0円を追加したリストを作成する
    c = [0] + coin_list
    
    # 2次元リストdpを初期化する
    for i in range(0, m + 1):
        dp[i][0] = 0
    for j in range(1, n + 1):
        dp[0][j] = INF
    
    # 2次元リストdpを埋める
    # iを1～mに変化させて繰り返す
    for i in range(1, m + 1):
        # jを1～nに変化させて繰り返す
        for j in range(1, n + 1):
            # 現在の硬貨「c[i]円」が現在の支払い金額「j円」より大きい場合
            if c[i] > j:
                # 1つ前の「c[i - 1]円」までを使ったときの
                # dp[i - 1][j]枚を
                # dp[i][j]に入れる
                dp[i][j] = dp[i - 1][j]
                dp2[i][j] = False # 【改造】
            # そうでない場合
            else:
                # 1つ前の「c[i - 1]円」までを使ったときの
                # dp[i - 1][j]枚と
                # 現在の「c[i]円」までを使ったときの
                # dp[i][j - c[i]] + 1枚を
                # 比べて、小さい方をdp[i][j]に入れる
                if dp[i - 1][j] > dp[i][j - c[i]] + 1:
                    dp[i][j] = dp[i][j - c[i]] + 1
                    dp2[i][j] = True # 【改造】
                else:
                    dp[i][j] = dp[i - 1][j]
                    dp2[i][j] = False # 【改造】

    # 【改造】使った硬貨の枚数を求める
    coin_num_list = [0] * m # 硬貨の枚数を格納するリストを初期化する
    i = m # 2次元リストdp2の右下の行
    j = n # 2次元リストdp2の右下の列
    rem = n # 残金（枠をたどって使った硬貨の額面分だけ減らしていく）
    while rem > 0:
        # その枠の枚数が、当該行の硬貨を使って決定されている場合
        if dp2[i][j]:
            # 使った硬貨の枚数をカウントアップする
            coin_num_list[i - 1] += 1
            # 残金を更新する
            rem -= c[i]
            # 使用した硬貨の額面分だけ前へたどる
            j -= c[i]
        else:
            # 1つ上の枠へたどる
            i -= 1

    # 【改造】DPテーブルの右下の枠に得られた正解と、使った硬貨の枚数を返す
    return dp[m][n], coin_num_list

# 2次元リストdpを表示する関数の定義
def show_dp():
    global dp
    for row in dp:
        for col in row:
            print(f"{col}\t", end="")
        print()

# 【改造】2次元リストdp2を表示する関数の定義
def show_dp2():
    global dp2
    for row in dp2:
        for col in row:
            print(f"{col}\t", end="")
        print()

# メインプログラム
if __name__ == '__main__':
    # dynamic関数を呼び出し、戻り値を画面に表示する
    print(dynamic([1, 5, 10, 40, 50], 5, 87))