n = int(input())
for i in range(n):
    k = int(input())
    if k < 4:
        print(1)
    else:
        t = k // 4
        y = k % 4
        print(t + y // 2)