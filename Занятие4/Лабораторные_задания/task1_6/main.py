if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

    list_great_first = len([i for i in list_ if i > list_[0]])   # TODO отфильтровать элементы больше первого
    list_1 = [i for i in list_ if i > list_[0]]
    print(list_great_first)
    print(list_1)