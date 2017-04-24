""" mycolors.py | Wed, Mar 29, 2017 | Roman S. Collins

    Python script that returns a list of colors to
    import into the main coolplane.py script.

    https://krazydad.com/tutorials/makecolors.php

    Oh boy... here goes

"""
import math

# Float rgb
def float_rgb_color(frequency1, frequency2, frequency3,
                phase1, phase2, phase3, center=128,
                width=127, length=50
               ):
    myrainbow = []

    for i in range(length):
        r = abs(math.sin((frequency1 * i + phase1)) * (width + center))
        g = abs(math.sin((frequency2 * i + phase2)) * (width + center))
        b = abs(math.sin((frequency3 * i + phase3)) * (width + center))

        # Convert to float RGB
        r /= 255
        g /= 255
        b /= 255

        myrainbow.append((r, g, b))

    return myrainbow

# Non-float rgb
def rgb_color(frequency1, frequency2, frequency3,
                phase1, phase2, phase3, center=128,
                width=127, length=50
               ):
    myrainbow = []

    for i in range(length):
        r = abs(int(math.sin((frequency1 * i + phase1)) * (width + center)))
        g = abs(int(math.sin((frequency2 * i + phase2)) * (width + center)))
        b = abs(int(math.sin((frequency3 * i + phase3)) * (width + center)))

        myrainbow.append((r, g, b))

    return myrainbow

def main():
    myrainbow = gimme_color(.3, .3, .3, 0, 2, 4)

    for i in myrainbow:
        print(i)

if __name__ == "__main__":
    main()

