n = int(input())
for i in range(n):
    t = int(input())
    k = list(map(int, input().split()))
    y = {}
    for i in set(k):
        if k.count(i) == 1:
            print(k.index(i) + 1)