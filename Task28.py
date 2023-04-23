# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4


def sum(first_number: int, second_number: int) -> int:
    """"Принимает на вход два целых неотрицательных числа и возвращает их сумму"""
    if second_number == 0:
        return first_number
    return sum(first_number+1, second_number-1)


print("Введите первое целое неотрицательное число")
first_number = int(input())
print("Введите второе целое неотрицательное число")
second_number = int(input())
print("Сумма двух введеных целых неотрицательных чисел =",
      sum(first_number, second_number))
