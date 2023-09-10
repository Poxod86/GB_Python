# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_1 = [1, 2, 3, 4, 5]
k = 2
k %= len(list_1)
# 1 2 3 4 5 - input
# 0 1 2 3 4 - index

# 3 4 5 1 2 - output
# 2 3 4 0 1 - index
output_list = []
for i in range(k):
    output_list.append(list_1[len(list_1) - k + i])
for i in range(len(list_1) - k):
    output_list.append(list_1[i])
print(output_list)
