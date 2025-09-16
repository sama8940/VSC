import sys # sys.exit()を使うためにインポートする

# 経路の情報[元の地点の添字, 先の地点の添字, 重み]を設定する
edge = [
[0 , 1, 1], # A地点からB地点への経路[0]の重みは1kWh
[1 , 3, 3], # B地点からD地点への経路[1]の重みは3kWh
[2 , 3, 4], # C地点からD地点への経路[2]の重みは4kWh
[2 , 1, -2], # C地点からB地点への経路[3]の重みは-2kWh
[0 , 2, 2] # A地点からC地点への経路[4]の重みは2kWh
]

# 出発地点の添字
start_idx = 0 # A地点

# 目的地点の添字
goal_idx = 3 # D地点

# 無限大をINFとする
INF = float("inf")

# 【手順1】各地点の情報[出発地点から各地点までの重み, 1つ前の地点]を初期化する
vertex = [
[INF, None], # [0]A地点
[INF, None], # [1]B地点
[INF, None], # [2]C地点
[INF, None] # [3]D地点
]

# 【手順2】出発地点の重みを0に更新する
vertex[0][0] = 0

# 地点の数を求める
vertex_num = len(vertex)

# 【手順3】地点の数 - 1回だけ、【手順4】繰り返す
for _ in range(vertex_num - 1):
    # 【手順4】それぞれの地点の重みを緩める
    for e in edge:
        sorc = e[0] # 経路の元の地点の添字
        dist = e[1] # 経路の先の地点の添字
        weight = e[2] # 経路の重み
        if vertex[sorc][0] + weight < vertex[dist][0]:
            vertex[dist][0] = vertex[sorc][0] + weight
            vertex[dist][1] = sorc

# 【手順5】もう1回だけ【手順4】を行い、更新があれば負閉路があるので終了する
for e in edge:
    sorc = e[0] # 経路の元の地点の添字
    dist = e[1] # 経路の先の地点の添字
    weight = e[2] # 経路の重み
    if vertex[sorc][0] + weight < vertex[dist][0]:
        print("負閉路があります！ ")
        sys.exit()

# 出発地点から目的地点までの最短経路を得る
route = []
idx = goal_idx
while idx != start_idx:
    route.append(idx)
    idx = vertex[idx][1]
route.append(start_idx)
route.reverse()

# 【手順6】最短経路を表示して終了する
print(f"最短経路の重み：{vertex[goal_idx][0]}")
print(f"最短経路：{route}")