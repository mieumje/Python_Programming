n = int(input())
a = str(input())


b = []
for i in range(0, n):
    b.append(int(a[i]))


c = [0 for i in range(n)]


for i in range(0, n):
    if i < 2:
        c[i] = b[i]
    if i >= 2:
        c[i] = c[i-1] + c[i-2]
    if b[i] == 0:
        c[i] = 0
print(c)
max = 0
for i in c:
    if i >= max:
        max = i
print(max)
