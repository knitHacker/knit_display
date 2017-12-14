#!/usr/bin/python3
from knit_display import Color, KnitDisplay
from sense_hat import SenseHat
from time import sleep

SENSE_HAT_DISPLAY = SenseHat()

def two_color(col_a, col_b, pattern):
    knit_pattern = []
    curr_col = col_a
    next_col = col_b
    for row in pattern:
        row_pattern = []
        curr_col = col_a
        next_col = col_b
        for changes in row:
            row_pattern.extend([curr_col]*changes)
            tmp_col = curr_col
            curr_col = next_col
            next_col = tmp_col
        knit_pattern.append(row_pattern)

    return knit_pattern
            
SPIRAL = [[20],
          [8, 7, 5],
          [6, 11, 3],
          [5, 4, 5, 4, 2],
          [4, 3, 9, 3, 1],
          [3, 3, 3, 5, 3, 3],
          [3, 2, 3, 7, 3, 2],
          [2, 2, 3, 3, 3, 3, 2, 2],
          [2, 2, 2, 3, 5, 2, 2, 2],
          [2, 2, 2, 2, 3, 1, 2, 2, 2, 2],
          [2, 2, 2, 2, 2, 2, 2, 1, 3, 2],
          [2, 2, 2, 2, 2, 2, 5, 3],
          [1, 3, 2, 2, 2, 3, 3, 3, 1],
          [1, 3, 2, 2, 3, 7, 2],
          [0, 4, 3, 2, 3, 5, 3],
          [0, 5, 2, 3, 9, 1],
          [0, 5, 3, 4, 5, 3],
          [0, 1, 1, 4, 2, 12],
          [3, 3, 3, 11],
          [4, 3, 3, 9, 1],
          [1, 1, 3, 3, 3, 7, 2],
          [0, 3, 3, 3, 3, 5, 3],
          [0, 4, 3, 3, 3, 3, 3, 1],
          [0, 1, 1, 3, 3, 3, 3, 3, 3],
          [3, 3, 3, 3, 3, 3, 2],
          [2, 3, 3, 5, 3, 3, 1],
          [1, 3, 3, 3, 1, 3, 3, 3],
          [0, 3, 3, 3, 3, 3, 3, 2],
          [0, 2, 3, 3, 5, 3, 3, 1],
          [0, 1, 3, 3, 3, 1, 3, 3, 3],
          [3, 3, 3, 3, 3, 3, 2],
          [2, 3, 3, 5, 3, 3, 1],
          [1, 3, 3, 3, 1, 1, 3, 3, 2],
          [0, 3, 3, 3, 5, 3, 3],
          [0, 4, 3, 3, 3, 3, 3, 1],
          [0, 1, 1, 3, 3, 3, 1, 3, 3, 2],
          [3, 3, 3, 5, 3, 3],
          [4, 3, 3, 3, 3, 3, 1],
          [1, 1, 3, 3, 3, 1, 3, 3, 2],
          [0, 3, 3, 3, 5, 3, 3],
          [0, 4, 3, 3, 3, 3, 3, 1],
          [0, 1, 1, 3, 3, 3, 3, 3, 3],
          [3, 3, 3, 3, 3, 3, 2],
          [2, 3, 5, 3, 3, 3, 1],
          [1, 3, 7, 3, 3, 3],
          [0, 3, 9, 3, 3, 2],
          [0, 2, 11, 3, 3, 1],
          [0, 1, 13, 2, 4],
          [5, 5, 4, 3, 3],
          [3, 9, 3, 2, 3],
          [2, 3, 5, 3, 2, 3, 2],
          [1, 3, 7, 3, 2, 2, 2],
          [1, 2, 3, 3, 3, 2, 2, 2, 2],
          [0, 2, 3, 5, 2, 2, 2, 2, 2],
          [0, 2, 2, 3, 1, 2, 2, 2, 2, 2, 2],
          [0, 2, 2, 2, 2, 2, 1, 3, 2, 2, 2],
          [0, 2, 2, 2, 2, 5, 3, 2, 2],
          [0, 2, 2, 2, 3, 3, 3, 2, 3],
          [0, 2, 2, 3, 7, 3, 2, 1],
          [0, 2, 3, 3, 5, 3, 3, 1],
          [0, 3, 3, 9, 3, 2],
          [0, 4, 4, 5, 4, 3],
          [0, 5, 11, 4],
          [0, 7, 7, 6],
          [0, 20]]           


def main():
    front = Color(0, 0, 100)
    back = Color(0, 100, 0)
    spiral_pat = two_color(front, back, SPIRAL)

    for row in spiral_pat[::-1]:
        stitches = []
        for stitch in row:
            if stitch == front:
                stitches.append("*")
            elif stitch == back:
                stitches.append(" ")
        print(" | ".join(stitches))

    display = KnitDisplay(spiral_pat, SENSE_HAT_DISPLAY)

    @display.clear_when_done
    def run():
        while not display.at_end():
            sleep(0.1)
            display.move_on(1)
 
    run()

if __name__ == "__main__":
    main()
