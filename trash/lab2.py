# обёртка функций, декоратор, оно же принцип замыкания

def decorate_(original_function):
    """ декоратор (исходной функции)"""
    def wrapper(*args, **kwargs):
        """ обёртка и исполнение до, исходная функция, после"""
        print('-----что-то делаем перед вызовом функции-----')
        action = original_function(*args, **kwargs)
        print('-----что-то делаем после вызова функции-----')
        return action
    return wrapper


def transform_text(title, tag):
    """ исходная функция """
    print('title =', title, 'tag =', tag)
    return f'<{tag}>{title}</{tag}>'


#transform_text = decorate_(transform_text) # замыкание
#print(transform_text('Python навсегда','h1'))

def func_show(func):
    def print_result(*args, **kwargs):
        f = func(*args, **kwargs)
        print(f'Площадь прямоугольника: {f}')
        return f
    return print_result


@func_show
def get_sq(width, height):
    return width * height


#width = 10
#height = 20
#get_sq(width, height)

def show_menu(func):
    def inner(*args, **kwargs):
        l = func(*args, **kwargs)
        for n, i in enumerate(l):
            print(f'{n + 1}. {i}')
    return inner

#@show_menu
def get_menu(s):
    s1 = s.split()
    return s1

#s = input()
    
#print(get_menu(s))

def sort_list(func):
    def inner(*args, **kwargs):
        l = func(*args, **kwargs)
        return l.sort()
    return inner

#@sort_list
def get_list(s):
    s1 = sorted(list(map(int, s.split())))
    return s1

#l = input()
#print(get_list(l))

def lst_to_d(func):
    def inner(*args, **kwargs):
        d = {}
        l = func(*args, **kwargs)
        for i in range(len(l[0])):
            d[l[0][i]] = l[1][i]
        return d
    return inner
@lst_to_d
def strs_to_lst(s1, s2):
    l1 = list(s1.split())
    l2 = list(s2.split())
    return l1, l2
    
#s1 = input()
#s2 = input()

#print(strs_to_lst(s1, s2))


def tire_off(func):
    def inner(*args, **kwargs):
        l2 = []
        l = list(func(*args, **kwargs))
        count = 0
        for i in l:
            if i == '-' and count < 1:
                l2.append(i)
                count += 1
            elif i == '-' and count >= 1:
                count += 1
            else:
                l2.append(i)
                count = 0
        return ''.join(l2)
    return inner

@tire_off
def trans(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    s2 = []
    for i in s:
        if i.lower() in t:
            s2.append(t[i.lower()])
        elif i.lower() == ":" or i.lower() == "," or i.lower() == ";" or i.lower() == "_" or i.lower() == " ":
            s2.append('-')
        else:
            s2.append(i.lower())
    return ''.join(s2)


#s = input()
#print(trans(s))

#def sum_plus_val(start=5):
#    def sum_plus(func):
#        def wrapper(*args, **kwargs):
#            res = func(*args, **kwargs) + start
#            return res
#        return wrapper
#    return sum_plus

#@sum_plus_val(start=500)
#def num_from_s(s):
#    l = []
#    for i in s.split():
#        l.append(int(i))
#    return sum(l)

#s = input()
#print(num_from_s(s))

#def sum_plus_val(tag='h1'):
#    def sum_plus(func):
#        def wrapper(*args, **kwargs):
#            res = func(*args, **kwargs)
#            return f'<{tag}>{res}</{tag}>'
#        return wrapper
#    return sum_plus
#
#@sum_plus_val(tag='h1')
#def num_from_s(s):
#    return s.lower()
#
#s = input()
#print(num_from_s(s))

from functools import wraps

def sum_plus(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = sum(func(*args, **kwargs))
        return res
    return wrapper


@sum_plus
def get_list(s):
    """Функция для формирования списка целых значений"""
    l = []
    for i in s.split():
        l.append(int(i))
    return l

s = input()
print(get_list(s))