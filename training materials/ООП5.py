# __setattr__(self, key,value) - автоматически вызывается при изменении свойств key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойств класса с именем item
# Без return возвращает None. 
# __getattr__(self, item) - автоматически вызывается при получении несуществующего свойства item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойства item (не важно: существует оно или нет)

from typing import Any


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if MIN_COORD <= x <= MAX_COORD:
            self.x = x
            self.y = y

    # Для изменения атрибутов класса создадим метод класса
    #@classmethod
    #def set_bound(cls, left):
    #    cls.MIN_COORD = left

    def __getattribute__(self, __name: str) -> Any:
        print('__getattridute__')
        return object.__getattribute__(self, item)
    
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('Недопустимое имя арибута')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
    
    def __delattr__(self, item) -> None:
        print('__delattr__' + item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
#pt1.z = 1
#pt1.set_bound(-100)
#print(pt1.MIN_COORD)
