s = 'Hello World'
print('0        1')
print('012345678901234')

print(f"문자열 s 출력하기 : {s}")
print(f"문자열 s를 대문자로 출력하기 : {s.upper()}")
print(f"문자열 s를 소문자로 출력하기 : {s.lower()}")
print(f"문자열 s에서 'Wo'의 문자열은 몇번째에 있는가? : {s.find('Wo')}")
print(f"문자열 s에서 'W'는 몇번째 인덱스에 있는가? : {s.index('W')}")
print(f"문자열 s는 'He'로 시작하는가? : {s.startswith('He')}")
print(f"문자열 s는 'W'로 시작하는가? : {s.startswith('W')}")
print(
    f"문자열 s를 소문자로 변환하고, 그 문자열 s가 'h'로 시작하는가? : {s.lower().startswith('h')}\n")

t = '   temp    '
print('123456789123456789')
print(f"문자열 t: {t}")
print(f"문자열 t의 왼쪽 공백 잘라내기 : {t.lstrip()}")
print(f"문자열 t의 오른쪽 공백 잘라내기 : {t.rstrip()}")
print(f"문자열 t의 좌우 공백 잘라내기 : {t.strip()}")
print(f"문자열 t: {t}")
