# 입력 받은 시간에서 겹치는 시간 찾기

n = int(input())

st = []
et = []

for i in range(0, n):
    ST, ET = input().split('~')
    st.append(ST)
    et.append(ET)

print(st)
print(et)

STH = []
ETH = []

for i in st:
    a, b = i.split(':')
    STH.append(a)

for i in et:
    a, b = i.split(':')
    ETH.append(a)

print(STH, ETH)

s_max = 0
e_min = 23

for i in STH:
    if int(i) > s_max:
        s_max = int(i)
for i in ETH:
    if int(i) < e_min:
        e_min = int(i)
print(f"{s_max}:00~{e_min}:00")
