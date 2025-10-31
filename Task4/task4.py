import numpy as np

# Генерация матриц
A = np.random.randint(1, 11, size=(5, 5))
B = np.random.randint(1, 11, size=(5, 5))

print("A:\n", A)
print()

print("B:\n", B)
print()


print("A * B:\n", A * B)
print()

print("A @ B:\n", A @ B)
print()

print("Определитель А:", np.linalg.det(A))
print()

print("Транспортированная B:\n", B.T)
print()

try:
    print("Обратная матрица А:\n", np.linalg.inv(A))
except:
    print("A вырожденная")


print()

# Решение СЛУ
C = np.sum(A, axis=1).reshape(-1, 1)
x = np.linalg.solve(A, C)
print("x:\n", x)
