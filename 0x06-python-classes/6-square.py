#!/usr/bin/python3

"""Defines a square class"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square
        Args:
            size (int): The size of the new square
            position (int, int): The position of the new square
        """
        self.__size = size
        self.__position = position
    @property
    def size(self):
        """Get the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with the # character"""
        if self.__size > 0:
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print("")
