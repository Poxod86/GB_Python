# Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Сумма загаданных чисел равна: "))
mult = int(input("Произведение загаданных чисел равно: "))


D = sum**2 -4*mult
y1 = (sum + D**0.5 ) /2
y2 = (sum - D**0.5 ) /2
print(y1)
print(y2)