# Функція - перевірка, чи правильно пораховано вектор х
def check_equality(vec1, vec2):
    return all(abs(x - y) < 1e-6 for x, y in zip(vec1, vec2))
# Оголошуємо функцію lu_decomposition, яка приймає два параметри k і p
def lu_decomposition(k, p):
    # Обчислюємо s і B як 0.02 * k і 0.02 * p відповідно
    s = 0.02 * k
    B = 0.02 * p

    # Створюємо матрицю A з заданими елементами, які залежать від s
    A = [
        [8.3, 2.62 + s, 4.1, 1.9],
        [3.92, 8.45, 7.78 - s, 2.46],
        [3.77, 7.21 + s, 8.04, 2.28],
        [2.21, 3.65 - s, 1.69, 6.69]
    ]

    # Створюємо вектор b з заданими елементами, які залежать від B
    b = [-10.65 + B, 12.21, 15.45 - B, -8.35]

    # Знаходимо розмірність матриці A і вектора b
    n = len(A)

    # Створюємо нульові матриці L і U розмірності n x n
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    # Заповнюємо матриці L і U за допомогою модифікованого алгоритму Гауса
    for i in range(n):
        for j in range(i, n):
            # Елементи верхньотрикутної матриці U обчислюються як різниця між елементами матриці A і сумою добутків елементів матриць L і U
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        # Елементи головної діагоналі матриці L дорівнюють 1
        L[i][i] = 1.0
        for j in range(i + 1, n):
            # Елементи нижньотрикутної матриці L обчислюються як частка між різницею між елементами матриці A і сумою добутків елементів матриць L і U, і елементами головної діагоналі матриці U
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    # Створюємо нульовий вектор c розмірності n
    c = [0.0] * n
    # Знаходимо вектор c за допомогою зворотного ходу для рівняння LY = b
    for i in range(n):
        # Елементи вектора c обчислюються як різниця між елементами вектора b і сумою добутків елементів матриці L і вектора c
        c[i] = b[i]
        for j in range(i):
            c[i] -= L[i][j] * c[j]

    # Створюємо нульовий вектор x розмірності n
    x = [0.0] * n
    # Знаходимо вектор x за допомогою зворотного ходу для рівняння UX = Y
    for i in range(n - 1, -1, -1):
        # Елементи вектора x обчислюються як частка між різницею між елементами вектора c і сумою добутків елементів матриці U і вектора x, і елементами головної діагоналі матриці U
        x[i] = c[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    AX = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]

    # Перевіряємо рівність між AX і b
    if check_equality(AX, b):
        print("Перевірка пройшла успішно: AX дорівнює b.")
    else:
        print("Перевірка не пройшла: AX не дорівнює b.")

    # Повертаємо вектор x як розв'язок системи AX = b
    return x

# Задаємо значення k і p
k = 13
p = 21

# Викликаємо функцію lu_decomposition з заданими k і p і отримуємо вектор x
result = lu_decomposition(k, p)

# Виводимо результат на екран
print("Result:")
for i, sol in enumerate(result):
    print(f"x{i + 1} = {sol:.4f}")


