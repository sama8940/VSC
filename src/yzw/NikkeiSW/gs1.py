# 新入社員の名前と希望部署リストを格納した辞書
employee_dict = {
"Aさん":["X部", "Y部", "Z部"],
"Bさん":["X部", "Y部", "Z部"],
"Cさん":["Y部", "Z部", "X部"]
}

# 3つの部署の名前と希望社員リストを格納した辞書
department_dict = {
"X部":["Cさん", "Aさん", "Bさん"],
"Y部":["Bさん", "Cさん", "Aさん"],
"Z部":["Aさん", "Bさん", "Cさん"]
}

# 安定マッチングを行う関数の定義
def stable_match(request_dict, accept_dict):
    # マッチングした結果の辞書
    match_dict = {}

    # マッチングする数を得る
    req_len = len(request_dict)

    # マッチングが完了するまで繰り返す
    while len(match_dict) < req_len:
        # 要求側の辞書から順番に1つずつ名前を取り出す
        for req_name in request_dict:
            # すでにマッチングされているなら、これ以降の処理をスキップする
            if req_name in match_dict.values():
                continue
            # 現時点で第1希望の名前を取り出し、希望のリストから削除する
            acc_name = request_dict[req_name].pop(0)
            # まだ受け入れ側にマッチングされているライバル候補がいない場合
            if acc_name not in match_dict:
                # 受け入れ側に要求側をマッチングする
                match_dict[acc_name] = req_name
            # すでに受け入れ側にマッチングされているライバル候補がいる場合
            else:
                # ライバル候補の名前を取り出す
                rival_name = match_dict[acc_name]
                # 受け入れ側の希望のリストにおいて、新たな候補の方が、
                # ライバル候補より順位が上の場合
                if accept_dict[acc_name].index(req_name) < \
                    accept_dict[acc_name].index(rival_name):
                    # 受け入れ側と要求側のマッチングを更新する
                    match_dict[acc_name] = req_name

    # マッチングした結果の辞書を返す
    return match_dict

# メインプログラム
if __name__ == '__main__':
    # 新入社員を要求側とし、部署を受け入れ側として、マッチングする
    match_dict = stable_match(employee_dict, department_dict)
    # マッチングした結果の辞書を表示する
    print(match_dict)