# 最短経路を求める関数
def shortest_route(route_map, start, goal):
    # 無限大を得る
    INF = float("inf")

    # 駅数を求める
    station_num = len(route_map)
    
    # 駅数分の要素を持つ辞書のリストを作成し、すべての駅の情報を初期化する
    station = []
    for n in range(station_num):
        station.append({"time":INF, "prev":-1, "fixed":False})
    
    # 発駅の「時間」に0を設定する
    station[start]["time"] = 0
    
    # 経路探索処理
    while True:
        # リストの先頭からチェックして、未確定の駅の番号をidxに得る
        all_fixed = True
        for idx in range(station_num):
            if station[idx]["fixed"] == False:
                all_fixed = False
                break
            
        # すべての駅が確定していれば、経路探索処理を終了する
        if all_fixed:
            break
        
        120 # 未確定の駅の中で、最も時間が小さい駅の番号をshortest_idxに得る
        shortest_idx = idx
        for idx in range(shortest_idx + 1, station_num):
            if station[idx]["fixed"] == False and \
                station[idx]["time"] < station[shortest_idx]["time"]:
                shortest_idx = idx

        # 最も時間が小さい駅を確定にする
        station[shortest_idx]["fixed"] = True
        
        # リストのすべての要素をチェックして、
        for idx in range(station_num):
            # 新たに確定した駅に直接つながっていて、かつ、未確定な駅で
            if route_map[shortest_idx][idx] > 0 and \
                station[idx]["fixed"] == False:
                # 新たに確定した駅からその駅までの時間を求めて
                new_time = station[shortest_idx]["time"] \
                            + route_map[shortest_idx][idx]
                # 求めた時間が、それまでの時間より短ければ
                if new_time < station[idx]["time"]:
                    # その駅の時間を、求めた時間で更新して
                    station[idx]["time"] = new_time
                    # その駅の直前に、新たに確定した駅の番号を設定する
                    station[idx]["prev"] = shortest_idx

    # 着駅から発駅まで直前をたどって最短経路のリストを作成する
    answer_route = []
    idx = goal
    while idx != start:
        answer_route.append(idx)
        idx = station[idx]["prev"]
    answer_route.append(start)

    # リストの要素を逆順にして、発駅から着駅までの最短経路のリストにする
    answer_route.reverse()
    
    # 最短経路のリストと時間を戻り値として返す
    return answer_route, station[goal]["time"]

# メインプログラム
if __name__ == '__main__':
    # 駅名
    station_name = ["0駅", "1駅", "2駅", "3駅", "4駅", "5駅"]

    # 路線図（同一の駅は0、直接つながっていない駅は-1）
    route_map = [
    [ 0, 11, 9, 3, -1, -1], # 0駅から他の駅までの時間
    [ 10, 0, 3, -1, 3, -1], # 1駅から他の駅までの時間
    [ 10, 2, 0, 4, 6, -1], # 2駅から他の駅までの時間
    [ 4, -1, 5, 0, -1, 14], # 3駅から他の駅までの時間
    [ -1, 2, 5, -1, 0, 2], # 4駅から他の駅までの時間
    [ -1, -1, -1, 15, 3, 0] # 5駅から他の駅までの時間
    ]

    # 0駅から5駅までの最短経路と時間を求める
    start = 0
    goal = 5
    sr, time = shortest_route(route_map, start, goal)

    # 最短経路と時間を表示する
    for idx in sr:
        print(station_name[idx], end="")
        if idx != goal:
            print("→", end="")
        else:
            print(f"（{time}分）")