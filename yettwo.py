n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    k = abs(a - b) 
    if k % 10 == 0:
        print(k // 10)
    else:
        print(k // 10 + 1)
    
# 13
# 42
# 29
