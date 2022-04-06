if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    list_1 = [i for i in list_ if i % 2 == 0]
    list_2 = [i for i in list_ if i % 2 == 1]# TODO получить два списка четных и нечетных чисел

    print("Чет", len(list_1), "Нечет", len(list_2))

    # print(len(list_2))                                               # TODO найти длины этих списков

    if len(list_1) > len(list_2):
        print("Список четных больше")# TODO распечатать каких чисел больше. Учтите, что длины могу быть равны
    elif len(list_1) < len(list_2):
        print("Список нечетных больше")
    else:
        print("Списки равны")
