"""
Алгоритм сжатия, который сжимает повторяющиеся символы в строке следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'.
"""
s = input()
j = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        j += 1
    elif s[i] != s[i + 1]:
        print(s[i] + str(j), end='')
        j = 1
print(s[-1] + str(j), end='')
