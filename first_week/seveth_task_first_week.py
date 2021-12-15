"""
Вычисление площади фигур по заданным параметрам.
"""
PI = 3.14
form = input()
if form == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    x = (p - a)
    y = (p - b)
    z = (p - c)
    print(((p * x * y * z)**0.5))
if form == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
if form == 'круг':
    r = float(input())
    print(PI * (r ** 2))