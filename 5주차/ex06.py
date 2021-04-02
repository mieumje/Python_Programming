# pop()
t = ['a', 'b', 'c']
print(t)
x = t.pop(1)
print(t)
print(x)
# 삭제하고자 하는 원소의 인덱스를 알고 있을 경우 사용
# 삭제된 원소도 알 수 있음


print("")
# del 연산자
t = ['a', 'b', 'c']
print(t)
del t[1]
print(t)

print("")
# remove()
t = ['a', 'b', 'c']
print(t)
t.remove('b')
print(t)
# 삭제하고자 하는 원소의 인덱스를 모르고, 원소의 값을 알 경우 사용
# 다른 대부분의 리스트 메소드와 마찬가지로 remove() 메소드의 반환값은 none

print("")
# del 연산자와, 슬라이스
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t)
del t[1:5]
print(t)
