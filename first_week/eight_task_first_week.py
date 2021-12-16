"""
Нахождение максимального и минимального числа.
"""
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c and b >= c:
    print(a)
    print(c)
    print(b)
elif a <= b and a <= c and b <= c:
    print(c)
    print(a)
    print(b)
elif b >= c and b >= a and c >= a:
    print(b)
    print(a)
    print(c)
elif b <= c and b <= a and c <= a:
    print(a)
    print(b)
    print(c)
elif c >= a and c >= b and a >= b:
    print(c)
    print(b)
    print(a)
elif c <= a and c <= b and a <= b:
    print(b)
    print(c)
    print(a)
