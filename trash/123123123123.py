#h = int(input())
#m = int(input())
#t = int(input())
#t_without24 = (t + h * 60 + m) % 86400
#t_h = int(t_without24 // 60) % 24
#t_m = int(t_without24 - t_h * 60)  % 60
#print(f'{t_h:02}:{t_m:02}')

# km1 = int(input())
# km2 = int(input())
# speed = int(input())
# km = max(km1, km2) - min(km1, km2)
# print(round(km / speed, 2))

#n1 = int(input())
#n2 = input()
#print(n1 + int(n2, 2))

#n1 = int(input(), 2)
#n2 = int(input())
#print(n2 - n1)

#pos = input()
#coast = int(input())
#weght = int(input())
#cash = int(input())
#coast_all = f"{str(weght)}кг * {str(coast)}руб/кг"
#coast_itog = f"{weght * coast}руб"
#cash_in = f"{cash}руб"
#cash_out = f"{cash - weght * coast}руб"
#st1 = int(35 - 6 - len(pos))
#st2 = int(35 - 5 - len(coast_all))
#st3 = int(35 - 6 - len(coast_itog))
#st4 = int(35 - 8 - len(cash_in))
#st5 = int(35 - 6 - len(cash_out))
#print(f"{'Чек':=^35}")
#print(f"Товар:{' ' * st1}{pos}")
#print(f"Цена:{' ' * st2}{coast_all}")
#print(f"Итого:{' ' * st3}{coast_itog}")
#print(f"Внесено:{' ' * st4}{cash_in}")
#print(f"Сдача:{' ' * st5}{cash_out}")
#print('=' * 35)


# считывание списка из входного потока
#lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама, Колобок']
#i = 0
#print(len(lst_in))
#lst_out = []
#while i < len(lst_in):
#    if ' ' in lst_in[i]:
#        i += 1
#        continue
#    else:
#        lst_out.append(lst_in[i])
#    i += 1
#print(*lst_out)

#def em(s):
#    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890.@"
#    for i in s:
#        if i not in symbols:
#            return False
#    if s.count('@') != 1 or s.count('@') == 0:
#        return False
#    elif s[0] == '@' or s[0] == '.' or s[-1] == '@' or s[-1] == '.':
#        return False
#    elif '.' not in s[s.index('@'):]:
#        return False
#    else:
#        return True
#        
#l = list(input().split())
#l_out = list(filter(em, l))
#print(*l_out)
#ls = 'Москва Уфа Тула Самара Омск Воронеж Владивосток Лондон Калининград Севастополь'
#z = list(zip(*[iter(input().split())]*3))
#for i in z:
#    print(*i)

#class Translator:
#    def add(self, eng, rus):
#        if 'tr' not in self.__dict__:
#            self.tr = {}
#        self.tr.setdefault(eng, [])
#        if eng not in self.tr:
#            self.tr[eng] = [rus]
#        elif rus in self.tr[eng]:
#            self.tr[eng].append(rus)
#        else:
#            pass
#      
#    def remove(self, eng):
#        if eng in self.tr:
#            self.tr.pop(eng)
#        else:
#            pass
#
#    def translate(self, eng):
#      return self.tr[eng]

#tr = Translator()
#tr.add('tree', 'дерево')
#tr.add('car', 'машина')
#tr.add('car', 'автомобиль')
#tr.add('leaf', 'лист')
#tr.add('river', 'река')
#tr.add('go', 'идти')
#tr.add('go', 'ехать')
#tr.add('go', 'ходить')
#tr.add('milk', 'молоко')
#tr.add('milk', 'молоко')
#print(tr.__dict__)
#tr.remove('box')
#print(tr.__dict__)
#print(*tr.translate('car'))


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def is_triangle(self, a, b, c):
        print(type(a))
        if type(a) in (int, float) and type(b) in (int, float) and type(c) in (int, float):
            if a <= 0 or b <= 0 or c <= 0:
                return 1
            elif a >= c + b or b >= a + c or c >= a + b:
                return 2
            else:
                return 3
        else:
            return 1

a, b, c = map(int, input().split()) # эту строчку не менять

tr = TriangleChecker(a, b, c)
print(tr.is_triangle(a, b, c))
print(tr.is_triangle('3', 4, 5))