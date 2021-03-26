i = int(input('test cas : '))

print(i)

a = []


for x in range(0, i):
    str = input('Input : ')
    str1 = str.rstrip().lstrip()
    a.append(str1)


cnt = 0
for x in a:
    words = x.split(' ')
    print(f"'{a[cnt]}'의 단어의 갯수는 : ", end="")
    print(len(words))
    cnt += 1
