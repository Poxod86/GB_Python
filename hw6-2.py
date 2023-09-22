# Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


nums = [int(num) for num in input("Enter numbers: ").split()]
range_list = [int(num) for num in input("Enter range: ").split()]

print(*[i for i in range(len(nums))
        if range_list[0] <= nums[i] <= range_list[1]])