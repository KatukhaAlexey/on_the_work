class Point:
    def __init__(self, x=0, y=0) -> None:
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x # переменные с двумя подчеркиваниями - приватные
            self.__y = y

    @classmethod
    def __check_value(cls, x): # Приватный метод. Метод класса. Проверяем вводимые данные, чтобы они были числами
        return type(x) in (int, float)


    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):  # Проверка на то, что x и y - это числа
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами') # Генерация исключения
        
    def get_coord(self):
        return self.__x, self.__y
    
pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())