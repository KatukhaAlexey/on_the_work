# Циклы
# while True: pass - безконечный цикл. Пока i не станет равным какомуто значению, выполнять цикл.
i=0
while i<5:
    print(i)
    i+=1
# Цикл выводит переменную i пока она не станет равной 5
i=0
while i<5:
    if i==3:
        break #прерывает цикл, если значение переменной станет равной 3
    print(i)
    i+=1
i=0
while i<5:
    i+=1
    if i==3:
        continue #не прерывая выполнения всего цикла, пропускается только один ход
    print(i)