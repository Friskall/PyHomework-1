
# Задание 1
# Пользователь вводит с клавиатуры два числа. Необходимо
# найти сумму чисел,разницу чисел,произведение чисел.
# Результат вычислений вывести на экран.

#Start_1
# """

def sum_numbers(a, b):
    result = a + b
    return result

def neg_numbers(a, b):
    result = a - b
    return result

def mult_numbers(a, b):
    result = a * b
    return result

def dev_numbers(a, b):
    result = a / b
    return result

a = float(input("Введи 1е число: "))
b = float(input("Введи 2е число: "))

print(f"{a} + {b} = {sum_numbers(a, b):.2f}")
print(f"{a} - {b} = {neg_numbers(a, b):.2f}")
print(f"{a} * {b} = {mult_numbers(a, b):.2f}")
print(f"{a} / {b} = {dev_numbers(a, b):.2f}")

# """
#End_1

# Задание 2
# Пользователь вводит с клавиатуры три числа.Первое
# число—зарплата за месяц,второе число—сумма месячного
# платежа по кредиту в банке, третье число — задолженность
# за коммунальные услуги.Необходимо вывести
# на экран сумму, которая останется у пользователя после
# всех выплат.

#Start_2
# """

def sum_left(a, b, c):
    result = a - (b+c)
    return result

a = int(input("Введи сумму зарплаты за месяц (Р): "))
b = int(input("Введи сумму месячного платежа по кредиту в банке (Р): "))
c = int(input("Введи сумму задолжненности за коммунальные усгули (Р): "))


print(f"От зарплаты в {a}р после вычета {b}р с банка и {c}р с коммунальных услуг, останется: {sum_left(a, b, c)}р")

# """
#End_2

# Задание 3
# Напишите программу,вычисляющую площадь ромба.
# Пользователь с клавиатуры вводит длину двух его
# диагоналей

#Start_3
# """

def formula(a,b):
    result = (a * b)/2
    return result

a = float(input("Введи диагональ ромба №1 (см): "))
b = float(input("Введи диагональ ромба №2 (см): "))
print(f"Площадь ромба с диагоналями: {b}см и  {a}см, равна: {formula(a, b):.2f}см")

# """
#End_3

# Задание 4
# Выведите на экран надпись To be or not to be на разных
# строках.

#Start_4
# """

print(f"\tTo be\n\tor not\n\tto be")

# """
#End_4

# Задание 5
# Выведите на экран надпись «Life is what happens when
# you're busy making other plans» John Lennon на разных
# строках.

#Start_4
# """

tabs = "\t" * 10
print(f"\t«Life is what happens\n\t\twhen\n\t\t   you're busy making other plans»\n{tabs}John Lennon")

# """
#End_5