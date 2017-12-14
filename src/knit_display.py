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
        new_color = [max(0, c - amnt) for c in self]
        return Color(*new_color)

    def __eq__(self, other):
        return (other
                and self.red == other.red
                and self.green == other.green
                and self.blue == other.blue)

    def __repr__(self):
        return "(R: {}, G: {}, B: {})".format(self.red,
                                              self.green,
                                              self.blue)


class KnitDisplay:

    MAX_COORD = 8
    OFF = Color(0, 0, 0)

    def __init__(self, pattern, display, width=8, height=8,
                 highlight_amnt=50, orient=Orient.UP):
        """Inits a display on the sensehat for the raspberry pi.
           A pattern is an array of arrays with colors."""
        self._display = display
        self._orient = orient
        self._highlight_amnt = highlight_amnt
        self._output_buffer = []
        for x in range(KnitDisplay.MAX_COORD):
            tmp_row = []
            for y in range(KnitDisplay.MAX_COORD):
                tmp_row.append(KnitDisplay.OFF)
            self._output_buffer.append(tmp_row)

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

    def clear_display(self):
        for x in range(KnitDisplay.MAX_COORD):
            for y in range(KnitDisplay.MAX_COORD):
                self._set_point(x, y, KnitDisplay.OFF)

    def _draw(self):
        bottom_row = max(0, self._row - round(self._height / 2))
        bottom_row = max(0, min(bottom_row, self._max_row - self._height))
        top_row = min(len(self._pattern), bottom_row + self._height)

        right_column = max(0, self._column - round(self._width / 2))
        right_column = max(0, min(right_column,
                                  self._max_column - self._width))
        left_column = min(self._max_column,
                          right_column + self._width)

        row = 0
        for r in range(bottom_row, top_row):
            column = 0
            for c in range(right_column, left_column):
                x, y = self._get_coord(row, column)
                if len(self._pattern[r]) > c:
                    color = self._pattern[r][c]
                    if r == self._row and c == self._column:
                        self._set_point(x, y, color)
                    else:
                        self._set_point(x, y, color.dim(self._highlight_amnt))
                else:
                    self._set_point(x, y, KnitDisplay.OFF)
                column += 1
            row += 1

    def _set_point(self, x, y, color, dim_amnt=0):
        rgb = color.get_color()
        if self._output_buffer[x][y] != color:
            self._output_buffer[x][y] = color
            self._display.set_pixel(x, y, rgb)

    def move_on(self, amnt=1):

        if self._pattern is None:
            return

        if ((self._column + amnt) > self._max_column):
            if (self._row + 1) < self._max_row:
                self._row += 1
                self._column = 0
        else:
            self._column += amnt

        self._draw()

    def at_end(self):
        if (self._row == (self._max_row - 1)
                and self._column == (self._max_column - 1)):
            return True

        return False


    def clear_when_done(self, display_func):
        def wrapper(*args, **kwargs):
            try:
                display_func(*args, **kwargs)
            except (KeyboardInterrupt, Exception) as e:
                print(e)
            finally:
                self.clear_display()
        return wrapper


