# Требуется найти в массиве list_1 
# самый близкий по величине элемент к заданному числу k и вывести его.

n = int(input("Введите число: "))
list_1 = list()
for i in range(n):
    list_1.append(int(input("Введите число: ")))
print(list_1)

k = int(input("Какое число ищем?: "))

prew = abs(k-list_1[0])
close = list_1[0]
for j in list_1:
    if abs(k-j) < prew:
        prew = abs(k-j)
        close = j
print(f'Самое близкое к числу {k}, число {close}')