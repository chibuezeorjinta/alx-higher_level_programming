#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(qw, dd, fe, 110)
    print(r1)

    r1.update(89)
    print(r1)


    r1.update(89, 2, 3, 4, 5)
    print(r1)
