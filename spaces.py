n = int(input())
for i in range(n):
    max_space = 0
    a = int(input())
    k = list(map(int, input().split()))
    y = 0
    
    for i in k:
        if i == 0:
            y += 1
            max_space = max(y, max_space)
        else:
            y = 0
    print(max_space)