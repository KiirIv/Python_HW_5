# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))


def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        tmp = power(a, b/2)
        return tmp * tmp
    else:
        return a * power(a, b-1)


print(power(a, b))
