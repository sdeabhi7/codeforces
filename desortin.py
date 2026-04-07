n = int(input())
for i in range(n):
    k = int(input())
    y = list(map(int, input().split()))
    if y != sorted(y):
        print(0)
    else:
        value = float('inf')
        a, b = 0, 0
        for i in range(len(y)-1):
            s = abs(y[i] - y[i+1])
            if s < value:
                value = s
                a, b = y[i], y[i+1]
        h = abs(b - a)
        print(int(h/2) + 1)