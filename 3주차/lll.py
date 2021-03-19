t = int(input())

a = [[0 for i in range(2)] for i in range(4)]


for i in range(t):
    n, m = input().split()
    n = int(n)
    m = int(m)
    a[i][0] = n
    a[i][1] = m

x = 0
while x < t:
    cnt = 0
    if a[x][0] + a[x][1] < 12 or a[x][0] < 5:
        cnt = 0
    elif a[x][1] == 0:
        cnt = a[x][0]//12
    elif a[x][0] == 5 and a[x][1] >= 7:
        cnt = a[x][0]//5
    elif a[x][0] // 5 == a[x][1] // 7:
        cnt = a[x][0] // 5
    elif a[x][0] // 5 < a[x][1] // 7:
        while a[x][0] < 5:
            cnt += a[x][1] // 7
            a[x][0] = a[x][0] - 5 * a[x][1] // 7
            a[x][1] = a[x][1] % 7
            if a[x][0] + a[x][1] < 12:
                break
            else:
                cnt += a[x][0] // 5
    print(cnt)
    x += 1
