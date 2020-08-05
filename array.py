from vector import generates_random_lists, find_element_in_list


def find_two_min_elements_of_vector(arr: list) -> tuple:
    """Ищет 2 минимальных элемента в одномерном массиве
    и возвращает кортеж с этими элементами.
    Аргументы:
    arr -- одномерный массив"""
    minimum1 = find_element_in_list(arr, min)[1]
    arr.remove(minimum1)
    minimum2 = find_element_in_list(arr, min)[1]
    return minimum1, minimum2


def input_array(rows: int, columns: int) -> list:
    """Заполняет матрицу указанного размера с клавиатуры.
    Аргументы:
    rows -- количество строк в матрице
    columns -- количество столбцов в матрице"""
    arr = []
    i = 0
    while i < columns:
        try:
            arr.append([int(input()) for _ in range(rows)])
        except ValueError:
            print("Нужно вводить именно целые числа. Повторите ввод.\n")
            continue
        i += 1
    return arr


def sum_of_values_in_rows(arr: list) -> list:
    """Расчитывает сумму значений в строках
    и добавляет её в конец строки массива
    Аргументы:
    arr -- двумерный массив"""
    [arr[i].append(sum(arr[i])) for i in range(len(arr))]
    return arr


def matrix_output(arr: list):
    """Выводит матрицу на экран в более читабельном виде.
    Пример:
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    Аргументы:
    arr - двумерный массив"""
    [print(arr[i]) for i in range(len(arr))]


def find_min_in_column(arr: list) -> list:
    """Находит минимальное значение в каждом столбце массива
    и возвращает список этих элементов.
    Аргументы:
    arr -- матрица для поиска"""
    minimum = arr[0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if minimum[j] > arr[i][j]:
                minimum[j] = arr[i][j]
    return minimum


if __name__ == "__main__":
    random_list = generates_random_lists(10, 1000)
    print('Список со случайным набором чисел: ')
    print(random_list)
    print("Минимальные элементы вектора: ")
    print(find_two_min_elements_of_vector(random_list))

    array = input_array(4, 4)
    print("Матрица после заполнения с клавиатуры: ")
    matrix_output(array)
    array = sum_of_values_in_rows(array)
    print("Матрица после добавления в конец каждой строки суммы элементов строки: ")
    matrix_output(array)

    print("Результат поиска максимального элемента среди минимальных элементов столбцов матрицы: ")
    print(max(find_min_in_column(array)))
