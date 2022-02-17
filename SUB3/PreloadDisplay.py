from tkinter import *
from PIL import Image, ImageTk
import math

high_image_dir = 'C:/Program Files/LETREP2/resources/HighImage.png'
low_image_dir = 'C:/Program Files/LETREP2/resources/LowImage.png'
good_image_dir = 'C:/Program Files/LETREP2/resources/GoodImage.png'

class PreloadDisplay(Canvas):



    def __init__(self, root, width, height, max, min, *args, **kw):
        super(PreloadDisplay, self).__init__(root, width=width, height=height, *args, **kw)
        self.width = width
        self.height = height
        self.preload_max = max
        self.preload_min = min

        self._bg = self.create_rectangle(0, 0, width, height, fill="#0ed145")
        self.high_image = Image.open(high_image_dir)
        self.low_image  = Image.open(low_image_dir)
        self.good_image = Image.open(good_image_dir)
        self._high = self.create_image(100, 50, image=ImageTk.PhotoImage(self.high_image))
        self._low  = self.create_image(100, 50, image=ImageTk.PhotoImage(self.low_image))
        self._good = self.create_image(100, 50, image=ImageTk.PhotoImage(self.good_image))


        # animation constants
        self._dx = 7
        self._dy = 70 / 200 * width
        self._r = 0.5 * (self._dy**2 / self._dx - self._dx)
        # self._r *= width / 200
        self._thetamax = math.asin(self._dy / self._r)
        self._a = 1
        self._image_width = width
        self._image_height = width / 2

        self._high_placeholder = None
        self._low_placeholder = None
        self._good_placeholder = None
        self.update_data((max + min) / 2)

    def _update_position(self, id, theta, image):
        x = self._r * (1 - math.cos(theta))
        w = self._image_width - 2 * x
        y = self._image_height / 2 - self._r * math.sin(theta)
        h = self._image_height / self._image_width * w
        self.coords(id, self.width / 2, y + self.height / 2 - self._image_height / 2)
        image = ImageTk.PhotoImage(image.resize((int(w), int(h)), Image.ANTIALIAS))
        self.itemconfigure(id, image=image)
        return image


    def update_data(self, torque):
        z = (torque - self.preload_min) / (self.preload_max - self.preload_min)
        theta = -self._thetamax * math.atan(self._a * z)
        self._high_placeholder = self._update_position(self._high, theta + self._thetamax, self.high_image)
        self._low_placeholder  = self._update_position(self._good, theta, self.good_image)
        self._good_placeholder = self._update_position(self._low,  theta - self._thetamax, self.low_image)

        if z > 1:
            self.tag_raise(self._high)
            self.itemconfigure(self._bg, fill="#ec1c24")
        elif z < 0:
            self.tag_raise(self._low)
            self.itemconfigure(self._bg, fill="#fff200")
        else:
            self.tag_raise(self._good)
            self.itemconfigure(self._bg, fill="#0ed145")

    def update_preloads(self, pre_min, pre_max):
        self.preload_max = pre_max
        self.preload_min = pre_min


if __name__ == "__main__":
    import time
    root = Tk()
    pd = PreloadDisplay(root, 200, 300, 1, 0)
    pd.pack()

    f = 0.5
    w = 2 * math.pi * f
    t = 0
    dt = 0.01

    while 1:
        data = math.sqrt(2) * math.sin(w * t)
        pd.update_data(data)
        print(data)
        time.sleep(dt)
        t += dt
        root.update()
