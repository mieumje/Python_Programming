# in 연산자
s = 'banana'
k = 'a' in s
print(k)

b = 'nan' in s
print(b)

if 'an' in s:
    print('있다\n')
else:
    print('없다\n')


# 문자열 비교 연산자, ==, >, <
print(s == 'banana')
if s == 'banana':
    print("s는 바나나 맞음")
else:
    print("s는 바나나 아님")
print(f"s > apple : {s > 'apple'}")
print(f"s < apple : {s < 'apple'}")
print(f"Hi > Hii : {'Hi' > 'Hii'}")
print(f"Hi > HI : {'Hi' > 'HI'}")
print(f"hi == HI : {'hi' == 'HI'}\n")
print("문자열의 대소비교 : ")
print("문자인 경우는 ASCII 숫자로 변환되서 맨앞 문자부터 비교한다.\n")

print(f"문자 H의 ASCII 코드 값 : {ord('H')}")
print(f"ASCII 코드 값 72 : {chr(72)}")


x = 'H'

print("chr(ord('H')+ord('a')-ord('A'))")
print(f"문자 {x}의 소문자 =>", end=" ")
print(chr(ord('H')+ord('a')-ord('A')))
