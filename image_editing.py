from tkinter import *
from PIL import Image, ImageTk
import global_variable
global txt, sub_window
import time
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.00.0\bin\gswin64c'

class ImageEditor:
    # Initialize the image editor with canvas and other necessary attributes
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.img_flipped = None
        self.img_flipped_tk = None
        self.img_rotated = None
        self.img_rotated_tk = None
        self.img_cropped = None
        self.img_cropped_tk = None
        self.x_crop_start = 0
        self.y_crop_start = 0
        self.x_crop_end = 0
        self.y_crop_end = 0
        self.rectange_id = 0
        self.is_drawing = False
        self.is_cropping = False


    # Define a method for flipping images horizontally
    def flipping_image(self):
        # Unbind certain mouse events
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>") 
        # Flip the global image horizontally
        global_variable.image = global_variable.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        # Resize the flipped image and convert it to a tkinter image
        self.img_flipped = global_variable.image.resize((400, 400))
        self.img_flipped_tk = ImageTk.PhotoImage(self.img_flipped)
        # Update the image in the canvas
        self.canvas.imgref = self.img_flipped_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_flipped_tk)
    

    # Define a method for applying the rotation of an image after the user inputs a degree
    def rotateApplyButton(self):
        global txt, sub_window
        # Get the user input from the text box and rotate the global image
        global_variable.image = global_variable.image.rotate(float(txt.get()), expand=True)
        # Resize the rotated image and convert it to a tkinter image
        self.img_rotated = global_variable.image.resize((400, 400))
        # Close the sub-window
        sub_window.destroy()
        self.img_rotated_tk = ImageTk.PhotoImage(self.img_rotated)
        # Update the image in the canvas
        self.canvas.imgref = self.img_rotated_tk
        self.canvas.itemconfig(global_variable.image_container, image=self.img_rotated_tk)


    # Define a method for rotating images
    def rotating_image(self):
        # Unbind certain mouse events
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")
        # Create a new window for user input
        global txt, sub_window
        sub_window = Tk()
        txt = Entry(sub_window, width=20)
        txt.grid(column=0, row=1)
        btn = Button(sub_window, text='Apply', command=self.rotateApplyButton)
        btn.grid(column=1, row=1)
        sub_window.mainloop()

    
    def start_draw(self, event):
        self.x = event.x
        self.y = event.y
    

    def draw(self, event):
        self.canvas.create_line((self.x, self.y, event.x, event.y), fill='red', width=3, tags="line")
        self.x, self.y = event.x, event.y
        global_variable.isDrawed = True
    

    def drawing_image(self):
        self.is_drawing = True
        if self.is_drawing:
            self.canvas.unbind("<ButtonPress>")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<ButtonRelease>")
            self.canvas.bind("<Button-1>", self.start_draw)
            self.canvas.bind("<B1-Motion>", self.draw)


    # This function sets the starting coordinates of the crop area
    def start_crop(self, event):
        self.x_crop_start = event.x
        self.y_crop_start = event.y


    # This function updates the ending coordinates of the crop area
    def crop(self, event):
        self.x_crop_end = event.x
        self.y_crop_end = event.y


    # This function crops the selected area of the image and updates the canvas to display the cropped image
    def done_crop(self):
        # Crop the image using the min and max values of the starting and ending coordinates of the crop area
        w, h = global_variable.image.size
        global_variable.image = global_variable.image.resize((400, 400)).crop((min(self.x_crop_start, self.x_crop_end),
                                                            min(self.y_crop_start, self.y_crop_end),
                                                            max(self.x_crop_start, self.x_crop_end),
                                                            max(self.y_crop_start, self.y_crop_end))).resize((w, h))
        # Resize the cropped image to 400x400
        self.img_cropped = global_variable.image.resize((400, 400))
        # Convert the cropped image to a Tkinter PhotoImage object
        self.img_cropped_tk = ImageTk.PhotoImage(self.img_cropped)
        # Delete the rectangle used to define the crop area from the canvas
        self.canvas.delete("rect")
        # Set the image reference of the canvas to the cropped image
        self.canvas.imgref = self.img_cropped_tk
        # Update the image in the canvas to display the cropped image
        self.canvas.itemconfig(global_variable.image_container, image=self.img_cropped_tk)


    # This function creates a rectangle on the canvas to define the crop area
    def end_crop(self, event):
        self.x_crop_end = event.x
        self.y_crop_end = event.y
        # Draw a rectangle on the canvas using the starting and ending coordinates of the crop area
        self.canvas.create_rectangle(self.x_crop_start, self.y_crop_start,
                                                         self.x_crop_end, self.y_crop_end, width=1, tags="rect")    
        
        # Use the done_crop() function after a delay of 1000 ms to crop the selected area
        self.canvas.after(1000, self.done_crop)


    # This function allows the user to crop the image by binding the relevant events to the canvas
    def cropping_image(self):
        self.is_drawing = False
        self.is_cropping = True
        if self.is_cropping:
            self.canvas.unbind("<ButtonPress>")
            self.canvas.unbind("<B1-Motion>")
            self.canvas.bind("<ButtonPress>", self.start_crop)
            self.canvas.bind("<B1-Motion>", self.crop)
            self.canvas.bind("<ButtonRelease>", self.end_crop)
        

