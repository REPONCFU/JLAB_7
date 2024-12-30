
# Ввод списка A из 10 элементов
A = [int(input(f"Enter element {i+1} of list A: ")) for i in range(10)]

# Нахождение суммы отрицательных элементов
negative_sum = sum(x for x in A if x < 0)

# Вывод результата
print(f"Sum of negative elements: {negative_sum}")
