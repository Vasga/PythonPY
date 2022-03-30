# TODO запишите здесь функцию factorial
def factorial(n):
    proiz = 1
    for nom in range(1, n + 1):
        proiz *= nom
    return proiz

if __name__ == "__main__":
    print(factorial(5))
    # TODO распечатать результат выполнения функции factorial от числа 5
