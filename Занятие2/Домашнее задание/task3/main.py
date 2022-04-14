a = int(input('A '))
b = int(input('B'))
c = int(input('C '))

result1 = a < 45 and b >= 45 and c >= 45
result2 = a >= 45 and b < 45 and c >= 45
result3 = a >= 45 and b >= 45 and c < 45

if result1 or result2 or result3:
    print("Одно из чисел меньше 45")
else:
    print("Все числа больше 45 или все числа меньше 45")

