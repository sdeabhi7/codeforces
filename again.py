n = int(input())
for i in range(n):
    a = int(input())
    k = 0
    for i in str(a):
        k += int(i)
    print(k)