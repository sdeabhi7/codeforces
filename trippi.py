#   author: sdeabhi



n = int(input())
for i in range(n):
    s = input()
    k = s.split()
    y = ''
    for i in k:
        y += i[0]
    print(y)