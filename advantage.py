n = int(input())
for i in range(n):
    k = int(input())
    s = list(map(int, input().split()))
    t = sorted(s)
    max_value = t[-1]
    max_next = t[-2]
    y = []
    for i in s:
        if i != max_value:
            y.append(i - max_value)
        else:
            y.append(max_value - max_next)
    print(*y)