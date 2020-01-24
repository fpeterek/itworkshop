import turtle
import time
import math


# Nakreslit čáru
def line():
    t.forward(100)


# Nakreslit kruh
def circle():
    t.forward(100)


# Nakreslit přerušovanou čáru pomocí cyklu
def dashed_line():
    t.forward(100)


# Nakreslit trojúhelník, nejlépe pomocí cyklu
def triangle():
    t.forward(100)


# Nakreslit čtverec pomocí cyklu
def square():
    t.forward(100)


# Nakreslit šestiúhelník pomocí cyklu
def hexagon():
    t.forward(100)


# Nakreslit znak Audi pomocí cyklu, nejlépe pomocí cyklu
def audi():
    t.forward(100)


# Nakreslit logo Olympijských her, lze využít cyklu
def olympic_logo():
    t.forward(100)


# Nakreslit kruh pomocí cyklu (bez metody `circle`)
def custom_circle():
    t.forward(100)


# Nakreslit vlny
def wave():
    t.forward(100)


# Nakreslit vlny bez metody `circle`, nejlépe bez použití kódu z příkladu 8
def custom_wave():
    t.forward(100)


def test_all():
    functions = [
        line, circle, dashed_line, triangle, square, hexagon, audi,
        olympic_logo, custom_circle, wave, custom_wave
    ]

    for fun in functions:
        fun()
        time.sleep(1)
        t.reset()
        t.shape('turtle')


if __name__ == '__main__':
    t = turtle.Turtle()
    t.shape('turtle')
    test_all()
