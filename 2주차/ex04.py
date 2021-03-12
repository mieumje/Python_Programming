f = 'banana'
count = 0
for c in f:
    count += 1
print(count)


a = 'apple'
print(f"apple의 길이 = {len(a)}")


words = 'It allows embedding Sage computations into any webpage'
w_counts = 0
for i in words:
    w_counts += 1
print(f"words의 문자열의 개수 = {w_counts}")
print(f"words의 문자열에서 12번째 문자는? '{words[11]}'")
print("맨 마지막 문자를 출력하시오 (단, len() 함수를 이용할 것")
print(f"맨 마지막 문자 = {words[len(words)-1]}")
