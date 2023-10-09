class Car:
    pass

c = Car()
print(c, type(c))

class Room:
    number = 'Room 34' # атрибут класса (поле). По сути - это переменная
    floor = 4          # атрибут класса (поле)

r = Room()
r1 = Room()
print(r.number, r1.number)
print(r.floor, r1.floor)

# атрибуты можно менять

r.number = 12
r.floor = '5 floor'
print(r.number, r1.number)
print(r.floor, r1.floor)

# Внутри класса могут быть функции. Эти функции внутри класса называются МЕТОДАМИ

class Door:
    def open(self): #метод - это функция внутри класса.
        print('self is', self)
        print('Door is opened!')
        self.opened = True
d = Door()
d.open()
d1 = Door()
d1.open()

# Методы могут принимать параметры
class Terminal:
    def hello(self, user_name):
        print('self is the object itself', self)
        print('Hello, ', user_name)
t = Terminal()
t.hello('Nikita')
t.hello('Vova')

class Window:
    is_opened = False
    def open(self):
        self.is_opened = not self.is_opened # меняем состояние is_opened на противоположное
        print('Window is now', self.is_opened)
w = Window()
w1 =Window()

print('Initial state', w.is_opened, w1.is_opened)
w.open()
print('New state', w.is_opened, w1.is_opened)

# Конструктор = это такой метод, который вызывается тогда, когда мы создаем экземпляр класса
class TestClass:
    def __init__(self):
        print('Constructor is called!')
        print('Self is the object itself!', self)
        
t = TestClass()
t1 = TestClass()

# Конструктору можно передавать параметры
class Table:
    def __init__(self, nuber_of_legs): # количество ножек в данном примере мы никуда не сохраняем, позже обратится к нему мы не сможем
        print('New table has {} legs'.format(nuber_of_legs))
t = Table(4)
t1 = Table(3)

class Chair:
    def __init__(self, color):
        self.color = color # в данном примере мы сохраняем цвет стула в переменную.
c = Chair('green')
print(c, c.color)

# НАСЛЕДОВАНИЕ

class Parent:   #Родительский класс
    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'
    def do(self):
        print('Parent do(): {}'.format(self.value))
class Child(Parent): #Класс, для которого класс Parent является родительским
    def __init__(self):
        print('Child initrd')
        self.value = 'Child'
parent = Parent()
parent.do()
child = Child()
child.do()
class Calc():
    def __init__(self, number):
        self.number = number
    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)
    def calc_value(self):
        return self.number * 10 + 2
    def print_number(self, value_to_print):
        print('______________')
        print('Numbers is', value_to_print)
        print('______________')
class CalcExtraValue(Calc):
    def calc_value(self):
        return self.number - 100

c = Calc(3)
c.calc_and_print()
c1 = CalcExtraValue(3)
c1.calc_and_print()

# ИНКАПСУЛЯЦИЯ. Инкапсуляция позволяет скрывать реализацию методов, что делает их использование удобным и безопасным.

class Example:
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
        print ('{}{}{}'.format(self.a, self_b, self.__c))
    def call(self)
        print('Called!')
example = Example()
print('example.a')
print('example._b')
try:
    print('example.__c')
except AttributeError as ex:
    print(ex)
