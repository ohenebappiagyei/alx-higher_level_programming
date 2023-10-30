#!/usr/bin/python3
"""
This module defines the Rectangle class with private attributes,
properties, methods for calculating area and perimeter,
and  custom __str__ and __repr__ methods, and a custom __del__ method
for deletion messages, and a class attribute for tracking the number of
instances and the print symbol, and a static method for comparing rectangles
based on area and a class method that returns a new Rectangle instance with
width, height and size as the same.
"""


class Rectangle:
    """
    A class that represents a rectangle.
    """
    # Class attribute for tracking instances
    number_of_instances = 0
    # Class attribute for print symbol
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.
        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1  # Increment instances count

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.
        Args:
            value (int): The value to set as the width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.
        Args:
            value (int): The value to set as the height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Custom __str__ method to print the rectangle with '#'.
        If width or height is 0, return an empty string.
        Returns:
            str: The string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Custom __repr__ method to return a string representation of the object.
        This representation can be used with eval() to recreate a new instance.
        Returns:
            str: The string representation of the object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Custom __del__ method to print a deletion message.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instances count

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to compare two rectangles based on their area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.


        Returns:
            Rectangle: The rectangle with the bigger area, or rect_1 if they are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instanc eof Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a square rectangle with equal width and height.

        Args:
            cls (class): The class itself (Rectangle).
            size (int): The size of the square.

        Returns:
            Rectangle: A new Rectangle instance representing a square.
        """
        return cls(size, size)
