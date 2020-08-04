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
    for i in range(columns):
        arr.append([int(input()) for _ in range(rows)])
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


def reverse_matrix(arr: list) -> list:
    """Находит максимальное значение в каждом столбце массива
    и возвращает список этих элементов.
    Аргументы:
    arr -- матрица для поиска"""
    new_arr = []
    for i in range(len(arr)):
        new_arr.append([])
        for j in range(len(arr[i])):
            new_arr[i].append(arr[j][i])
    return new_arr


def find_max_in_column(arr: list) -> list:
    """Находит максимальное значение в каждом столбце массива
        и возвращает список этих элементов.
        Аргументы:
        arr -- матрица для поиска"""
    maximum = []
    for i in arr:
        maximum.append(max(i))
    return maximum


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

    array = reverse_matrix(array)
    print("Результат поиска минимального элемента среди максимальных элементов столбцов матрицы: ")
    print(min(find_max_in_column(array)))
