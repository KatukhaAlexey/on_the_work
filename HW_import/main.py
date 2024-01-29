from application.salary import calculate_salary
from application.db.people import get_employees
from color50 import rgb, constants


if __name__ == '__main__':
    y = int(input('Введите год начала работы сотрудника: '))
    m = int(input('Введите месяц начала работы сотрудника: '))
    d = int(input('Введите день приема на работу сотрудника: '))
    s = int(input('Введите среднюю зарплату сотрудника за один день: '))
    print(f'Зарплата за проработанное время: {calculate_salary(y, m, d, s)} рублей')
    my_color = rgb(128, 0, 128)
    print(my_color + get_employees('Вася') + constants.RESET)
