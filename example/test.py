#!/usr/bin/python3
from knit_display import Color, KnitDisplay
from sense_hat import SenseHat
from time import sleep

SENSE_HAT_DISPLAY = SenseHat()

def make_test_pattern(frst_c, sec_c, thrd_c, four_c):
    pattern = []
    test = [frst_c]*4+[sec_c]*4+[thrd_c]*4+[four_c]*4
    pattern.append(test)
    pattern.append(test)
    pattern.append(test)
    pattern.append(test)
    test2 = [four_c]*4+[frst_c]*4+[sec_c]*4+[thrd_c]*4
    pattern.append(test2)
    pattern.append(test2)
    pattern.append(test2)
    pattern.append(test2)
    test3 = [thrd_c]*4+[four_c]*4+[frst_c]*4+[sec_c]*4
    pattern.append(test3)
    pattern.append(test3)
    pattern.append(test3)
    pattern.append(test3)
    test4 = [sec_c]*4+[thrd_c]*4+[four_c]*4+[frst_c]*4
    pattern.append(test4)
    pattern.append(test4)
    pattern.append(test4)
    pattern.append(test4)

    return pattern

def main():
    front = Color(80, 80, 0)
    back = Color(0, 80, 80)
    red = Color(160, 0, 0)
    green = Color(0, 160, 0)
    blue = Color(0, 0, 160)
    yellow = Color(160, 160, 0)
    test = make_test_pattern(red, green, blue, yellow)

    display = KnitDisplay(test, SENSE_HAT_DISPLAY)

    @display.clear_when_done
    def run():
        while not display.at_end():
            sleep(1)
            display.move_on(1)

    run()


if __name__ == "__main__":
    main()
