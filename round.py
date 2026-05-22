#   author: sdeabhi



n = int(input())
for i in range(n):
    k = int(input())
    value = 0
    power = 1
    while power <= k:
        for digit in range(1, 10):
            num = digit * power
            if num <= k:
                value += 1
        power *= 10
    print(value)