def main():
    print("Hello, World!")

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Флаг swapped используется для отслеживания перестановок элементов массива.
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Если текущий элемент больше следующего элемента, меняем их местами.
                array[j], array[j + 1] = array[j + 1], array[j]
                # Устанавливаем флаг swapped в True, чтобы указать, что была выполнена перестановка.
                swapped = True
        # Если не было выполнено ни одной перестановки на этой итерации, значит массив уже отсортирован, выходим из цикла.
        if not swapped:
            break
    return array


if name == 'main':
    main()

    my_array = [5, 2, 8, 12, 3]
    sorted_array = bubble_sort(my_array)
    print(sorted_array)