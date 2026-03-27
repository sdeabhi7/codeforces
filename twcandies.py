n = int(input())
for i in range(n):
    y = int(input())
    if y > 2 and y % 2 != 0:
        k = int(y / 2)
        print(k)
    elif y > 2 and y % 2 == 0:
        k = int(y / 2) - 1
        print(k)
    else:
        print(0)