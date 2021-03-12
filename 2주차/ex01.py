print(len([3,41,12,9,74,15]))
fr =  [3,41,12,9,74,15] 
print(len(fr))
print(sum(fr))

avg = sum(fr) / len(fr)
print(f"평균은 {avg}")

count_a = 0
for i in fr:
    if i >= 20:
        count_a = count_a + 1
print(f"20 이상의 값은 총 {count_a}개")

sum_a = 0
for i in fr:
    if i >= 20:
        sum_a = sum_a + i
print(f"20 이상인 값의 합계는 {sum_a}")