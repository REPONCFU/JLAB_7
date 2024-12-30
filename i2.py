# Ввод списка вещественных чисел
n = int(input("Enter the number of elements in the list: "))
lst = [float(input(f"Enter element {i+1}: ")) for i in range(n)]

# 1. Сумма элементов списка с нечётными номерами (индексы 1, 3, 5, ...)
sum_odd_index = sum(lst[i] for i in range(1, len(lst), 2))

# 2. Сумма элементов между первым и последним отрицательными элементами
first_negative_index = next((i for i in range(len(lst)) if lst[i] < 0), -1)
last_negative_index = next((i for i in range(len(lst) - 1, -1, -1) if lst[i] < 0), -1)

if first_negative_index != -1 and last_negative_index != -1 and first_negative_index < last_negative_index:
    sum_between_negatives = sum(lst[first_negative_index + 1:last_negative_index])
else:
    sum_between_negatives = 0  # Если отрицательные элементы отсутствуют или их меньше двух

# 3. Сжатие списка
compressed_list = [x for x in lst if abs(x) > 1]
compressed_list += [0] * (len(lst) - len(compressed_list))  # Добавление нулей в конец

# Вывод результатов
print(f"Sum of elements with odd indices: {sum_odd_index}")
print(f"Sum of elements between the first and last negative elements: {sum_between_negatives}")
print(f"Compressed list: {compressed_list}")
