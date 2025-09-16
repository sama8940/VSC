# 2つの数をキー入力する
a = int(input("A --> "))
b = int(input("B --> "))

# ここからはフローチャートと同様
l = a
s = b

while True:
    if l > s:
        l = l - s
    elif s > l:
        s = s - l
    else: # lとsが等しいなら繰り返しを抜ける
        break
print(a, b, l)