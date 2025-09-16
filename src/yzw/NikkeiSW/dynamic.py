INF = float("inf") # 無限大
dp = [] # リストdp

# 動的計画法でコイン問題を解く関数の定義
def dynamic(coin_list, m, n):
    # 2次元リストdpを作成する
    global dp
    dp = [[None for _ in range(0, n + 1)] for _ in range(0, m + 1)]

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
            # そうでない場合
            else:
                # 1つ前の「c[i - 1]円」までを使ったときの
                # dp[i - 1][j]枚と
                # 現在の「c[i]円」までを使ったときの
                # dp[i][j - c[i]] + 1枚を
                # 比べて、小さい方をdp[i][j]に入れる
                if dp[i - 1][j] > dp[i][j - c[i]] + 1:
                    dp[i][j] = dp[i][j - c[i]] + 1
                else:
                    dp[i][j] = dp[i - 1][j]

    # DPテーブルの右下の枠に得られた正解を返す
    return dp[m][n]

# 2次元リストdpを表示する関数の定義
def show_dp():
    global dp
    for row in dp:
        for col in row:
            print(f"{col}\t", end="")
        print()

# メインプログラム
if __name__ == '__main__':
    # dynamic関数を呼び出し、戻り値を画面に表示する
    print(dynamic([1, 3, 4, 5], 4, 7))
    print()

    # show_dp関数を呼び出す
    show_dp()