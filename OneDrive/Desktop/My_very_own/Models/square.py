from rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__size)
    
    @property
    def size_getter(self):
        return self.__width
    @size_getter.setter
    def size_setter(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        another_dict = {"id": self.__id, "size": self.__size, "x": self.__x, "y": self.__y}

    def to_dictionary(self):
        my_dict = {"id": self.id, "size": self.__size, "x": self.__x, "y": self.__y}
        return my_dict