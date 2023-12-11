#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    squ1 = Square(5)
    print(squ1)

    squ1.update(10)
    print(squ1)

    squ1.update(1, 2)
    print(squ1)

    squ1.update(1, 2, 3)
    print(squ1)

    squ1.update(1, 2, 3, 4)
    print(squ1)

    squ1.update(x=12)
    print(squ1)

    squ1.update(size=7, y=1)
    print(squ1)

    squ1.update(size=7, id=89, y=1)
    print(squ1)

