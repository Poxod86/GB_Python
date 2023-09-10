# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

n = int(input("Введите число: "))
numbers = list()
for i in range(n):
    numbers.append(int(input("Введите число: ")))

print(len(set(numbers)))

# help_list = []
# for i in range(len(numbers)):
# if numbers[i] not in help_list:
# help_list.append(numbers[i])
# print(help_list)
