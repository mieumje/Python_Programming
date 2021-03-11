# 그래프를 그리기 위한 모듈 선언
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


# matplotlib는 파이썬에서 매트랩과 유사한 그래프 표시를 가능하게 하는 라이브러리
# matplotlib에서 한글 폰트가 깨지는 경우가 있어 font_manager를 통해 한글 폰트를 등록한다
# 컴퓨터에 등록된 한글 폰트 목록은 [C:/Windows/Fonts/]에서 확인 할 수 있다.

font_path = 'C:/Windows/Fonts/malgun.ttf'  # 컴퓨터에 설치된 폰트 경로

font_name = font_manager.FontProperties(fname=font_path).get_name()
# font_manager를 통해 font_path에 있는 font의 이름을 가져온다.
rc('font', family=font_name)
# rc를 통해 font를 설정한다.


x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# x축에 표시할 제목 리시트에 저장

plt.title('일주일간 유동 인구수 데이터', fontsize=16)  # 큰 제목
plt.xlabel('요일', fontsize=12)  # x축 제목
plt.ylabel('유동 인구수', fontsize=12)  # y 축 제목

# y축에 표시할 유동 인구 데이터 입력
a = [242, 256, 237, 223, 263, 81, 46]

weekday_size = 5  # 주중 데이터
weekday_sum = 0
weekday_avg = 0

for i in range(0, weekday_size):
    weekday_sum = weekday_sum + a[i]

weekday_avg = weekday_sum / weekday_size

print('주중 유동 인구 = ', a[0:5])
print('주중 유동 인구 합계 = ', weekday_sum)
print('주중 유동 인구 평균 = ', weekday_avg)

plt.scatter(x_data, a, c="red", label="유동인구")  # 산점도 표시
plt.plot(x_data, a, c="red")  # 꺾은선 그래프
plt.legend()
plt.show()
