n = int(input())
k = list(map(int, input().split()))
min_s = k[0]
max_s = k[0]
y = 0
for i in range(1,n):
    if k[i] > max_s:
        max_s = k[i]
        y += 1
    elif k[i] < min_s:
        min_s = k[i]
        y += 1
print(y)