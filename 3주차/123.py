# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
a = str(input())


b = []
for i in range(0, n):
    b.append(int(a[i]))

z_count = 0
for i in range(0, n):
    if b[i] == 0:
        z_count += 1

if z_count == 0 and n > 3:
    print(n)
elif z_count == 0 and n == 3:
    print(n-1)
elif z_count > 0:
    c = []
    c = a.split('0')
    result = 0
    max = 0

    for i in range(0, len(c)):
        if len(c[i]) < 3:
            result = 1
            """ if max != 0:
                max = max + result """
        elif len(c[i]) >= 3:
            max = max + len(c[i])
    if max != 0:
        print(max)
    else:
        print(result)
