# 貪欲法でコイン問題を解く関数の定義
def greedy(coin_list, n):
    # 硬貨のリストを大きい順にソートする
    coin_list.sort(reverse=True)
    # 硬貨の枚数を初期化する
    coin_num = 0
    # 硬貨のリストから大きい順に取り出す
    for c in coin_list:
        # 取り出した硬貨を使用する枚数を求めて集計する
        coin_num += n // c
        # 残りの金額を更新する
        n %= c
    # 硬貨の枚数を返す
    return coin_num

# メインプログラム
if __name__ == '__main__':
    # greedy関数を呼び出し、戻り値を画面に表示する
    print(greedy([10, 50, 100, 500], 870))