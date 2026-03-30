n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    k = list(map(int, input().split()))
    if b in k:
        print('YES')
    else:
        print('NO')