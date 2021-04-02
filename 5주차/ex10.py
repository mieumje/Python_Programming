# 리스트 인수

# 함수에 대한 리스트 매개변수 전달

def del_head(t):
    del t[0]


val = [1, 2, 3]
print(val)
del_head(val)
print(val)

""" 리스트를 전달할 경우, 참조(reference)를 전달하는 것이므로, 호출 후, 되돌아올 경우, 호출한 곳에서도 변형이 반영된다. """

print("")
# 리스트 수정, 생성의 구분
# append() : 리스트 수정
# + 연산자 : 리스트 생성
t1 = [1, 2]
t2 = t1.append(3)
print(t1)   # => [1,2,3]
print(t2)   # => None

t3 = [1, 2]
t4 = t3+[3]
print(t3)   # => [1,2]
print(t4)   # => [1,2,3]
print(t1 is t4)  # => False
print(t1 == t4)  # => True

print("")
# 리스트 변형


def delete_head(t):
    t = t[1:]


val = [1, 2, 3, 4, 5]
delete_head(val)
print(val)    # => [1,2,3,4,5]
# 어떠한 리스트 변형도 없음

# 다음으로 진행하면 첫번째 원소를 제거할 수 있음


def d_head(t):
    return t[1:]


val = [1, 2, 3, 4, 5]
rest = d_head(val)
print(rest)   # => [2,3,4,5]
# return 자리에 t[:] = t[1:]로 수정해도 같은 결과
