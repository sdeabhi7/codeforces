n = int(input())
for i in range(n):
    k = list(map(int, input().split()))
    h = 23 - k[0]
    m = 60 - k[1]
    print(h * 60 + m)