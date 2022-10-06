# Семинар 5, задача 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

inp = list(map(str, input('Введите текст: ').split()))
sample = input('Введите удаляемый текст: ')
print(*list(filter(lambda x: x!= sample, inp)))