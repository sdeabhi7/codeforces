n = int(input())
for i in range(n):
    a, b, y = map(int, input().split())
    if a == b:
        print(y)
    elif a == y:
        print(b)
    else:
        print(a)