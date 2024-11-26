import threading
import time

def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def create_input_function():
    # Создаем замыкание для ввода массива
    def input_array():
        return list(map(int, input("Введите элементы массива через пробел: ").split()))
    return input_array

def main_menu():
    print("\nГлавное меню:")
    print("1. Задача 1")
    print("2. Задача 2")
    print("3. Выход")

def rotation_task(global_matrix, matrix_changed):
    # Функция для поворота матрицы в отдельном потоке
    while True:
        if matrix_changed[0]:
            with matrix_lock:
                if matrix_changed[0]:
                    global_matrix[0] = rotate_matrix(global_matrix[0])
                    print("Матрица повернута:")
                    for row in global_matrix[0]:
                        print(row)
                    matrix_changed[0] = False
        time.sleep(0.1)

def main():
    # Используем списки для хранения глобальных переменных
    global_matrix = [None]
    matrix_changed = [False]

    # Запуск потока для поворота матрицы
    rotation_thread = threading.Thread(target=rotation_task, args=(global_matrix, matrix_changed), daemon=True)
    rotation_thread.start()

    input_array = create_input_function()  # Получаем функцию ввода

    while True:
        main_menu()
        choice = int(input("Выберите пункт меню: "))

        if choice == 1:
            array1 = input_array()
            array2 = input_array()
            with matrix_lock:
                global_matrix[0] = [array1, array2]
                matrix_changed[0] = True
            print(f"Результат задачи 1: {global_matrix[0]}")
        elif choice == 2:
            array1 = input_array()
            array2 = input_array()
            array3 = input_array()
            with matrix_lock:
                global_matrix[0] = [array1, array2, array3]
                matrix_changed[0] = True
            print(f"Результат задачи 2: {global_matrix[0]}")
        elif choice == 3:
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    matrix_lock = threading.Lock()  # Инициализация блокировки
    main()