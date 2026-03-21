n = int(input())
value = ''
for i in range(1, n+1):
    if i % 2 != 0 and i != n:
        value += 'I hate that '
    elif i % 2 == 0 and i != n:
        value += 'I love that '
    elif i % 2 != 0 and i == n:
        value += 'I hate it'
    else:
        value += 'I love it'
print(value)