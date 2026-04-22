n = int(input())
for i in range(n):
    k = int(input())
    y = list(map(int, input().split()))
    print(max(y) - min(y))