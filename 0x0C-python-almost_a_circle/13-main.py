#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    squ1 = Square(10, 2, 1)
    print(squ1)
    squ1_dictionary = squ1.to_dictionary()
    print(squ1_dictionary)
    print(type(squ1_dictionary))

    squ2 = Square(1, 1)
    print(squ2)
    squ2.update(**squ1_dictionary)
    print(squ2)
    print(squ1 == squ2)

