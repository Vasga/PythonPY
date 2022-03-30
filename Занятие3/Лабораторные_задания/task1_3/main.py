def get_list_number_divisors(number):
    list_numbers = []
    for divisior in range(1, number + 1):
        if number % divisior == 0:
            list_numbers.append(divisior)
    return list_numbers



if __name__ == "__main__":
    print(get_list_number_divisors(4))
