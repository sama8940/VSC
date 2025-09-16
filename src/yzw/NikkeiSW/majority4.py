# 投票
vote = [
"山田太郎", "鈴木花子", "佐藤三郎", "鈴木花子",
"鈴木花子", "佐藤三郎", "鈴木花子", "佐藤三郎",
"鈴木花子", "鈴木花子", "山田太郎", "鈴木花子"
]

# 黒板の役をする辞書を作成する
blackboard = dict()

# 票を1票ずつ取り出して集計を行う繰り返し
for v in vote:
    # キーが辞書にない場合（黒板に名前がない場合）
    if v not in blackboard.keys():
        # 辞書にキーを登録しバリューを1にする（黒板に名前を書き票数を1にする）
        blackboard[v] = 1
    # キーが辞書にある場合（黒板に名前がある場合）
    else:
        # キーに対応するバリューに1を加える（名前に対応する票数に1を加える）
        blackboard[v] += 1
    # 現在の辞書の内容（黒板の内容）を表示する
    print(blackboard)

# 集計後の辞書のバリューの最大値を求める
max_value = max(blackboard.values())

# 辞書の最大値が過半数なら当選者がいる
if max_value > (len(vote) // 2):
    # 過半数を取ったキーを見つけて表示する
    for key, value in blackboard.items():
        if (value == max_value):
            print(key + "が過半数を取りました。")
            break
# そうでなければ当選者はいない
else:
    print("過半数を取った人はいません。")