#!/usr/bin/python3
from hat_output import Color, KnitDisplay

from time import sleep


def make_test_pattern(frst_c, sec_c, thrd_c, four_c):
    pattern = []
    test = [frst_c]*4+[sec_c]*4+[thrd_c]*4+[four_c]*4
    pattern.append(test)
    pattern.append(test)
    pattern.append(test)
    pattern.append(test)
    test2 = [sec_c]*4+[thrd_c]*4+[four_c]*4+[frst_c]*4
    pattern.append(test2)
    pattern.append(test2)
    pattern.append(test2)
    pattern.append(test2)
    test3 = [thrd_c]*4+[four_c]*4+[frst_c]*4+[sec_c]*4
    pattern.append(test3)
    pattern.append(test3)
    pattern.append(test3)
    pattern.append(test3)
    test4 = [four_c]*4+[frst_c]*4+[sec_c]*4+[thrd_c]*4
    pattern.append(test4)
    pattern.append(test4)
    pattern.append(test4)
    pattern.append(test4)

    return pattern


if __name__ == "__main__":
    front = Color(100, 100, 0)
    back = Color(0, 100, 100)
    red = Color(200, 0, 0)
    green = Color(0, 200, 0)
    blue = Color(0, 0, 200)
    yellow = Color(200, 200, 0)
    test = make_test_pattern(red, green, blue, yellow)

    display = KnitDisplay(test)

    while not display.at_end():
        sleep(2)
        display.move_on(1)
