import numpy as np

# Функція, яка повертає значення системи рівнянь та її матрицю Якобі
def f (x):
    f1 = 1 - np.exp (-x [0]) * np.cos (x [1]) - x [0]
    f2 = np.exp (-x [0]) * np.sin (x [1]) + 1 - x [1]
    F = np.array ([f1, f2])
    J = np.array ([[-np.exp (-x [0]) * np.cos (x [1]) - 1, np.exp (-x [0]) * np.sin (x [1])], [-np.exp (-x [0]) * np.sin (x [1]), np.exp (-x [0]) * np.cos (x [1]) - 1]])
    return F, J

# Спрощений метод Ньютона
def newton (x0, tol, maxiter):
    x = x0
    for i in range (maxiter):
        F, J = f (x)
        dx = np.linalg.solve (J, -F) # Розв'язуємо систему J * dx = -F
        x = x + dx # Оновлюємо наближення
        if np.linalg.norm (dx) < tol: # Перевіряємо умову зупинки
            break
    return x, i

# Початкове наближення
x0 = np.array ([0.1, 0.1])

# Точність
tol = 1e-6

# Максимальна кількість ітерацій
maxiter = 50

# Знаходимо корені системи рівнянь
x, i = newton (x0, tol, maxiter)

# Виводимо результат
print ("Корені системи рівнянь:")
print (x)
print ("Кількість ітерацій:")
print (i)
