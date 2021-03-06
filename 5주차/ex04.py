# + 연산자
a = [1, 2, 3]
b = [4, 5]
c = a+b
print(c)


print("")
# * 연산자
# 주어진 수만큼 리스트를 반복
a = [4, 5]
b = a * 3
c = b * 2
print(b)
print(c)

print("")
# 슬라이스 연산자
# a:b > a번 인덱스부터 b-1까지의 인덱스
# 3:7 > 3번 인덱스부터 6까지의 인덱스
# 3,4,5,6
# t[1:3] > t의 리스트에서 t[1],t[2],t[3]를 잘라냄
# t[:3] > t의 리스트에서 첫 원소에서 2번 인덱스까지 잘라냄
# t[3:] > t의 리스트에서 3번째 원소부터 마지막까지 잘라냄
# t[:] > t의 모든 원소

t = ['가', '나', '다', '라', '마', '바', '사']
print(t)
print(t[1:3])
print(t[:3])
print(t[3:])
print(t[:])

print("")
# 슬라이스 연산자를 이용한 대입문
# 슬라이스 연산자를 대입문 왼쪽에 두면 여러개의 원소를 업데이트 가능
print(t)
t[1:3] = ['a', 'b']
print(t)
