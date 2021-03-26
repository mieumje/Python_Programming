# 오름차순이 몇 번 있는지?
""" 784321231235 1245289012= 3, 9875 = 0, 7678159 ,98751249871=2 9875=0 165516531834779 =5 """
a = 1245289012
b = str(a)
c = []
for i in b:
    c.append(i)
print(c)
print(len(c))

for i in range(0, len(c)-1):
    if c[i] <= c[i+1]:
        continue
    else:
        c[i] = 0

print(c)
cnt = 0
for i in range(0, len(c)-1):
    if int(c[i]) > int(c[i+1]):
        cnt += 1
if cnt != 0:
    print(cnt+1)
else:
    print(cnt)
