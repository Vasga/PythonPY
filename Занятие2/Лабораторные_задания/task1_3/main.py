if __name__ == '__main__':
    a = int(input("A="))
    b = int(input("В="))

    A = a ** 2 + b ** 2
    B = (a +b) ** 2

    if A > B:
        print ("Сумма квадратов больше чем квадрат сумм ")
    elif B > A:
        print("Сумма квадратов меньше чем квадрат сумм ")
    else:
        print ("они равны")