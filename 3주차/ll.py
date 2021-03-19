import math

n, k = input().split()
n = int(n)
k = int(k)

arr = []
l = list(map(int, input().split()))

result = 0
if n == k:
    result = 1
elif n-k == 1:
    result = 2
else:
    if (n-1) / (k-1) == 0.0:
        result = (n-1) / (k-1)
    else:
        result = math.ceil((n-1) / (k-1))


print(result)
