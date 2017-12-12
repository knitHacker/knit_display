#!/usr/bin/python3
from hat_output import Color, KnitDisplay

from time import sleep


def make_spiral(front_color, back_color):
    pattern = []
    pattern.append([front_color]*20)
    pattern.append(([front_color]*8)+([back_color]*7)+([front_color]*5))
    pattern.append(([front_color]*6)+([back_color]*11)+([front_color]*3))
    pattern.append(([front_color]*5)+([back_color]*4)+([front_color]*5)+([back_color]*4)+([front_color]*3))
    pattern.append(([front_color]*4)+([back_color]*3)+([front_color]*9)+([back_color]*3)+([front_color]*1))
    pattern.append(([front_color]*3)+([back_color]*3)+([front_color]*3)
                   +([back_color]*5)+([front_color]*3)+([back_color]*3))
    pattern.append(([front_color]*3)+([back_color]*2)+([front_color]*3)
                   +([back_color]*7)+([front_color]*3)+([back_color]*2))
    pattern.append(([front_color]*2)+([back_color]*2)+([front_color]*3)
                   +([back_color]*3)+([front_color]*3)+([back_color]*3)
                   +([front_color]*2)+([back_color]*2))
    pattern.append(([front_color]*2)+([back_color]*2)+([front_color]*2)
                   +([back_color]*3)+([front_color]*5)+([back_color]*2)
                   +([front_color]*2)+([back_color]*2))
    pattern.append(([front_color]*2)+([back_color]*2)+([front_color]*2)
                   +([back_color]*2)+([front_color]*3)+([back_color]*1)
                   +([front_color]*2)+([back_color]*2)+([front_color]*2)
                   +([back_color]*2))
    return pattern


if __name__ == "__main__":
    front = Color(100, 100, 0)
    back = Color(0, 100, 100)
    spiral = make_spiral(front, back)

    display = KnitDisplay(spiral)

    while not display.at_end():
        sleep(2)
        display.move_on(1)
