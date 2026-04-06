n = int(input())
for i in range(n):
    k = int(input())
    y = list(map(int, input().split()))
    min_y = min(y)
    value = 0
    for i in y:
        value += i - min_y
    print(value)