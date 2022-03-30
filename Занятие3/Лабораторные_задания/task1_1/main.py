def main():
    n = 1  # первое натуральное число
    current_sum = 0  # текущая сумма
    max_sum = 500  # максимальная сумма

    while True:
        current_num = n ** 4
        if current_sum + current_num >= max_sum:
            break
        current_sum = current_sum + current_num
        n += 1
    return n, current_sum



if __name__ == "__main__":
    count_numbers, sum_ = main()
    print(count_numbers, sum_)
    print(type(count_numbers))
