n = int(input())
value = 0
while n != 0:
    if n // 100 != 0:
        value += n // 100
        n = n % 100
    elif n // 20 != 0:
        value += n // 20
        n = n % 20
    elif n // 10 != 0:
        value += n // 10
        n = n % 10
    elif n // 5 != 0:
        value += n // 5
        n = n % 5
    else:
        value += n
        n -= n
print(value)