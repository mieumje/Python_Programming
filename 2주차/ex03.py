f = 'banana'

print(f)

a1 = f[0]
a2 = f[2]
print(a1)
print(a2)
print(f[4])
print("\n")


f = 'banana'
print("한글자씩 출력하기 : for 문")
for m in f:
    print(m)
print("\n")

print("한글자씩 출력하기 : while 문")
k = 0
while k < 6:
    print(f[k])
    k = k+1
