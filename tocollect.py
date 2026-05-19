#   author: sdeabhi



n = int(input())
for i in range(n):
    a, b, c, n = map(int, input().split())
    max_value = max(a, b, c)
    t = (max_value - a) + (max_value - b) + (max_value - c)
    if n >= t and (n - t) % 3 == 0:
        print("Yes")
    else:
        print("No")