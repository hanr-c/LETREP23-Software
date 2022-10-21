from tkinter import *
from PIL import Image, ImageTk
import math
import time
import random
from global_funcs import *

class BaselineMaxDisplay(Canvas):

    def __init__(self, root, width, height, nwidth, nheight, margin=10, squareSide=20, colors=None, start_color=1, *args, **kw):
        super(BaselineMaxDisplay, self).__init__(root, width=width, height=height, *args, **kw)
        self._nwidth = nwidth
        self._nheight = nheight
        self.width = width
        self.height = height

        if colors is None:
            self.colors = ["red", "green", "gray", "yellow", "orange"]
        else:
            self.colors = colors

        self._bg = self.create_rectangle(0, 0, width, height)
        self.itemconfigure(self._bg, fill=self.colors[start_color], outline="")

        self._margin = margin
        self._squareSide = squareSide

        self._records = [0] * (nwidth * nheight)
        r = 0
        c = 0
        for i in range(nwidth * nheight):
            x = margin + c * (width  - margin * 2 - squareSide) / (nwidth)
            y = margin + r * (height - margin * 2 - squareSide) / (nheight)
            record = self.create_rectangle(x, y, x + squareSide, y + squareSide)
            self.itemconfigure(record, fill=self.colors[2])
            self._records[i] = record
            c += 1
            if c >= nwidth:
                c = 0
                r += 1

    def set_record(self, i, success):
        self.itemconfigure(self._records[i], fill=self.colors[success])
        self.itemconfigure(self._bg, fill=self.colors[success])

    def reset_record(self, i):
        self.itemconfigure(self._records[i], fill=self.colors[2])
    
    def reset_all(self):
        for i in range(self._nwidth * self._nheight):
            self.reset_record(i)
    
    def update_background(self, color_index):
        self.itemconfigure(self._bg, fill=self.colors[color_index])





class ControlSuccessRecordDisplay(Canvas):

    def __init__(self, root, width, height, nwidth, nheight, margin=10, radius=10, colors=None, start_color=1, *args, **kw):
        super(ControlSuccessRecordDisplay, self).__init__(root, width=width, height=height, *args, **kw)
        self._nwidth = nwidth
        self._nheight = nheight
        self.width = width
        self.height = height

        if colors is None:
            self.colors = ["red", "green", "gray", "yellow", "orange"]
        else:
            self.colors = colors

        self._bg = self.create_rectangle(0, 0, width, height)
        self.itemconfigure(self._bg, fill=self.colors[start_color], outline="")

        self._margin = margin
        self._radius = radius

        self._records = [0] * (nwidth * nheight)
        r = 0
        c = 0
        for i in range(nwidth * nheight):

           # if (nwidth * nheight) <= 30:
            x = margin + c * (width  - margin * 2 - radius * 2) / (nwidth)
            y = margin + r * (height - margin * 2 - radius * 2) / (nheight)
            record = self.create_oval(x, y, x + 2 * radius, y + 2 * radius)
            self.itemconfigure(record, fill=self.colors[2])
            self._records[i] = record
            c += 1
            if c >= nwidth:
                c = 0
                r += 1

    def set_record(self, i, success):
        self.itemconfigure(self._records[i], fill=self.colors[success])
        self.itemconfigure(self._bg, fill=self.colors[success])

    def reset_record(self, i):
        self.itemconfigure(self._records[i], fill=self.colors[2])
    
    def reset_all(self):
        for i in range(self._nwidth * self._nheight):
            self.reset_record(i)
    
    def update_background(self, color_index):
        self.itemconfigure(self._bg, fill=self.colors[color_index])


def main():
    root = Tk()
    nw = 15; nh = 5
    display = SuccessRecordDisplay(root, 650, 250, nw, nh, margin=15, radius=15)
    display.pack()
    i = 0

    center_window(root)
    while 1:
        time.sleep(1)
        display.set_record(i, random.randint(0, 1))
        i += 1
        if i == nw * nh:
            i = 0
            display.reset_all()
        root.update()

if __name__ == "__main__":
    main()

