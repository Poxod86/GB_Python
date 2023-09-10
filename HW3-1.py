# Требуется вычислить, 
# сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

n = int(input("Введите число: "))
list_1 = list()
for i in range(n):
    list_1.append(int(input("Введите число: ")))
print(list_1)

k = int(input("Какое число ищем?: "))

count = 0
for j in list_1:
    if j == k:
        count = count + 1
print (f'Число {k} втречается {count} раз')