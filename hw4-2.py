# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
flag = True
while flag:
    n = int(input("Введите количество кустов на клумбе: "))
    if n >= 3:
        flag = False
    else:
        print("В клумбе не может быть меньше 3х кустов")

berry_list = list()
for i in range(n):
    count_berry = int(input(f"Введите количество ягод на {i}-ом кусте: "))
    berry_list.append(count_berry)

print (berry_list)
max_berry = 0
for i in range(len(berry_list)):
    sum = (berry_list[i-1]+berry_list[i]+ berry_list[i-2])
    print (sum)
    if sum > max_berry: max_berry = sum
print(max_berry)
