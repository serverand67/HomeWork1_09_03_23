"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
385916 -> yes
123456 -> no
"""

# Пример 2

tiketNum = input("Введите число из билета (6 цыфр) ")

digit1 = tiketNum[0]
digit2 = tiketNum[1]
digit3 = tiketNum[2]
digit4 = tiketNum[3]
digit5 = tiketNum[4]
digit6 = tiketNum[5]

digit1 = int(digit1)
digit2 = int(digit2)
digit3 = int(digit3)
digit4 = int(digit4)
digit5 = int(digit5)
digit6 = int(digit6)

num1 = digit1 + digit2 + digit3
num2 = digit4 + digit5 + digit6

if num1 == num2:
    print("Это счастливый билет!!!")
else:
    print("Повезет в следующий раз.")
