n = int(input())
for i in range(n):
    k = int(input())
    y = list(map(int, input().split()))
    s = 0
    for i in range(k-1):
        if y[i] % 2 == y[i+1] % 2:
            s += 1
    print(s)