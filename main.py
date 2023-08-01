# 1
i = int(input("Введите число в диапазоне от 1 до 100: "))
if 1 <= i <= 100:
    if not i%3 and not i%5:
        print("Fizz Buzz")
    elif not i%3:
        print("Fizz")
    elif not i%5:
        print("Buzz")
    else:
        print(i)
else:
    print("Введи число в диапазоне от 1 до 100...")

# 2
value2 = int(input("Напишите число: "))
print("0, 1, 2, 3, 4, 5, 6, 7")
value3 = int(input("В какую степень возвести число: "))
if(value3==0):
    print(value2**0)
elif(value3==1):
    print(value2**1)
elif (value3 == 2):
    print(value2 ** 2)
elif (value3 == 3):
    print(value2 ** 3)
elif (value3 == 4):
    print(value2 ** 4)
elif (value3 == 5):
    print(value2 ** 5)
elif (value3 == 6):
    print(value2 ** 6)
elif (value3 == 7):
    print(value2 ** 7)
else:
    print("Возвести можно только до 7 включительно!")

# 3
value4 = input("Введите вашего оператора: ")
print(" 1 - билайн;\n 2 - мегафон;\n 3 - теле2;\n 4 - мтс")
value5 = input("Введите оператора на которого звонили: ")
value6 = int(input("Сколько минут вы проговорили: "))
value7= int(input("Стоимость минуты звонка: "))
if(value5=='1'):
    print("Вы звонили с оператора", value4, "на номер оператора билайн, стоимость звонка за минуту составляет -", value7, "рубля(ей). Вы проговорили: ",value6, "минут. Звонок обошелся в", value6*value7, "рублей." )
elif(value5=='2'):
    print("Вы звонили с оператора", value4, "на номер оператора мегафон, стоимость звонка за минуту составляет -", value7, "рубля(ей). Вы проговорили: ",value6, "минут. Звонок обошелся в", value6*value7, "рублей.")
elif(value5=='3'):
    print("Вы звонили с оператора", value4, "на номер оператора теле2, стоимость звонка за минуту составляет -", value7, "рубля(ей). Вы проговорили: ",value6, "минут. Звонок обошелся в", value6*value7, "рублей.")
elif(value5=='4'):
    print("Вы звонили с оператора", value4, "на номер оператора МТС, стоимость звонка за минуту составляет -", value7, "рубля(ей). Вы проговорили: ",value6, "минут. Звонок обошелся в", value6*value7, "рублей.")
else:
    print("Введите корректное значение!!!!")

# 4
a = int(input('На сколько продал первый менеджер: '))
b = int(input('На сколько продал второй менеджер: '))
c = int(input('На сколько продал третий менеджер: '))
oklad = 200
if a>1000:
   zp1 = oklad+a*0.08
else:
   if a <500:
       zp1 = oklad+a*0.03
   else:
       zp1 = oklad+a*0.05
if b>1000:
   zp2 = oklad+b*0.08
else:
   if b <500:
       zp2 = oklad+b*0.03
   else:
       zp2 = oklad+b*0.05
if c>1000:
   zp3 = oklad+c*0.08
else:
   if c <500:
       zp3 = oklad+c*0.03
   else:
       zp3 = oklad+c*0.05
if zp1 > zp2 and zp1 > zp3:
   print('Лучший по продажам - 1 менеджер!')
   zp1 += 200
if zp2 > zp1 and zp2 > zp3:
   print('Лучший по продажам - 2 менеджер!')
   zp2 += 200
if zp3 > zp1 and zp3 > zp2:
   print('Лучший по продажам - 3 менеджер!')
   zp3 +=200
print('Зарплата 1 менеджера ',zp1)
print('Зарплата 2 менеджера ',zp2)
print('Зарплата 3 менеджера ',zp3)