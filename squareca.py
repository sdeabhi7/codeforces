n = int(input())
for i in range(n):
    k = int(input())
    y = list(map(int, input().split()))
    t = sum(y)
    if int(t ** 0.5)  ** 2 == t:
        print('Yes')
    else:
        print('No') 