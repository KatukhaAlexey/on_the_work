from application.salary import *
from application.db.people import *
import color50

if __name__ == '__main__':
    y = int(input('Введите год начала работы сотрудника: '))
    m = int(input('Введите месяц начала работы сотрудника: '))
    d = int(input('Введите день приема на работу сотрудника: '))
    s = int(input('Введите среднюю зарплату сотрудника за один день: '))
    print(f'Зарплата за проработанное время: {calculate_salary(y, m, d, s)} рублей')
    my_color = color50.rgb(128, 0, 128)
    print(color50.my_color + get_employees('Вася') + color50.constants.RESET)
