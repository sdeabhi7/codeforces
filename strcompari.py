n = int(input())
s = 'codeforces'
for i in range(n):
    k = 0
    y = input()
    for i,j in zip(s, y):
        if i != j:
            k += 1
    print(k)