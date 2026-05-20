#   author: sdeabhi



n = int(input())
for i in range(n):
    k = int(input())
    max_value = 0
    t = 0
    for i in range(2, k+1):
        value = 0
        for j in range(i, k+1):
            if j % i == 0:
                value += j
        if value >= max_value:
            max_value = value
            t = i
    print(t)