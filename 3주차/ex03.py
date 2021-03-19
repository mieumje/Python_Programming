# 문자열 파싱
# find()함수와 index를 활용

data = '    From mieumje@eulj.ac.kr Fri Mar 19 13:46'

print(f"문자열 data : {data}")
t_data = data.strip()
print(
    f"문자열 data에서 공백을 지우고, 그 문자열이 From으로 시작하는가 ? : {t_data.startswith('From')}")
a = t_data.find('@')
print(f"t_data에서 '@'의 위치는 : {a}")
b = t_data.find(' ', a)
print(f"t_data에서 공백이 시작하는 위치는? (시작 인덱스는 a번째부터) : {b}")
host = t_data[a+1:b]
print(f"eulji.ac.kr을 추출한 결과 host의 출력 값은 : {host}\n")

str = 'X-DSPAM-Confidence:0.8475'
print("문제 : str = 'X-DSPAM-Confidence:0.8475'")
print("위 str 변수의 문자열에서 콜론 이후의 문자열을 가져와 이를 실수로 바꾸어라.")
f = str.find(':')
print(f"str에서 ':'의 위치는 : {f}")
print(f"str에서 ':'이후의 문자는: {str[f+1:]}")
result = float(str[f+1:])
print(f"str에서 ':'이후의 문자를 실수로 바꾸면 : {result}")
print(f"result의 type은 : {type(result)} \n")

words = "kbsTv"
print("kbsTv를 vTsbk로 출력하라")
print(f"words의 길이는 : {len(words)}")

print(words[-1], words[-2], words[-3], words[-4], words[-5], '\n')

n = len(words)-1
while n >= 0:
    print(words[n], end=" ")
    n -= 1
print("\n")

for i in range(1, len(words)+1):
    print(words[-i], end=" ")

c = 0
rev = ""
while c < len(words):
    rev = words[c] + rev
    c += 1
print(rev)
