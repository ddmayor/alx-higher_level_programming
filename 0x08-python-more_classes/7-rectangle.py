#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """Return the printable representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for x in range(self.__height):
            [rect.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self) -> str:
        """Return string rep of a rectangle"""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """print message for deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
