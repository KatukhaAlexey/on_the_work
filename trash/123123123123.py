def sort_of_list(l):
    # сортировка списка методом пузырька
    kol_of_elements = len(l)
    # переменная kol_of_elements - количество элементов в последовательности
    # Для сортировки все элементы последовательности должны быть типа int или float
    for i in range(kol_of_elements - 1):
        for j in range(kol_of_elements - i - 1):
            if l[j] > l [j+1]:
                l[j], l[j+1] = l[j + 1], l[j]
    return l

N = int(input('Введите количество элементов последовательности: '))
l = []
for i in range(N - 1):
    l.append(int(input('Введите число последовательности: ')))
print('Вы ввели следующую последовательность: ', l)
print('Эта же последовательность, только отсортированная по возврастанию:', sort_of_list(l))
