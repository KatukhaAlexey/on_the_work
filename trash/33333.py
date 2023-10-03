import random
import collections
calendar = {
    'январь' : 31,
    'февраль' : 28,
    'март' : 31,
    'апрель' : 30,
    'май' : 31,
    'июнь' : 30,
    'июль' : 31,
    'август' : 31,
    'сентябрь' : 30,
    'октябрь' : 31,
    'ноябрь' : 30,
    'декабрь' : 31}
manths = {
    1 : 'январь',
    2 : 'февраль',
    3 : 'март',
    4 : 'апрель',
    5 : 'май',
    6 : 'июнь',
    7 : 'июль',
    8 : 'август',
    9 : 'сентябрь',
    10 : 'октябрь',
    11 : 'ноябрь',
    12 : 'декабрь'}
ko = {}
k = int(input('Введите количество человек в коллективе: '))
for m in range(1, k + 1):
        date = random.randint(1,366)
        manth = 0
        day = 0
        i=0
        while i < date :
            manth += 1
            i1 = i
            for j in range(1, int(calendar.get(manths.get(manth)))+1):
                if i < date :
                   i +=1
        manthstr = manths.get(manth)
        day = i - i1
        kol = str(manthstr) + ' ' + str(day)
        ko[m] = kol
print(ko)