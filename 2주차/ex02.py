val = [3, 41, 12, 9, 74, 15]
print('최소값 : ', min(val))
print('최대값 : ', max(val))

min = min(val)
for i in val:
    print(f"최소값의 위치는 {val.index(min)}")
    break;

max = max(val)
for i in val:
    print(f"최대값의 위치는 {val.index(max)}")
    break;