# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

room1 = int(input("Введите число учеников в первом классе: "))
room2 = int(input("Введите число учеников в втором классе: "))
room3 = int(input("Введите число учеников в третьем классе: "))

desk1 = room1 // 2  +  room1 % 2
desk2 = room2 // 2  +  room2 % 2
desk3 = room3 // 2  +  room3 % 2
result = desk1 + desk2 + desk3

print(result)