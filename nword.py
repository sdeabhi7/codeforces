n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    print(b[0]+a[1:], a[0]+b[1:])