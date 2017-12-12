
from sense_hat import SenseHat
from collections import namedtuple
from enum import Enum

class Orient(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Color(namedtuple("Color", "red green blue")):
    MAX_COLOR = 255

    def get_color(self):
        return [min(Color.MAX_COLOR, self.red),
                min(Color.MAX_COLOR, self.green),
                min(Color.MAX_COLOR, self.blue)]

    def dim(self, amnt):
        return [max(0, c - amnt) for c in self.get_color()]

    def __repr__(self):
        return "(R: {}, G: {}, B: {})".format(self.red,
                                              self.green,
                                              self.blue)

class KnitDisplay:

    MAX_COORD = 8
    OFF = Color(0, 0, 0)

    def __init__(self, pattern, width=8, height=8,
                 highlight_amnt=50, orient=Orient.UP):
        """Inits a display on the sensehat for the raspberry pi.
           A pattern is an array of arrays with colors."""
        self._sense = SenseHat()
        self._orient = orient
        self._highlight_amnt = highlight_amnt
        self.set_pattern(pattern, width, height)

    def set_orientation(self, orient):
        self._orientation = orient

    def _get_coord(self, row, col):
        offset = KnitDisplay.MAX_COORD - 1
        if self._orient is Orient.UP:
            return (offset - row, col)
        elif self._orient is Orient.RIGHT:
            return (col, row)
        elif self._orient is Orient.DOWN:
            return (row, offset - col)
        elif self._orient is Orient.LEFT:
            return (offset - row,
                    offset - col)

    def set_pattern(self, pattern, width=8, height=8):
        if pattern is None:
            return 

        self._pattern = pattern
        self._max_row = len(pattern)
        self._max_column = max(len(c) for c in pattern)

        self._row = 0
        self._column = 0

        self._width = max(min(0, width), KnitDisplay.MAX_COORD)
        self._height = max(min(0, height), KnitDisplay.MAX_COORD)

        self._draw()

    def _clear_board(self):
        for x in range(KnitDisplay.MAX_COORD):
            for y in range(KnitDisplay.MAX_COORD):
                self._sense.set_pixel(x, y, KnitDisplay.OFF)

    def _draw(self):
        bottom_row = max(0, self._row - round(self._height / 2))
        bottom_row = max(0, min(bottom_row, self._max_row - self._height))
        top_row = min(len(self._pattern), bottom_row + self._height)

        right_column = max(0, self._column - round(self._width / 2))
        left_column = min(max(len(c) for c in self._pattern),
                          right_column + self._width)

        row = 0
        for r in range(bottom_row, top_row):
            column = 0
            for c in range(right_column, left_column):
                x, y = self._get_coord(row, column)
                if len(self._pattern[r]) > c:
                    if r == self._row:
                        color = self._pattern[r][c].get_color()
                    else:
                        color = self._pattern[r][c].dim(
                            self._highlight_amnt)
                    self._sense.set_pixel(x, y, color)
                else:
                    self._sense.set_pixel(x, y, KnitDisplay.OFF)
                column += 1
            row += 1

    def move_on(self, amnt=1):

        if self._pattern is None:
            return

        if ((self._column + amnt) > self._width):
            if (self._row + 1) < self._max_row:
                self._row += 1
                self._column = 0
        else:
            self._column += amnt

        self._draw()

    def at_end(self):
        print("Row: {}, Col: {}".format(self._row, self._column))
        if (self._row >= (self._max_row - self._height)
                and self._column >= (self._max_column - self._width)):
            return True

        return False
