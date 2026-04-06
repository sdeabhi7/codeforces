n = int(input())
for i in range(n):
    k = int(input())
    y = list(map(int, input().split()))
    min_y = min(y)
    t = 0
    value = 1
    for i in y:
        if i == min_y and t != 1:
            value *= i + 1
            t += 1
        else:
            value *= i
    print(value)