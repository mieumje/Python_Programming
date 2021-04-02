food = ['치즈', '바나나', '사과', '커피']
print(food[0])
print(food[1])
# 리스트 원소 위치를 인덱스로 가리킬 수 있으며
# 인덱스는 0부터 시작

val = [10, 20, 30, 40]
print(val)
print(val[0])
val[0] = 50
val[1] = -30
print(val)
# 원소의 순서를 바꾸거나, 다른 원소로 바꿀수 있다.
# 문자열은 X

f = 'hello'
print(f)
print(f[1])

""" f[1]='o'
print(f) """
# TypeError  TypeError: 'str' object does not support item assignment
# ==> '스트링형' 객체는 원소들에 대한 대입을 지원하지 않습니다.

val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 2
print(val[x])
# 수식 등으로 표현된 정수 표현식도 인덱스로 사용할 수 있다.

""" y = 11
print(val[y]) """
# 존재하지 않는 원소를 읽거나 쓰려고 하면 indexError가 발생

arr = [1, 2, 3, 4, 5]
print(arr[-1])
print(arr[-2])
print(arr[-3])
# 인덱스의 값이 음수면 리스트 끝부터 역방향으로 계산

brr = [11, 12, 13, 14]
print(brr)
x = 12
y = x in brr
print(y)
print(80 in brr)
# in 연산자를 사용해, 특정 원소가 리스트의 한 원소인지를 알아낼 수 있다
