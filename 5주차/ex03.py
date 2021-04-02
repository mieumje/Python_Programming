val = [10, 20, 30, 40]
for x in val:
    print(x)
# 리스트를 순회하여 출력하기
# 단순 읽기 작업에서는 for~in~을 이용

print("")
for i in range(len(val)):
    print(val[i])
# 각 원소별로 특정지어 값을 쓰거나 변형하느 경우
# 인덱스를 직접 지정하는데 가장 흔한 방법은 range(), len()함수를 이용하는 것


print("")
print(len(val))
# len()함수로 리스트의 길이를 구할 수 있음

print("")
for i in range(0, 3):
    print(i)
# range(0,3)은 리스트[0,1,2]와 같다


print("")
empty = []
for x in empty:
    print("Yes")
print("No")
# 리스트가 비어있는 경우 for 루프 내로 진행하지 않는다
# 에러는 아님

print("")
data = [1, 2, 3, [12, 13], 4]
print('length : ', len(data))
for i in range(len(data)):
    print(data[i])
# 중첩된 리스트는 하나의 원소로 간주
