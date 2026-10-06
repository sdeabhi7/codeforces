#   author: sdeabhi



r = int(input())
for i in range(r):
    n, k = map(int, input().split())
    t = n - k + 1
    s = 1
    for j in range(t):
        s *= 2
    s += (n - t) * 2
    print(s)