mount = int(input ( "Введите номер месяца "))  # TODO запросить месяц у пользователя. Номер месяца - целочисленное значение!

if  mount == 3 or mount == 4 or mount == 5  :  # TODO записать условие через операторы or
    print("Весна")
elif mount in [6, 7, 8]:  # TODO проверить вхождение месяца в список месяцев лета
    print("Лето")
elif mount in (9, 10, 11):
    print("Осень")
elif mount in {12, 1, 2}:
    print("Зима")
