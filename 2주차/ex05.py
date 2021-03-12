print("문제 1 : words에서 while문을 이용하여 문자를 뒤에서부터 앞으로 한 문자씩 차례로 출력하기")

words = "It allows embedding Sage Computations into any Webpage"

n = 1
while n <= len(words):
    if n < len(words):
        if words[-n] == " ":
            print("\n")
        else:
            print(words[-n], end=',')
    else:
        if words[-n] == " ":
            print("\n")
        else:
            print(words[-n])
    n += 1

print("문제 2 : words에서 for문과 if문을 이용하고, 대문자만을 출력한다")
for i in words:
    if i == words[0]:
        print("대문자인 문자열 = ", end='')
    if i >= 'A' and i <= 'Z':
        print(i, end=' ')
