a = input()
b = input()
y = input()
n = a + b
k = {}
t = 'YES'
if len(n) != len(y):
    print('NO')
else:
    for i in n:
        if i not in k:
            k[i] = 1
        else:
            k[i] += 1
    for i in set(y):
        if i not in k or y.count(i) != k[i]:
            t = 'NO'
    print(t)