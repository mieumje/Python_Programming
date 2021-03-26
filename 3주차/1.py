# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())

st = []
en = []
a = [[0 for i in range(n)] for i in range(2)]
for i in range(0, n):
    ST, EN = input().split('~')
    st.append(ST.rstrip())
    en.append(EN.lstrip())

print(st, en)

en_min = 23
st_max = 0

STH = []
STM = []
ETH = []
ETM = []
for i in st:
    a, b = i.split(":")
    STH.append(int(a))
    STM.append(int(b))
for i in en:
    a, b = i.split(":")
    ETH.append(int(a))
    ETM.append(int(b))

sc = 0
ec = 0
for i in range(0, n-1):
    if STH[i] == STH[i+1]:
        sc = i
    if ETH[i] == ETH[i+1]:
        ec = i

for i in range(0, n):
    if STH[i] > st_max:
        st_max = STH[i]
    if ETH[i] < en_min:
        en_min = ETH[i]

sm = 0
em = 0

if sc == 0 and ec == 0:
    print(f"{st_max}:00 ~ {en_min}:00")
elif sc != 0 and ec == 0:
    for i in range(0, n):
        if STM[i] > sm:
            sm = STM[i]
    print(f"{st_max}:{%dsm} ~ {en_min}:00")
elif ec != 0 and sc == 0:
    for i in range(0, n):
        if ETM[i] <= 59:
            em = ETM[i]
    print(f"{st_max}:00 ~ {en_min}:{%dem}")
elif ec != 0 and sc != 0:
    for i in range(0, n):
        if ETM[i] <= 59:
            em = ETM[i]
    for i in range(0, n):
        if STM[i] > sm:
            sm = STM[i]
    print(f"{st_max}:{sm} ~ {en_min}:{%dem}")
