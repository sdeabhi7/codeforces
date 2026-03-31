n = int(input())
for i in range(n):
    k = int(input())
    y = 0
    for j in range(1, k*3):
        if j % 3 != 0 and str(j)[-1] != '3':
            y += 1
            if y == k:
                print(j)