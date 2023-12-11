#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rec1 = Rectangle(3, 5, 1)
    rec1_dictionary = rec1.to_dictionary()
    rec2 = Rectangle.create(**rec1_dictionary)
    print(rec1)
    print(rec2)
    print(rec1 is rec2)
    print(rec1 == rec2)

