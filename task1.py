#  Семинар 2, задача 2
#  Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

def Factorial(number): 
    if number == 1:
        return 1
    else:
        return number * Factorial(number - 1)
print(*list(map(Factorial, [i for i in range(1, int(input('Введите число: ')) + 1)])))