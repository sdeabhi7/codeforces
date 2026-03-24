n, k, l, c, d, p, nl, np = map(int, input().split())
ml = k * l
t = ml / nl
s = c * d
h = p / np
print(int(min(t, s, h)/n))