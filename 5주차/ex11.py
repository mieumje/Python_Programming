t = [1, 2, 3, 4, 5]
x = [8, 9]

t = t+x
print(t)

t.append(x)
print(t)

t = t+[x]
print(t)
# append(리스트) == + [리스트]

t.append([x])
print(t)
# append([]) => 리스트를 리스트로 추가
t = t+x
print(t)
