from tkinter import *
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageDraw
import cv2
import numpy as np
import global_variable

class FilterManipulator:
    # Initialize the class by creating instance variables
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.img_blur = None
        self.img_blur_tk = None
        self.img_contour = None
        self.img_contour_tk = None
        self.img_sharpen = None
        self.img_sharpen_tk = None
        self.img_smooth = None
        self.img_smooth_tk = None
        self.img_black_white = None
        self.img_black_white_tk = None


    # Define a method called blur_filter
    def blur_filter(self):
        # Unbind mouse events from the canvas
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        # Access the global variables txt and sub_window
        global txt, sub_window
        # Apply a Box Blur filter to the image
        global_variable.image = global_variable.image.filter(ImageFilter.BoxBlur(float(txt.get())))
        # Resize the blurred image and convert it to a Tkinter-compatible format
        self.img_blur = global_variable.image.resize((400, 400))
        self.img_blur_tk = ImageTk.PhotoImage(self.img_blur)
        # Close the sub-window that is displaying the filter parameter entry form
        sub_window.destroy()
        # Update the canvas to display the blurred image
        self.canvas.imgref = self.img_blur_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_blur_tk)

    # Define a method called contour_filter
    def contour_filter(self):
        # Unbind mouse events from the canvas
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        # Apply a Contour filter to the image
        global_variable.image = global_variable.image.filter(ImageFilter.CONTOUR)
        # Resize the image and convert it to a Tkinter-compatible format
        self.img_contour = global_variable.image.resize((400, 400))
        self.img_contour_tk = ImageTk.PhotoImage(self.img_contour)
        # Update the canvas to display the filtered image
        self.canvas.imgref = self.img_contour_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_contour_tk)


    # Define a method called emboss_filter
    def emboss_filter(self):
        # Unbind mouse events from the canvas
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        # Apply a Emboss filter to the image
        global_variable.image = global_variable.image.filter(ImageFilter.EMBOSS)
        # Resize the image and convert it to a Tkinter-compatible format
        self.img_contour = global_variable.image.resize((400, 400))
        self.img_contour_tk = ImageTk.PhotoImage(self.img_contour)
        # Update the canvas to display the filtered image
        self.canvas.imgref = self.img_contour_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_contour_tk)


    # Define a method called sharpen_filter
    def sharpen_filter(self):
        # Unbind mouse events from the canvas
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        open_cv_image = np.array(global_variable.image) 
        # Convert RGB to BGR 
        open_cv_image = open_cv_image[:, :, ::-1].copy() 
        kernel = np.array([[-1,-1,-1], 
                       [-1, 9,-1],
                       [-1,-1,-1]])
        sharpened = cv2.filter2D(open_cv_image, -1, kernel)
        sharpened = cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB)
        global_variable.image = Image.fromarray(sharpened)
        self.img_sharpen = global_variable.image.resize((400, 400))
        self.img_sharpen_tk = ImageTk.PhotoImage(self.img_sharpen)
        # Update the canvas to display the filtered image
        self.canvas.imgref = self.img_sharpen_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_sharpen_tk)

    
    # Define a method called smooth_filter
    def smooth_filter(self):
        # Unbind mouse events from the canvas
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        open_cv_image = np.array(global_variable.image) 
        # Convert RGB to BGR 
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        kernel = np.ones((5,5),np.float32)/25
        smooth_img = cv2.filter2D(open_cv_image,-1,kernel)
        smooth_img = cv2.cvtColor(smooth_img, cv2.COLOR_BGR2RGB)
        global_variable.image = Image.fromarray(smooth_img)
        self.img_smooth = global_variable.image.resize((400, 400))
        self.img_smooth_tk = ImageTk.PhotoImage(self.img_smooth)
        # Update the canvas to display the filtered image
        self.canvas.imgref = self.img_sharpen_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_smooth_tk)


    # Define a method called black_white_filter
    def black_white_filter(self):
        # Unbind mouse events from the canvas
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        # Convert color image to black white image
        global_variable.image = global_variable.image.convert('L')
        self.img_black_white = global_variable.image.resize((400, 400))
        self.img_black_white_tk = ImageTk.PhotoImage(self.img_black_white)
        # Update the canvas to display the filtered image
        self.canvas.imgref = self.img_black_white_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_black_white_tk)


    def apply(self, filter):
        global txt, sub_window
        sub_window = Tk()
        sub_window.geometry('300x50')
        sub_window.title("Choose Parameter")
        txt = Entry(sub_window, width=20)
        txt.grid(column=0, row=1)
        btn = Button(sub_window, text='Apply', command=filter)
        btn.grid(column=1, row=1)
        sub_window.mainloop()