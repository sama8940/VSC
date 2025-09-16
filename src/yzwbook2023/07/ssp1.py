# 数列
seq = [2, 4, 7]

# 数列の内容を表示する
print(seq)

# 目的の数をキー入力する
val = int(input("目的の数-->"))

# 数を選んだらTrueに、選ばなかったらFalseにする
sel = [None, None, None]

# 判定結果をFalse（できない）にしておく
judge = False

# 3重のfor文で全探索を行う
for i in range(2): # iを0と1に変化させるループ
    for j in range(2): # jを0と1に変化させるループ
        for k in range(2): # kを0と1に変化させるループ
            sum = 0 # 足し合わせた値をゼロにしておく
            if i == 0: # iが0ならseq[0]を選ばない
                sel[0] = False # sel[0]をFalse（選ばない）に設定する
            else: # iが1ならseq[0]を選ぶ
                sum += seq[0] # 足し合わせた値にseq[0]を追加する
                sel[0] = True # sel[0]をTrue（選ぶ）に設定する
            if j == 0: # jが0ならseq[1]を選ばない
                sel[1] = False # sel[1]をFalse（選ばない）に設定する
            else: # jが1ならseq[1]を選ぶ
                sum += seq[1] # 足し合わせた値にseq[1]を追加する
                sel[1] = True # sel[1]をTrue（選ぶ）に設定する
            if k == 0: # kが0ならseq[2]を選ばない
                sel[2] = False # sel[2]をFalse（選ばない）に設定する
            else: # kが1ならseq[2]を選ぶ
                sum += seq[2] # 足し合わせた値にseq[2]を追加する
                sel[2] = True # sel[2]をTrue（選ぶ）に設定する
            if sum == val: # 目的の数ができる場合
                judge = True # judgeをTrue（できる）に設定する
                break # kのループを抜ける
        if judge: # judgeがTrue（できる）なら
            break # ｊのループを抜ける        
    if judge: # judgeがTrue（できる）なら
        break # iのループを抜ける

# 判定結果を表示する
if judge:
    print("できる")
    print(sel)
else:
    print("できない")