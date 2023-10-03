# ..................коментарий............
name = input('Введите Ваше имя: ')
age = input('Сколько Вам лет? ')
#greet = 'Привет, ' + name + '! '
#greet += 'Тебе ' + age + ' лет.'
greet = 'Привет, {}. Тебе {} лет.'.format(name, age)
print(greet)