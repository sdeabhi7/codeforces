n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        print(a, b)
    else:
        print(b, a)