import random
import collections
def daysofbirthday(k):
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
    #k = int(input('Введите количество человек в коллективе: '))
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
    #print(ko)
    return ko
###вводим день и проверяем корректность введенных данных (число от 1 до 365)
##proverka = False
##while proverka == False:
##    date = input('введите день в году по порядку: ')
##    if date.isdigit() is False:
##        print('Необходимо ввести номер дня только цифрами')
##    else:
##        if int(date) < 1 or int(date) > 356:
##            print('В году 365 дней, вы ввели недопустимое значение')
##        else:
##            date = int(date)
##            proverka = True
#определяем, что это будет за день (месяц и число)

#print(manthstr, day)
kol = {}
k = int(input('Введите количество человек в коллективе: '))
kol.update(daysofbirthday(k))
for name, bday in kol.items():
    print('Человек {0} родился {1}'.format(name, bday))
values = kol.values()
counter = collections.Counter(values)
print(dict(counter))
#sovpadenie = 0
#i = 0
#j = 0
#for a, b in kol.items():
#    if kol[i]