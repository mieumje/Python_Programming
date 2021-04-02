# list() 내장함수
# 문자열을 문자 단위로 분해해 리스트로 만들기 위해서는
# list() 내장함수를 이용하면 된다
s = 'python'
m = ['p', 'y', 't', 'h', 'o', 'n']
print(s)
print(m)
t = list(s)
print(t)

# split()
# 문자열을 단어 단위로 분해해 리스트로 만들기 위해서는
# split() 메소드를 이요하면 된다

s = "We are student"
print(s)
t = s.split()
print(t)
print(t[2])

# join() 메소드
# 문자열의 리스트를 하나의 문자열로 연결(join) 하고자 할 때 사용
s = ['We', 'are', 'the', 'champion']
print(s)     # => ['We','are','the','champion']
d = ' '
t = d.join(s)
print(t)
