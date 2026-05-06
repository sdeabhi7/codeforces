n = int(input())
for i in range(n):
    vlad_n = int(input())
    vlad = input()
    dima_n = int(input())
    dima = input()
    order = input()
    begin = ''
    last = ''
    for i, j in zip(dima, order):
        if j == 'D':
            last += i
        else:
            begin += i
    print(begin[::-1] + vlad + last)