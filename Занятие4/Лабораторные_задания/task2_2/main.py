def task(num: int) -> int:
    list_ = list(str(num))  # TODO сформировать список цифр
    # print(list_)
    lis_new = [int(d) for d in list_]

    if 4 in lis_new and 8 in lis_new or 9 in lis_new:  # TODO записать условие
        print("Входят цифры (4 и 8) или цифра 9")
    else:
        print("Не входят цифры (4 и 8) или цифра 9")


if __name__ == "__main__":
    task(1234)
    task(12345678)
    task(1235679)
    task(0)
