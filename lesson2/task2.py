# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


array = input("Введите элементы списка разделяя их символом пробел (' '): ").split(sep=' ')
print('Исходный список: ', array)

end_index = len(array) if len(array) % 2 == 0 else len(array) - 1
array[:end_index:2], array[1:end_index:2] = array[1:end_index:2], array[:end_index:2]

print('Конечный список: ', array)
