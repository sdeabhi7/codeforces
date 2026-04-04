n = int(input())
for i in range(n):
    t = int(input())
    k = list(map(int, input().split()))
    if len(set(k)) != t:
        print('NO')
    elif len(k) == 1:
        print('YES')
    else:
        print('YES')