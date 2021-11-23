def is_even(a):
    a = input("Введите число: ")
    if int(a) % 2 == 0:
        print(str(a) + " - чётное число")
    elif int(a) % 2 > 0 or int(a) % 2 < 0:
        print((str(a) + " - нечётное число"))
    return a


b = is_even(10)

