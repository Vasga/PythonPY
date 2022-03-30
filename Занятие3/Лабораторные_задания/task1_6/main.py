# TODO написать функцию для поиска необходимой суммы денег
def summa_(salary, spend, month=10, rost_cen = 0.03):
    su = 0
    for n in range(month):
        su += spend - salary
        spend *= 1 + rost_cen
    return su


if __name__ == "__main__":
    print(summa_(5000, 6000))  # TODO вызвать функцию и проверить работоспособность
