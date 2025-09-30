# 投票
vote = [
    '山田太郎', '鈴木花子', '佐藤三郎', '鈴木花子',
    '鈴木花子', '佐藤三郎', '鈴木花子', '佐藤三郎',
    '鈴木花子', '鈴木花子', '山田太郎', '鈴木花子'
]

# 投票数
n = len(vote)

# 当選の候補者
candidate = ''

# 当選の候補者の支持者の残存数
survivor = 0

# ペアリングの繰り返し
for i in range(0, n):
    # 現時点の当選の候補者がいない場合
    if survivor == 0:
        # 現時点の当選の候補者を設定する
        candidate = vote[i]
        # 残存数を1にする
        survivor = 1
    # 現時点の当選の候補者と同じ場合
    elif candidate == vote[i]:
        # 残存者に1を加える
        survivor += 1
    # 現時点の候補者と異なる場合
    else:
        # 残存者から1を引く
        survivor -= 1

# 当選の候補者の得票数
count = 0

# カウンティングの繰り返し
if survivor != 0:
    for i in range(0, n):
        # 当選の候補者と同じ名前の場合
        if candidate == vote[i]:
            # 得票数に1を加える
            count += 1

# 過半数を取っているかどうかを確認する
if count > (n // 2):
    print(candidate + 'が過半数を取りました。')
else:
    print('過半数を取った人はいません。')
