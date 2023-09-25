import math
E = 3e6 
epsilon_0 = 8.85e-12
epsilon = 1

r1 = float(input("Введите диаметр первого шара (м): "))
r2 = float(input("Введите диаметр второго шара (м): "))
r3 = float(input("Введите диаметр третьего шара (м): "))

def calculate_qmax(radius):
    return E / (4 * math.pi * epsilon_0 * epsilon * radius ** 2)

qmax1 = calculate_qmax(r1 / 2)
qmax2 = calculate_qmax(r2 / 2)
qmax3 = calculate_qmax(r3 / 2)

# Вывод результатов
print(f"Максимальный предельный заряд для шара с диаметром {r1} м: {qmax1} Кл")
print(f"Максимальный предельный заряд для шара с диаметром {r2} м: {qmax2} Кл")
print(f"Максимальный предельный заряд для шара с диаметром {r3} м: {qmax3} Кл")
