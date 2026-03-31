n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c = min(a,b)
    print((c-a)+(b-c))