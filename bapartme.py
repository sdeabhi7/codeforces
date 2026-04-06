n = int(input())
for i in range(n):
    k = input()
    if k == 1:
        print(1)
        break
    else:
        y = k[0]
        t = 10 * (int(y) - 1)
        if len(k) == 1:
            print(int(t) + 1)
        elif len(k) == 2:
            print(int(t) + 3)
        elif len(k) == 3:
            print(int(t) + 6)
        else:
            print(int(t) + 10)
        