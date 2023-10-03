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
#вводим день и проверяем корректность введенных данных (число от 1 до 365)
proverka = False
while proverka == False:
    date = input('введите день в году по порядку: ')
    if date.isdigit() is False:
        print('Необходимо ввести номер дня только цифрами')
    else:
        if int(date) < 1 or int(date) > 356:
            print('В году 365 дней, вы ввели недопустимое значение')
        else:
            date = int(date)
            proverka = True
#определяем, что это будет за день (месяц и число)
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
print(manthstr, day)
 
        