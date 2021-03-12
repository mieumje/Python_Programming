str = "이번 채용에 참여하는 신규 프로젝트는 총 9종으로 신규 다중접속역할수행게임(MMORPG), 프로젝트 SF2, HP 등 넥슨의 핵심 개발 역량을 집중한 대형 프로젝트를 비롯해 모바일 MMORPG 테일즈위버 M, 하이브리드 해양 어드벤처 장르의 멀티플랫폼 타이틀 DR, 팀 대전 액션 장르의 P2, RPG 장르의 PC 온라인 타이틀 P3 등 다양한 장르와 플랫폼으로 균형 잡힌 신작들이 포함됐다."

a = str.split(" ")
print(a)

""" for c in str:
    if ord(c) >= ord('A') and ord(c) <= ord('Z') or c == ',':
        print(c)
 """
c = []
for i in a:
    for x in i:
        if x >= "A" and x <= "Z":
            print(x, end="")
        print(end=" ")
