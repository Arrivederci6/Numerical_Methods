# Імпортуємо numpy
import numpy as np

# Визначаємо функцію, яку хочемо розв'язати
def f(x):
    return x - x**2

# Визначаємо інтервал, на якому шукаємо корінь
a = -3 # Ліва межа
b = 2 # Права межа

# Визначаємо точність, з якою хочемо знайти корінь
eps = 0.001 # Бажана похибка

# Використовуємо метод поділу ділянки навпіл, поки не досягнемо бажаної точності
while abs(b - a) > eps:
    # Знаходимо середину інтервалу
    c = (a + b) / 2
    # Перевіряємо, чи змінюється знак функції на підінтервалах [a, c] та [c, b]
    if np.sign(f(a)) * np.sign(f(c)) < 0:
        # Якщо знак змінюється на [a, c], то корінь лежить на цьому підінтервалі
        # Звужуємо інтервал до [a, c]
        b = c
    elif np.sign(f(c)) * np.sign(f(b)) < 0:
        # Якщо знак змінюється на [c, b], то корінь лежить на цьому підінтервалі
        # Звужуємо інтервал до [c, b]
        a = c
    else:
        # Якщо знак не змінюється на жодному підінтервалі, то ми знайшли корінь
        # Зупиняємо цикл
        break

# Виводимо наближене значення кореня та значення функції в цій точці
print(f"Корінь рівняння y = x - x^2 на інтервалі [-3; 2] дорівнює {c}")
print(f"Значення функції в цій точці дорівнює {f(c)}")
