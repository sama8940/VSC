# 2つの数をキー入力する
a = int(input("A --> "))
b = int(input("B --> "))

# ここからはフローチャートと同様
l = a
s = b
while True:
    r = l % s
    if r == 0: # 剰余が0なら繰り返しを抜ける
        break
    l = s
    s = r
print(a, b, s)