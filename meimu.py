n = int(input())
for i in range(n):
    a, b, y = map(int, input().split())
    print(max(min(a,b), min(b,y), min(a,y)))