a, b, y = map(int, input().split())
m = 0
m = max(min(a,b), min(b,y), min(a,y))
print(abs(a-m) + abs(b-m) + abs(y-m))