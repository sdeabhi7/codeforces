n = int(input())
k = 0
t = 0
for i in range(1, n+1):
    if n >= 0:
        t += i
        n -= t
        if n < 0:
            break
        else:
            k += 1
print(k)