n = int(input())
value = 0
k = list(map(int, input().split()))
h = max(k)
for i in range(n):
    value += h - k[i]
print(value)