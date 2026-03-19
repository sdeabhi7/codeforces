n = int(input())
for i in range(n):
    k, y, m = map(int, input().split())
    value = m - ((m - y) % k)
    print(value)