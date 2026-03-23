n = int(input())
for i in range(n):
    k = int(input())
    if k >= 1900:
        print('Division 1')
    elif 1600 <= k <= 1899:
        print('Division 2')
    elif 1400 <= k <= 1599:
        print('Division 3')
    else:
        print('Division 4')