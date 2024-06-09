from base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        return self.__width

    @property
    def get_height(self):
        return self.__height

    @property
    def get_x(self):
        return self.__x

    @property
    def get_y(self):
        return self.__y
    
    @width.setter
    def set_width(self,value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
           self.__width = value

    @height.setter
    def set_height(self,value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value   

    @x.setter
    def set_x(self,value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def set_y(self,value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height
    
    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self,*args.**kwargs):
        my_dict = {"width":self.__width,"height":self.__height,"x":self.__x,"y":self.__y}

    if __name__ == "__main__":

        r1 = Rectangle(10, 2)
        print(r1.id)

        r2 = Rectangle(2, 10)
        print(r2.id)

        r3 = Rectangle(10, 2, 0, 0, 12)
        print(r3.id)