value = 0
k, l, m, n, d = map(int, input().split())
for i in range(1, d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0 or i % d == 0:
        value += 1
print(value)