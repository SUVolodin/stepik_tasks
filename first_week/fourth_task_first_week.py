"""
Прграмма для вычисления площади треугольника по формуле Герона. Использование чисел с плавающей точкой.
"""
a = int(input("Введите длинну первой стороны треугольника: "))
b = int(input("Введите длинну второй стороны треугольника: "))
c = int(input("Введите длинну третьей стороны треугольника: "))
p = (a + b + c) / 2
x = (p - a)
y = (p - b)
z = (p - c)
print(float((p * x * y * z) ** 0.5))
