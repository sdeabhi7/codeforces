n = int(input())
k = list(map(int, input().split()))
s = 0
l = 0
for i in k:
    if i == -1 and l > 0:
        l -= 1
    elif i == -1 and l == 0:
        s += 1
    else:
        l += i
print(s)