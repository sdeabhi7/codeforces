#   author: sdeabhi



n = int(input())
for i in range(n):
    k = int(input())
    s = input()
    y = input()
    t = 'Yes'
    for i, j in zip(s, y):
        if i == 'G' and j == 'R' or i == 'R' and j == 'G' or i == 'R' and j == 'B' or i == 'B' and j == 'R':
            t = 'No'
            break
    print(t)