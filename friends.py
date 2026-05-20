#   author: sdeabhi



n = int(input())
y = []
for i in range(n):
    w, h, k = map(int, input().split())
    value = 1
    while w % 2 == 0:
        w //= 2
        value *= 2
    while h % 2 == 0:
        h //= 2
        value *= 2
    print('Yes' if value >= k else 'No')