# 리스트 메소드

# append()
t = ['a', 'b']
t.append('c')
print(t)
# 리스트에 새로운 원소를 추가


print("")
# extend()
t = ['a', 'b', 'c']
print(t)
t1 = ['x1', 'x2']
t.extend(t1)
print(t)
# append는 원소 추가, extend는 리스트 추가

print("")
# sort()
t = ['e', 'a', 'b', 'c', 'd']
print(t)
t.sort()
print(t)
# 원소를 오름차순으로 정렬

t = ['e', 'a', 'b', 'c', 'd']
print(t)
t1 = t.sort()
print(t)
print(t1)
# 리스트는 return값이 없다, 리스트를 수정할 뿐 return 값은 none
