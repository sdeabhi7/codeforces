n = int(input())
for i in range(n):
    y = int(input())
    k = list(map(int, input().split()))
    k = sorted(k)[::-1]
    while len(k) != 1:
        if abs(k[-2] - k[-1]) <= 1:
            k.pop()
        else:
            print('NO')
            break
    else:
        print('YES')