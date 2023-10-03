# def seconds_per_day(days=1): #функция. значение по умолчанию 1
#     s = 24 * days * 60 * 60
#     return s #То, что функция возвращает
# sec = seconds_per_day(5)
# print(sec)
# def area_of_disk(radius):
#     return 3.14 * float(radius) ** 2
# p = area_of_disk(2)
# print(p)
# outer = input('Введите радиус внешнего круга ')
# inner = input('Введите радиус внутреннего круга ')
# def area_of_ring(outer, inner):
#     return area_of_disk(outer) - area_of_disk(inner)
# ss = area_of_ring(outer, inner)
# print(ss)
# def fn(*params): в данной функции * говорит о том, что функция может принимать не ограниченное количество параметров (контент)
# def fn(a, b=5, c=10) параметры b и c не обязательные, по умолчанию принимают значения 5 и 10. Вызвать функцию можно
# явно указав те параметры, которые нужно передать fn(c=100, a=500). Порядок не важен, если параметры поименованы
sequence = [1, 2, 7, 19]

# Сравните:
idx = 0
for item in sequence:
    print(idx)
    idx += 1

# и
for idx, item in enumerate(sequence):
    print(idx, item)