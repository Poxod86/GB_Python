# Определите, можно ли от шоколадки размером a × b долек отломить c долек,
#  если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.

a = int(input("Введите количество рядов шоколадки: "))
b = int(input("Введите количество колонок шоколадки: "))
c = int(input("Сколько кусочков отломить: "))

if c <= a * b and c % a == 0 or c % b == 0:
    print('Да, конечно, угощайся')
else:
    print('Нет, так поделить не могу')