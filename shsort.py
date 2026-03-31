n = int(input())
for i in range(n):
    k = input()
    for i, j in enumerate(k):
        if (i == 0 and j == 'a')  or (i == 1 and j == 'b') or (i == 2 and j == 'c'):
            print('YES')
            break
    else:
        print('NO') 