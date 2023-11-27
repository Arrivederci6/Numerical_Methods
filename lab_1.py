def lu_decomposition(k, p):
    s = 0.02 * k
    B = 0.02 * p

    A = [
        [8.3, 2.62 + s, 4.1, 1.9],
        [3.92, 8.45, 7.78 - s, 2.46],
        [3.77, 7.21 + s, 8.04, 2.28],
        [2.21, 3.65 - s, 1.69, 6.69]
    ]

    b = [-10.65 + B, 12.21, 15.45 - B, -8.35]

    n = len(A)

    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        L[i][i] = 1.0
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    c = [0.0] * n
    for i in range(n):
        c[i] = b[i]
        for j in range(i):
            c[i] -= L[i][j] * c[j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = c[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

k = 13
p = 21

result = lu_decomposition(k, p)

print("Result:")
for i, sol in enumerate(result):
    print(f"x{i + 1} = {sol:.4f}")
