class Point:
    __count = 0


    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
        Point.__count += 1

    @classmethod
    def count_points(cls):
        return cls.__count

    def move_to(self, x, y):
        self.__x = x
        self.__y = y

    def move_by(self, x, y):
        self.__x += x
        self.__y += y
    
    def __repr__(self) -> str:
        return f'Я - точка: {self.__x}x{self.__y}'
    
    # для x
    def get_x(self):
        return self.__x
    
    def set_x(self, value):
        self.__x = value
    x = property(get_x, set_x)
    
    # для y
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value




