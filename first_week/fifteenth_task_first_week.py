"""
Программа, на вход которой подается одна строка с целыми числами должна вывести сумму этих чисел.
"""
a = [int(i) for i in input().split()]
j = 0
for i in a:
    j = j + i
print(j)
