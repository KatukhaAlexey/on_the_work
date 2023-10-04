'''
Модуль random используется для генерации случайных чисел
'''
import random
# random.random() -случайное число от 0 до 1
print(f'Случайное число от 0 до 1 random.random(): {random.random()}')
# random.randint(A,B) случайное целое число N, A<=N<=B
print(f'Случайное целое число от А до В random.randint(): {random.randint(0, 10)}')
# random.randrange(start, stop, step) возвращает случайное число из последовательности
print(f'Случайное целое число из последовательности random.randrange(start, stop, step): {random.randrange(0, 10, 2)}')
list1 = [55, 66, 77, 88, 99]
print(f'random.choice используется для выбора случайного элемента из списка, {random.choice(list1)}')
# random.sample(population, k) используется, когда требуется выбрать несколько элементов из заданной последовательности population
print(f'random.sample(population, k) выбирает случайные элементы из списка, {random.sample(list1, 3)}')
# random.choices(population, weights=None, *, cum_weights=None, k=1)
# Метод используется, когда требуется выбрать несколько случайных элементов из заданной последовательности.
# Он позволяет повторно выбирать один и тот же элемент
print(f'random.choices(population, k=n) выбирает случайные элементы из списка, {random.choices(list1, k=3)}')
# random.shuffle() применяется для расстановки элементов последовательности в случайном порядке
print(f'Так выглядит данный нам список: {list1}')
random.shuffle(list1)
print(f'А так выглядит список после применения метода random.shuffle(): {list1}')
# random.uniform(A,B) случайное число с плавающей точкой N, A<=N<=B
print(f'Случайное число с плавающей точкой от А до В random.uniform(): {random.uniform(0.34, 10.99)}')
'''
Случайные числа, полученные при помощи модуля random в Питоне, не являются криптографически устойчивыми. 
Это означает, что криптоанализ позволяет предсказать какое число будет сгенерировано следующим.
'''