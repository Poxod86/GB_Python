# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
i = 0
while i**2 < n:
    print(2**i)
    i = i + 1