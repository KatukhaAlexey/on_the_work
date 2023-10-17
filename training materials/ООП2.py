# Создавать новые атрибуты в классе: ИмяКласса.имя_атрибута = значение_атрибута
# Тоже самое можно делать с помощью специальной функции
# setattr(ИмяКласса, имя_атрибута, значение_атрибута)  setattr(Point, 'prop', 1)
# Она создает новый атрибут в указанном пространстве имен (в данном случае в классе Point) с заданным значением.
# Если эту функцию применить к уже существующему атрибуту, то оно будет изменено на новое значение.
# getattr(Point, 'prop', False) - функция для взятия значения атрибута. Третий аргумент - возвращаемое значение,
# если атрибут не будет найден.
# hassttr(Point, 'prop') - проверяет наличие атрибута
# delattr(Point, 'prop') - удаляет указанный атрибут

class Lamp:
    '''Класс лампочка'''
    brand = 'Phillips' # Атрибут класса
    count = 0 # Можно подсчитывать количество лампочек
    def __init__(self, floor=0): # ИНИЦИАЛИЗАТОР
        self.__state = False
        self.__floor = floor
        Lamp.count += 1 # При создании объекта вызывается __init__ где и идет подсчет количества объектов
        print('Создана лампочка ' + Lamp.brand)
    def get_state(self):
        return self.__state
    state = property(get_state)
    def get_foor(self):
        return self.__floor
    def set_floor(self, value):
        self.__floor = value
    floor = property(get_foor, set_floor)
    
    @classmethod
    def foo(cls):
        cls.count

    def switch_on(self):
        if not self.state:
            self.state = True
            print('Лампочку включили')
    def switch_off(self):
        if self.state:
            self.state = False
            print('Лампочку выключили')
    def __repr__(self):
        return f'Я - лампочка на {self.floor} этаже'

lamp1 = Lamp(1)
print(lamp1.state)
print(Lamp.__doc__)
