#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    squ1 = Square(5)
    print(squ1)
    print(squ1.size)
    squ1.size = 10
    print(squ1)

    try:
        squ1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

