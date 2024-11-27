def rotate_matrix(matrix):
    """Поворачивает матрицу на 90 градусов по часовой стрелке."""
    return [list(reversed(col)) for col in zip(*matrix)]

def input_array(prompt="Введите элементы массива через пробел: "):
    """Функция для ввода массива от пользователя."""
    return list(map(int, input(prompt).strip().split()))

def main_menu():
    """Отображает главное меню."""
    print("\nГлавное меню:")
    print("1. Задача 1")
    print("2. Задача 2")
    print("3. Повернуть матрицу")
    print("4. Выход")

def task_1(array1, array2):
    """Пример задачи 1 (сумма двух массивов)."""
    return list(map(lambda x, y: x + y, array1, array2))

def task_2(array1, array2, array3):
    """Пример задачи 2 (сумма трех массивов)."""
    return list(map(lambda x, y, z: x + y + z, array1, array2, array3))

def get_matrix_input(rows_count):
    """Функция для ввода матрицы заданного количества рядов."""
    return [input_array(f"Введите ряд {i + 1} матрицы через пробел: ") for i in range(rows_count)]

def main():
    while True:
        main_menu()
        choice = input("Выберите пункт меню: ")
        
        if choice == '1':
            array1 = input_array()
            array2 = input_array()
            result = task_1(array1, array2)
            print("Результат задачи 1:", result)
        elif choice == '2':
            array1 = input_array()
            array2 = input_array()
            array3 = input_array()
            result = task_2(array1, array2, array3)
            print("Результат задачи 2:", result)
        elif choice == '3':
            try:
                rows_count = int(input("Введите количество рядов матрицы: "))
                matrix = get_matrix_input(rows_count)
                rotated_matrix = rotate_matrix(matrix)
                print("Исходная матрица:", matrix)
                print("Повернутая матрица:", rotated_matrix)
            except ValueError:
                print("Пожалуйста, введите целое число.")
        elif choice == '4':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()