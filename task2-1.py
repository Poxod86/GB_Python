# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

n = int(input("Введите начальное значение числа: "))

N = 1
i = 0
while i < n:
    i =i+1
    N = N*i
print(N)