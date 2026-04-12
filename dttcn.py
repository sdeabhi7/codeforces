t = int(input())
for i in range(t):
    n, y = map(int, input().split())
    a = input().strip()
    s = input().strip()
    k = 0
    while len(a) < y:
        a += a
        k += 1
    for i in range(5):
        if s in a:
            print(k)
            break
        a += a
        k += 1
    else:
        print(-1)