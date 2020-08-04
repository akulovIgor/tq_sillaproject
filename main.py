import random
import operator


def sum_even_numbers(span: int, multiplicity: int) -> int:
    """Функция вычисляет сумму чисел кратных определённому значению
     и в определённому интервале от 0 до указанного в аргументах
     Аргументы:
    span -- верхнее ограничение интервала
    multiplicity -- значение, которому число должно быть кратно"""
    return sum([i for i in range(span) if i % multiplicity == 0])


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


def find_element_in_list(array: list, fn) -> int:
    """Ищет в списке минимальный/максимальный элемент и возвращает
    индекс элемента
    Аргументы:
    array -- список, в котором ищем значение
    fn -- функция, которую необходимо применить для поиска
    Например, min или max."""
    index, _ = fn(enumerate(array), key=operator.itemgetter(1))
    return index


def swap_elements(array: list, index1: int, index2: int) -> list:
    """Меняет в списке местами элементы с указанными индексами
    Аргументы:
    array -- список, в котором производится замена
    index1, index2 -- индекс элементов, которые нужно поменять местами"""
    array[index1], array[index2] = array[index2], array[index1]
    return array


if __name__ == '__main__':
    print(f'Сумма чисел кратных трём в ряде Фибоначи до 4000000 равна: {sum(fibonacci())}')

    print(f'Сумма натуральных чисел до 1000 кратных 6 равна: {sum_even_numbers(1000, 6)}')
    print(f'Сумма натуральных чисел до 1000 кратных 7 равна: {sum_even_numbers(1000, 7)}')

    random_list = generates_random_lists(10, 1000)
    print('Список со случайным набором чисел: ')
    print(random_list)
    random_list = swap_elements(random_list,
                                find_element_in_list(random_list, max),
                                find_element_in_list(random_list, min))
    print('Список со случайным набором чисел, после смены местами максимального и минимального значений: ')
    print(random_list)
