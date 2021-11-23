# Возведение в степень каждого числа из диапазона и последующее суммирование этих чисел
def my_function(n, k):
    n = int(input("Введите  число n: "))
    k = int(input("Введите  число k: "))
    total_sum1 = 0
    if n > 20:
        return 0
    elif n <= 20:
        for i in range(1, n):
            if i % 2 == 0:
                total_sum1 += i ** k

        return total_sum1


def main():
    print(my_function(21, 2))
    print(my_function(7, 2))
    print(my_function(20, 15))


main()
