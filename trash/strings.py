# методы класса str для строковых объектов
# Преобразование первого символа в верхний регистр
s1 = 'abcd'
print(f'в строке {s1} с помощью метода .capitalize изменяем первую букву на заглавную')
S = s1.capitalize()
print(f'первая буква заглавная: ', S)
# Приведение символов в верхний регистр
S = s1.upper()
print(f'все буквы заглавные: ', S)
# метод .lower() преобразует символы строки в нижний регистр
print(f'\n Изменим строку {S}, теперь все символы переведены в нижний регистр: {S.lower()}')
# Подсчет вхождений заданной подстроки
# Задаем некоторую последовательность (в данном примере строку)
s2 = 'aabccccdeggghhhhf abbcccddeeeeeghfff'
m = input(f'\n введите искомую последовательность \n в строке {s2} : ')
S2 = s2.count(m)
print(f'в строке "{s2}" элементов "{m}"  встречается {S2} раз(раза)')
# проверка, оканчивается ли строка конкретной подстрокой
m = input('\n Далее проверим, оканчивается ли строка на како-то конкретный элемент? \n Введите искомую последовательность: ')
print('метод .endswith() возвращает True или False')
S3 = s2.endswith(m)
if S3:
    print(f'строка "{s2}" оканчивается на "{m}"')
else:
    print(f'строка "{s2}" не оканчивается на "{m}"')
# метод .find() отыскивает первое вхождение заданной подстроки
print('\n Теперь найдем где в строке впервые встречается заданный элемент, и есть ли он вообще')
m = input('введите искомую последовательность: ')
S4 = s2.find(m)
if S4 != -1:
    print(f'элемент "{m}" в строке "{s2}" имеет индекс: {S4}, \n т.е. по счету он на {S4+1} месте с начала строки')
else:
    print(f'искомого элемента "{m}" в строке "{s2}" нет')
# метод .rfind() отыскивает последнее вхождение заданной подстроки
print('\n Теперь найдем где в строке в последний раз встречается заданный элемент, и есть ли он вообще')
m = input('введите искомую последовательность: ')
S4 = s2.rfind(m)
if S4 != -1:
    print(f'элемент "{m}" в строке "{s2}" имеет индекс: {S4}, \n т.е. по счету он на {S4+1} месте с начала строки')
else:
    print(f'искомого элемента "{m}" в строке "{s2}" нет')
# проверяем, состоит ли строка только из букв и цифр или нет, а за одно и проверяем, состоит ли строка только из цифр или только из букв
m = input('\n Введите любую поледовательность символов: ')
S5 = m.isalnum()
if S5:
    print(f'строка {m} состоит только из букв или цифр')
    # метод .isalpha() проверяет, состоит ли строка только из алфавитных символов
    S6 = m.isalpha()
    if S6:
        print(f'строка {m} состоит только из букв')
    # метод .isdigit() проверяет, состоит ли строка только из цифр
    S6 = m.isdigit()
    if S6:
        print(f'строка {m} состоит только из цифр')
else:
    print(f'строка {m} содержит не только буквы или цифры')
# метод .islower() проверяет, являются ли все символы в строке символами нижнего регистра
m = input('\n Теперь проверим, являются ли все символы в строке символами нижнего регистра \n Введите любую поледовательность символов: ')
S7 = m.islower()
if S7:
    print(f'строка {m} состоит только из символов нижнего регистра')
else:
    print(f'строка {m} состоит не только из символов нижнего регистра')
# метод .isspace() проверяет, содержит ли данная строка только символы пробела или нет.
# возвращает True если все символы строки являются пробелами
m = input('\n Проверим, состоит ли строка только из пробелов? \n Введите любую поледовательность символов: ')
S8 = m.isspace()
if S8:
    print(f'строка {m} состоит только из пробелов')
else:
    print(f'строка {m} состоит не только из пробелов')
# метод .istitle() проверяет, являются ли первые символы всех слов символами верхнего регистра или нет.
m = input('\n Проверим, являются ли первые символы всех слов символами верхнего регистра? \n Введите несколько слов: ')
S9 = m.istitle()
if S9:
    print(f'слова {m} все начинаются с символов верхнего регистра')
else:
    print(f'в словах {m} есть слова начинающиеся с символов нижнего регистра')
# метод .isupper() проверяет, являются ли все символы строки символами верхнего регистра или нет.
m = input('\n Проверим, являются ли все символы строки символами верхнего регистра? \n Введите любую последовательность символов: ')
S10 = m.isupper()
if S10:
    print(f'в последовательности {m} все символы верхнего регистра')
else:
    print(f'в последовательности {m} есть символы нижнего регистра')
# метод .lstrip([chrs]) удаляет начальные пробельные символы или символы, перечисленные в аргументе chrs
# метод .rstrip([chrs]) удаляет конечные пробельные символы или символы, перечисленные в аргументе chrs (после нужного слова)
# метод .strip([chrs]) удаляет пробелы в начале и конце строки или символы, перечисленные в аргументе chrs
m = input('\n с помощью .lstrip([chrs]) удалим начальные пробельные символы \n введите слово, начиная с пробелов:')
m1 = m.lstrip()
print(f'\n метод .lstrip([chrs]) убрал все пробелы перед словом: {m1}')
m = input('\n Теперь с помощью .lstrip([chrs]) удалим указанные символы в начале строки \n введите любое слово:')
m1 = input('\n введите символы в начале слова, которые нужно убрать:')
m2 = m.lstrip(m1)
print(f'\n метод .lstrip([chrs]) убрал все заданные символы в слове: {m2}')
m = input('\n Теперь с помощью .strip([chrs]) удалим указанные символы в строке \n введите любое слово:')
m1 = input('\n введите символы, которые нужно убрать:')
m2 = m.strip(m1)
print(f'\n метод .strip([chrs]) убрал все заданные символы слева и справа: {m2}')
# метод .replace(old, new [,maxreplace]) замещает подстроку old на подстроку new
# [,maxreplace] - это число показывающее, сколько раз в строке нужно заменить старую подстроку новой,
# если его не указать, то заменятся все подстроки old на new
m = input('\n Теперь с помощью .replace(old, new [,maxreplace]) удалим указанные последовательности в строке \n введите любое слово:')
m1 = input('\n введите подстроку, которую нужно убрать:')
m2 = input('\n введите подстроку, которой нужно заменить:')
m3 = m.replace(m1, m2, 2)
print(f'\n метод .replace(old, new [,maxreplace]) убрал все заданные символы в слове (первые 2): {m3}')
# метод swapcase() приводит символы верхнего регистра к нижнему и наоборот
m = input('\n введите любое слово с буквами в верхнем и нижнем регистре:')
print(f'\n метод .swapcase() все символы в верхнем регистре и заменил их на символы в нижнем регистре и наоборот: {m.swapcase()}')
