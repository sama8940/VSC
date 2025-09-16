# 2つの数をキー入力する
a = int(input("A --> "))
b = int(input("B --> "))

# 最大公約数を求める
l = a
s = b
while True:
    r = l % s
    if r == 0: # 剰余が0なら繰り返しを抜ける
        break
    l = s
    s = r
gcd = s

# 最小公倍数を求める
lcm = a * b // gcd

# 2つの数と最小公倍数を表示する
print(a, b, lcm)