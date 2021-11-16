from tkinter import *
from PIL import ImageTk, Image
from global_funcs import *

from select_device import select_device


def show_main():
    root = Tk()
    root.configure(bg="white")

    def analysis_command():
        pass

    def collection_button():
        root.destroy()
        select_device()

    width = 15
    height = 5

    img = Image.open("logo.jpg")
    img = img.resize((250, 250), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(img)
    logo_label = Label(root, image=logo, bg="white")
    logo_label.grid(row=0, column=0, columnspan=2, padx=padx, pady=pady)

    analysis = Button(root, text="Analysis", command=analysis_command,
                      width=width, height=height, bg=button_color, font=button_font, fg=button_font_color)
    collection = Button(root, text="Collection", command=collection_button,
                        width=width, height=height, bg=button_color, font=button_font, fg=button_font_color)
    analysis.grid(row=1, column=0, padx=padx, pady=pady)
    collection.grid(row=1, column=1, padx=padx, pady=pady)

    center_window(root)
    root.mainloop()


if __name__ == "__main__":
    show_main()