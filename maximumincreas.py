n = int(input())
k = list(map(int, input().split()))
y = 0
value = 0
for i in range(len(k)-1):
    if k[i+1] > k[i]:
        y += 1
        value = max(y, value)
    else:
        y = 0
print(value + 1)