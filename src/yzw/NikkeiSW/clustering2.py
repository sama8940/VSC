# モジュールをインポートする
import matplotlib.pyplot as plt # グラフを描画するモジュール
import random # 乱数の生成や選択を行うモジュール
import copy # オブジェクトをコピーするモジュール

# グループ化の対象となるデータ
student_num = 100 # 学生の人数
japanese_score = [] # 国語の得点（グラフのx軸）
math_score = [] # 数学の得点（グラフのy軸）

# 中心点
k = 4 # 中心点の数（クラスタの数）
japanese_center = [] # 国語の中心点
math_center = [] # 数学の中心点
center_fixed = False # 中心点が変化していないことを示すフラグ（処理の終了の判断に使う）

# グループを識別する色（0=赤、1=緑、2=青、3=橙、4=紫、5=茶、6=水、7=桃色、8=黄、9=灰、10=黒）
group_color = ["red", "green", "blue", "orange", "purple", "brown", "aqua", "pink", "yellow", "gray", "black"]
# 学生をグループ分けした結果（初期値の-1はグループ分けされていないことを意味し、散布図に黒で表示される）
group_idx = [-1] * student_num

# ウインドウがクリックされた回数（奇数のときはグループ分け、偶数のときは中心点の移動を行う）
press_count = 0

# 100人の学生の架空の得点データを作成する関数の定義
def make_100data():
    # グローバル宣言
    global japanese_score, math_score
    # 乱数の種を固定する（同じデータで、中心点を変えて、結果を比べるため）
    random.seed(60)
    # 国語の平均80点標準偏差5で、数学の平均35点標準偏差5の学生が30人
    for _ in range(30):
        japanese_score.append(int(random.normalvariate(80, 5)))
        math_score.append(int(random.normalvariate(35, 5)))
    # 国語の平均45点標準偏差5で、数学の平均85点標準偏差5の学生が30人
    for _ in range(30):
        japanese_score.append(int(random.normalvariate(45, 5)))
        math_score.append(int(random.normalvariate(85, 5)))
    # 国語の平均80点標準偏差5で、数学の平均75点標準偏差5の学生が20人
    for _ in range(20):
        japanese_score.append(int(random.normalvariate(80, 5)))
        math_score.append(int(random.normalvariate(75, 5)))
    # 国語の平均35点標準偏差5で、数学の平均25点標準偏差5の学生が20人
    for _ in range(20):
        japanese_score.append(int(random.normalvariate(35, 5)))
        math_score.append(int(random.normalvariate(25, 5)))

# 中心点の初期位置を設定する関数の定義
def init_center():
    # グローバル宣言
    global japanese_score, math_score, student_num, japanese_center, math_center, k
    # 乱数の種を変える
    random.seed()
    # 0 ～ 99のインデックスのリストを作成する
    idx_list = list(range(student_num))
    # ランダムに選んだデータを1つ目の中心点に設定する
    rnd_idx = random.choice(idx_list)
    japanese_center.append(japanese_score[rnd_idx])
    math_center.append(math_score[rnd_idx])
    # 設定した中心点の数を1にする
    center_num = 1
    # 残りの中心点を設定する
    while center_num < k:
        # それぞれのデータで、最も近い中心点までの距離の2乗を格納するリスト
        dist_square = []
        # それぞれのデータで、最も近い中心点までの距離の2乗を求める
        for i in range(student_num):
            # それぞれの中心点までの距離の2乗を格納するリスト
            dist = []
            for j in range(center_num):
                dist.append((japanese_score[i] - japanese_center[j])**2 +
                (math_score[i] - math_center[j])**2)
            # 最も近い中心点までの距離の2乗を記録する
            dist_square.append(min(dist)) 
        # 最も近い中心点までの距離の2乗を選択される重みとして、次の中心点を設定する
        next_idx = random.choices(idx_list, k=1, weights=dist_square)[0]
        japanese_center.append(japanese_score[next_idx])
        math_center.append(math_score[next_idx])
        # 設定した中心点の数に1を加える
        center_num += 1

