import random
month = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь', 11:'ноябрь', 12:'декабрь'}
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
birthdays = {}
for i in range(1, 24):
    monthofbirthday = int(random.randrange(1,13))
    dayofbirthday = int(random.randrange(1, days_in_month[monthofbirthday]+1))
    para = str(month[monthofbirthday]) + ' ' + str(dayofbirthday)
    birthdays[i] = para
    print(birthdays[i])

    
