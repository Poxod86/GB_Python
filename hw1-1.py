# Найдите сумму цифр трехзначного числа n.
# Результат сохраните в перменную res.

n = int(input("Введите трехзначное число: "))

handred = int(n / 100)
ten = int(n / 10 % 10)
unit = int(n % 10)
res = str(handred) + str(ten) + str(unit)

print(res)