# 現在のデータを散布図に設定する関数の定義
def set_scatter(description):
    # グローバル宣言
    global japanese_score, math_score, student_num, japanese_center,\
    math_center, k, group_color
    # 散布図の外観を設定する
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.title(description, fontname="MS Gothic")
    plt.xlabel("国語のテストの得点", fontname="MS Gothic")
    plt.ylabel("数学のテストの得点", fontname="MS Gothic")
    plt.grid(True)
    # 中心点を散布図に設定する
    for i in range(k):
        plt.scatter(japanese_center[i], math_center[i], s=300,
        c=group_color[i], marker="*", alpha=0.5)
    # 100人の学生の得点を散布図に設定する
    for i in range(student_num):
        plt.scatter(japanese_score[i], math_score[i],
        c=group_color[group_idx[i]], marker=".")

# 最も近い中心点にグループ分けする関数の定義
def grouping():
    # グローバル宣言
    global japanese_score, math_score, student_num, japanese_center,\
    math_center, k, group_idx
    # 100人の学生のデータをグループ分けする
    for i in range(student_num):
        # 中心点までの距離を求める（リストにする）
        dist = []
        for j in range(k):
            dist.append((japanese_score[i] - japanese_center[j])**2 +
            (math_score[i] - math_center[j])**2)
        # 最も近いグループを設定する
        group_idx[i] = dist.index(min(dist))

# ぞれぞれのグループの平均位置に中心点を移動する関数の定義
def move_center():
    # グローバル宣言
    global japanese_score, math_score, student_num, japanese_center,\
    math_center, k, group_idx, center_fixed
    # 現在の中心点の位置を保存する
    prev_japanese_center = copy.copy(japanese_center)
    prev_math_center = copy.copy(math_center)
    # グループごとに、位置の合計値およびデータ数を集計するリストを用意する
    japanese_sum = [0] * k
    math_sum = [0] * k
    group_data_num = [0] * k
    # 位置の合計値を求める
    for i in range(student_num):
        japanese_sum[group_idx[i]] += japanese_score[i]
        math_sum[group_idx[i]] += math_score[i]
        group_data_num[group_idx[i]] += 1
    # 位置の合計値／データ数＝平均位置を求めて、そこに中心点を移動する
    for i in range(k):
        # 位置の合計値／データ数
        if group_data_num[i] != 0:
            japanese_center[i] = japanese_sum[i] // group_data_num[i]
            math_center[i] = math_sum[i] // group_data_num[i]
    # 中心点が変化したかどうかをチェックする
    center_fixed = prev_japanese_center == \
    japanese_center and prev_math_center == math_center

# マウスがクリックされたときに呼び出される関数の定義
def button_press(event):
    # グローバル宣言
    global center_fixed, press_count
    # 中心点が変化していないなら処理を行わない
    if center_fixed:
        plt.title(f"({press_count})データのグループ分けが完了しました！ \n\
        （中心点が変化していません）", fontname="MS Gothic")
        plt.draw()
        return
    # クリックされた回数に1を加える
    press_count += 1
    # 現在の散布図を消去する
    plt.clf()
    # クリックされた回数が奇数のときはグループ分けを行う
    if press_count % 2 == 1:
        grouping()
        set_scatter(f"({press_count})最も近い中心点にデータをグループ分けしました。\n\
        （クリックすると先に進みます）")
    # クリックされた回数が偶数のときは中心点の移動を行う
    else:
        move_center()
        set_scatter(f"({press_count})グループの平均位置に中心点を移動しました。\n\
        （クリックすると先に進みます）")
    # 新たな散布図を描画する
    plt.draw()

# メインプログラム
if __name__ == '__main__':
    # 100人の学生の架空の得点データを作成する
    make_100data()
    # 中心点の初期位置を設定する
    init_center()
    # 初期状態のデータを散布図に設定する
    set_scatter(f"({press_count})初期状態です。\n\
    （クリックすると先に進みます）")
    # 散布図sがクリックされたときに呼び出される関数を設定する
    plt.connect("button_press_event", button_press)
    # ウインドウを表示する
    plt.show()