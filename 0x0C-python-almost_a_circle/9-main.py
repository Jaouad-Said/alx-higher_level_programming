#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    squ1 = Square(5)
    print(squ1)
    print(squ1.area())
    squ1.display()

    print("---")

    squ2 = Square(2, 2)
    print(squ2)
    print(squ2.area())
    squ2.display()

    print("---")

    squ3 = Square(3, 1, 3)
    print(squ3)
    print(squ3.area())
    squ3.display()

