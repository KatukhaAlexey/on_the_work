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

n = int(input())
kol = 1
t = 0
while t < n:
    if t % 3 == 0 and t != 0:
        kol *= 2
    t += 1
print(kol)