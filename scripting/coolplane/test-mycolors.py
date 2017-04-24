""" test-mycolors.py | Thu, Mar 30, 2017 | Roman S. Collins

    A test for my color library.

"""
import random
from mycolors import *
from turtle import *

def draw_shape(size):
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)

    end_fill()

def colset(col):
    color(col, col)
    pencolor(col)
    fillcolor(col)

def main():
    speed(9e10)

    size = 10
    pensize(size)

    freq = .3
    c, w = 120, 120

    width = window_width()
    height = window_height()

    x = -(width/2)
    y = (height/2)

    penup()
    setposition(-(width/2), (height/2))
    pendown()

    col = float_rgb_color(freq, freq, freq, 0, 2, 4, c, w)

    i = 0
    posi = list(position())
    while posi[1] < 900:
        i += 1
        if i > (len(col) - 1):
            i = 0

        colset(col[i])
        draw_shape(size)
        #forward(size)

        penup()
        forward(size)
        pendown()

        posi = list(position())
        print(posi)

        if posi[0] > 480:
            y -= size
            penup()
            setposition(x, y)
            pendown()

    wait = input()

if __name__ == "__main__":
    main()
