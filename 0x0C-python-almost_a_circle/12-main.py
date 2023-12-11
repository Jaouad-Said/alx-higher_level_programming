#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rec1 = Rectangle(10, 2, 1, 9)
    print(rec1)
    rec1_dictionary = rec1.to_dictionary()
    print(rec1_dictionary)
    print(type(rec1_dictionary))

    rec2 = Rectangle(1, 1)
    print(rec2)
    rec2.update(**rec1_dictionary)
    print(rec2)
    print(rec1 == rec2)

