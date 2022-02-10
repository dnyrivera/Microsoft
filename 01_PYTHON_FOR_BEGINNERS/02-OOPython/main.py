class Elevator:
    def __init__(self, starting_floor):
        self.make = "The elevator company"
        self.floor = starting_floor


# To create the object

elevator = Elevator(1)
print(elevator.make)  # "The Elevator company"
print(elevator.floor)  # 1


class Square:
    def __init__(self):
        self.height = 2
        self.width = 2

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side


square = Square()
square.height = 3  # not a square anymore

# PROTECTED ATRIBUTES
class Square:
    def __init__(self):
        self._height = 2
        self._width = 2

    def set_side(self, new_side):
        self._height = new_side
        self._width = new_side


square = Square()
square._height = 3  # not a square anymore

# PRIVATED ATRIBUTES
class Square:
    def __init__(self):
        self.__height = 2
        self.__width = 2

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side


square = Square()
square.__height = 3  # raises AttributeError

square = Square()
square._Square__height = 3  # is allowed

# GETTERS AND SETTERS
class Square:
    def __init__(self):
        self.__height = 2
        self.__width = 2

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    def get_height(self):
        return self.__height

    def set_height(self, h):
        if h >= 0:
            self.__height = h
        else:
            raise Exception("value needs to be 0 or larger")


square = Square()
square.__height = 3  # raises AttributeError

# DOCORATORS
class Square:
    def __init__(self, w, h):
        self.height = h
        self.__width = w

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_value):
        if new_value >= 0:
            self.__height = new_value
        else:
            raise Exception("Value must be larger than 0")
