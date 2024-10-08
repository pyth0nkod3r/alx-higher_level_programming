#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Represents a square
    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """Initializes a new square
        Args:
            size (int): The size of the new square
        """
        self.__size = size

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

    def area(self):
        """Return the current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character"""
        if self.__size > 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
