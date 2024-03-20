class Node:
    def __init__(self, value, type):
        self.__value = value
        self.__type = type

    @property
    def value(self):
        return self.__value
    
    @property
    def type(self):
        return self.__type
