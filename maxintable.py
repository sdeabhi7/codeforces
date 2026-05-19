#   author: sdeabhi



k = int(input())
if k > 2:
    f_row = [1] * k
    value = [f_row]
    m, n = k, k
    for i in range(1, m):
        t_row = [1]
        for j in range(1, n):
            t_row.append(t_row[-1] + value[i-1][j])
        value.append(t_row)
    print(value[-1][-1])
else:
    print(k)