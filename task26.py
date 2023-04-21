# Задача 26: Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
def exponentiation(basis,multiplier):
    if multiplier ==0:
        return 1
    if multiplier!=0:
        return(basis*exponentiation(basis,multiplier-1))
print("Введите число, которое надо возвести в степень:")
basis=int(input())
print("Введите степень, в которую надо возвести число")
multiplier=int(input())
print("Результат возведения в степень:",exponentiation(basis,multiplier))