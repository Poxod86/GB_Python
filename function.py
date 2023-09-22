# модуль числа
number = -5
print(abs(number))

# минимум максимум
numbers = [5,15, 7, 1, -9, 0]
print(max(numbers))
print(min(numbers))

# округление
print(round(10.9834, 2))

# сумма
print(sum(numbers))

# нумерация
winners =['Leo','Max','Kate']
for number, winner in enumerate(winners):
    print(number, winner)