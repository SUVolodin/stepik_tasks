"""
Простой калькулятор, принимающий на ввод три строки:
число 1, число 2 и операцию.
Поддерживаемые операции: +, -, /, *, mod, pow, div.
"""
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
c = input('Введите арифметическое действие: ')
if c == '+':
    print(a + b)
if c == '-':
    print(a - b)
if c == '*':
    print(a * b)
if c == 'pow':
    print(a ** b)
if (c == '/' or c == 'div' or c == 'mod') and b == 0:
    print('Деление на 0!')
elif c == '/':
    print(a / b)
elif c == 'div':
    print(a // b)
elif c == 'mod':
    print(a % b)