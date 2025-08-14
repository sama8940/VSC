a = [1, 4, 5, 6]
b = [2, 3, 7, 8]

a_len = len(a)
b_len = len(b)

c = [None] * (a_len + b_len)

i = 0
j = 0
while i < a_len and j < b_len:
    if a[i] < b[j]:
        c[i + j] = a[i]
        i += 1
    else:
        c[i + j] = b[j]
        j += 1

while i < a_len:
    c[i + j] = a[i]
    i += 1

while j < b_len:
    c[i + j] = b[j]
    j += 1

print(c)
