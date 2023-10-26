word = input()
lst = list(word)
centr = int(len(lst) // 2)
if lst[:centr] == lst[len(lst):centr:-1]:
    print('Да')
else:
    print('Нет')
    print(lst[:centr])
    print(lst[len(lst):centr:-1])