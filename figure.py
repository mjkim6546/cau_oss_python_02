import math

class Line:
    __length=1
    def __init__(self, length):
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
        else:
            self.__length = 1
    
    def set_length(self, length):
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length

    def get_length(self):
        return self.__length

def area_square(a):
    if not isinstance(a, Line):
        return 0
    return a.get_length() ** 2

def area_circle(a):
    if not isinstance(a, Line):
        return 0
    return a.get_length() ** 2 * math.pi

def area_regular_triangle(a):
    if not isinstance(a, Line):
        return 0
    return a.get_length() ** 2 * math.sqrt(3) / 4