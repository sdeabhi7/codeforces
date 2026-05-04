n = int(input())
for i in range(n):
    y = []
    for j in range(8):
        s = list(input())
        y.append(s)
    k = ''
    for i in y:
        for j in i:
            if j in 'qwertyuiopasdfghjklzxcvbnm':
                k += j
    print(k)