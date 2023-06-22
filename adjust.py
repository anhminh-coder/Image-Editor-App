from tkinter import *
from PIL import Image, ImageTk, ImageEnhance
import global_variable


class Adjustor:
    # Initializing the instance variables
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.brightness_scale = None
        self.r_scale = None
        self.g_scale = None
        self.b_scale = None
        self.brightness_label = None
        self.r_label = None
        self.g_label = None
        self.b_label = None
        self.apply_button = None
        self.cancel_button = None
        self.img_copy = None


    # Method to apply the adjustments to the image
    def apply_adjust(self):
        # Update the global image with the current adjustments
        global_variable.image = self.img_copy.copy()
        # Convert the image into a tkinter compatible object
        img_copy_tk = ImageTk.PhotoImage(self.img_copy.resize((400, 400)))
        self.img_copy = global_variable.image.copy()
        # Update the canvas image reference with the adjusted image
        self.canvas.imgref = img_copy_tk
        self.canvas.itemconfig(global_variable.image_container, image=img_copy_tk)
        # Close the adjust window
        self.adjust_window.destroy()


    # Method to cancel the adjustments
    def cancel_adjust(self):
        # Restore the global image to the original
        self.img_copy = global_variable.image.copy()
        # Update the canvas image reference with the original image
        img_tk = ImageTk.PhotoImage(global_variable.image.resize((400, 400)))
        # Update the canvas image reference with the original image
        self.canvas.imgref = img_tk
        self.canvas.itemconfig(global_variable.image_container, image=img_tk)
        # Close the adjust window
        self.adjust_window.destroy()


    # Method to update the brightness scale
    def update_brightness(self, event):
        # Enhance the brightness of the image using the given scale
        brightness_enhancer = ImageEnhance.Brightness(global_variable.image)
        self.img_copy = brightness_enhancer.enhance(self.brightness_scale.get())
        # Convert the image into a tkinter compatible object
        img_copy_tk = ImageTk.PhotoImage(self.img_copy.resize((400, 400)))
        # Update the canvas image reference with the adjusted image
        self.canvas.imgref = img_copy_tk
        self.canvas.itemconfig(global_variable.image_container, image=img_copy_tk)


    def update_red(self, event):
        r_value = self.r_scale.get()
        [xs, ys] = self.img_copy.size

        if not (r_value == 0):
            # Loop over every pixel and adjust the red channel
            for x in range(0, xs):
                for y in range(0, ys):
                    [r_, g_, b_] = self.img_copy.getpixel((x, y))
                    r_ = r_ + int(r_value)
                    value = (r_, g_, b_)
                    self.img_copy.putpixel((x, y), value)

        img_copy_tk = ImageTk.PhotoImage(self.img_copy.resize((400, 400)))
        # Update the canvas image reference with the adjusted image
        self.canvas.imgref = img_copy_tk
        self.canvas.itemconfig(global_variable.image_container, image=img_copy_tk)


    def update_green(self, event):
        g_value = self.g_scale.get()
        [xs, ys] = self.img_copy.size

        if not (g_value == 0):
            # Loop over every pixel and adjust the green channel
            for x in range(0, xs):
                for y in range(0, ys):
                    [r_, g_, b_] = self.img_copy.getpixel((x, y))
                    g_ = g_ + int(g_value)
                    value = (r_, g_, b_)
                    self.img_copy.putpixel((x, y), value)

        img_copy_tk = ImageTk.PhotoImage(self.img_copy.resize((400, 400)))
        # Update the canvas image reference with the adjusted image
        self.canvas.imgref = img_copy_tk
        self.canvas.itemconfig(global_variable.image_container, image=img_copy_tk)

    
    def update_blue(self, event):
        b_value = self.b_scale.get()
        [xs, ys] = self.img_copy.size

        if not (b_value == 0):
            # Loop over every pixel and adjust the blue channel
            for x in range(0, xs):
                for y in range(0, ys):
                    [r_, g_, b_] = self.img_copy.getpixel((x, y))
                    b_ = b_ + int(b_value)
                    value = (r_, g_, b_)
                    self.img_copy.putpixel((x, y), value)

        img_copy_tk = ImageTk.PhotoImage(self.img_copy.resize((400, 400)))
        # Update the canvas image reference with the adjusted image
        self.canvas.imgref = img_copy_tk
        self.canvas.itemconfig(global_variable.image_container, image=img_copy_tk)


    def display(self):
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        self.img_copy = global_variable.image.copy()
        self.adjust_window = Toplevel()
        self.adjust_window.title("Adjust")
        self.brightness_scale = Scale(self.adjust_window, from_=0, to_=2, length=250, resolution=0.1, orient=HORIZONTAL)
        self.r_scale = Scale(self.adjust_window, from_=-100, to_=100, length=250, resolution=1, orient=HORIZONTAL)
        self.g_scale = Scale(self.adjust_window, from_=-100, to_=100, length=250, resolution=1, orient=HORIZONTAL)
        self.b_scale = Scale(self.adjust_window, from_=-100, to_=100, length=250, resolution=1, orient=HORIZONTAL)
        self.brightness_label = Label(self.adjust_window, text="Brightness")
        self.r_label = Label(self.adjust_window, text="R")
        self.g_label = Label(self.adjust_window, text="G")
        self.b_label = Label(self.adjust_window, text ="B")
        self.apply_button = Button(self.adjust_window, text='Apply', command=self.apply_adjust)
        self.cancel_button = Button(self.adjust_window, text='Cancel', command=self.cancel_adjust)
        self.brightness_scale.set(1)
        self.brightness_label.pack()
        self.brightness_scale.pack()
        self.r_label.pack()
        self.r_scale.pack()
        self.g_label.pack()
        self.g_scale.pack()
        self.b_label.pack()
        self.b_scale.pack()
        self.cancel_button.pack(side=RIGHT)
        self.apply_button.pack(side=LEFT)

        self.brightness_scale.bind("<ButtonRelease-1>", self.update_brightness)
        self.r_scale.bind("<ButtonRelease-1>", self.update_red)
        self.g_scale.bind("<ButtonRelease-1>", self.update_green)
        self.b_scale.bind("<ButtonRelease-1>", self.update_blue)

        self.adjust_window.mainloop()
        

