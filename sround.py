n = int(input())
for i in range(n):
    y = int(input())
    value = []
    i = 0
    while y != 0:
        k = y % 10
        if k != 0:
            value.append(k * (10 ** i))  
        y = y // 10
        i += 1
    print(len(value))
    print(*value)