import random
import operator


def sum_even_numbers_seven_or_six(span: int) -> int:
    """Функция вычисляет сумму чисел кратных 6 или 7
     и в определённому интервале от 0 до указанного в аргументах
     Аргументы:
    span -- верхнее ограничение интервала"""
    return sum([i for i in range(span) if (i % 6 == 0 or i % 7 == 0)])


def fibonacci() -> list:
    """Функция для генерации ряда Фибоначчи,
    в котором содеражатся только числа кратные трём и
    ряд начинается с 1 и 2"""
    fib1 = 1
    fib2 = 2
    fibonacci_row = [fib1, fib2]
    while True:
        if fib2 > 4_000_000:
            break
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 % 3 == 0:
            fibonacci_row.append(fib2)
    return fibonacci_row


def generates_random_lists(quantity: int, span: int) -> list:
    """Генерирует список с рандомными значениями от 0 до заданного значения
    Аргументы:
    quantity -- количество элементов в списке
    span -- верхнее ограничение числа для генерации"""
    return [random.randint(0, span) for i in range(quantity)]


def find_element_in_list(array: list, fn) -> tuple:
    """Ищет в списке минимальный/максимальный элемент и возвращает
    кортеж с индексом элемента и его значением
    Аргументы:
    array -- список, в котором ищем значение
    fn -- функция, которую необходимо применить для поиска
    Например, min или max."""
    index, value = fn(enumerate(array), key=operator.itemgetter(1))
    return index, value


def swap_elements(array: list, index1: int, index2: int) -> list:
    """Меняет в списке местами элементы с указанными индексами
    Аргументы:
    array -- список, в котором производится замена
    index1, index2 -- индекс элементов, которые нужно поменять местами"""
    array[index1], array[index2] = array[index2], array[index1]
    return array


if __name__ == '__main__':
    print(f'Сумма чисел кратных трём в ряде Фибоначи до 4000000 равна: {sum(fibonacci())}')

    print(f'Сумма натуральных чисел до 1000 кратных 6 или 7 равна: {sum_even_numbers_seven_or_six(1000)}')

    random_list = generates_random_lists(10, 1000)
    print('Список со случайным набором чисел: ')
    print(random_list)
    random_list = swap_elements(random_list,
                                find_element_in_list(random_list, max)[0],
                                find_element_in_list(random_list, min)[0])
    print('Список со случайным набором чисел, после смены местами максимального и минимального значений: ')
    print(random_list)
