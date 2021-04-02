# 객체와 값
# 객체

# is 연산자 : 두 변수가 동일 객체를 가리키는지 확인하여 True, False로 결과값을 냄
a1 = 'banana'
b1 = 'banana'
print(a1 is b1)

a1 = b1
print(a1 is b1)

a2 = [1, 2, 3]
b2 = [1, 2, 3]
print(a2 is b2)
print(a2 == b2)

a3 = [1, 2, 3]
b3 = a3
print(a3 is b3)

# 문자열의 경우, 동일한 문자열 리터럴은 하나의 객체만 생성하고
# a1, b1이 이를 가리키는 것이므로 True

# 리스트의 경우 각각의 객체를 만들고 각각의 객체를 참조하고 있으므로
# a2, b2는 다른 값을 가짐

""" is 는 변수가 동일한 객체를 가리키면 True
== 는 변수가 같은 값을 가지면 True """
