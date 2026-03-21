n = int(input())
for i in range(n):
    k = list(map(int, input().split()))
    y = k[0]
    k.sort()
    print(len(k) - (k.index(y) + 1))