"""
Вычисление площади фигур по заданным параметрам.
"""
PI = 3.14
form = input()
if form == 'треугольник':
    a = float(input('Введите длинну первой стороны треугольника: '))
    b = float(input('Введите длинну второй стороны треугольника :'))
    c = float(input('Введите длинну третьей стороны треугольника :'))
    p = (a + b + c) / 2
    x = (p - a)
    y = (p - b)
    z = (p - c)
    print(((p * x * y * z)**0.5))
if form == 'прямоугольник':
    a = float(input('Введите длинну прямоугольника :'))
    b = float(input('Введите ширину прямоугольника :'))
    print(a * b)
if form == 'круг':
    r = float(input('Введите радиус окружности :'))
    print(PI * (r ** 2))