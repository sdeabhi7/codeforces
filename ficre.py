n, k = map(int, input().split())
t = 0
for i in range(n):
    a, b = map(str, input().split())
    if a == '+':
        k += int(b)
    elif a == '-' and k >= int(b):
        k -= int(b)
    else:
        t += 1
print(k, t)