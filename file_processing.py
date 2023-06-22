from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import global_variable
import io
import os


class FileProcessor:
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.img = None
        self.img_resized = None
        self.img_tk = None
        self.filename = None
        self.image_container = None
        self.img_size = None
    

    def new_file(self):
        f_types = [('Jpg Files', '*.jpg')]
        self.filename = filedialog.askopenfilename(filetypes=f_types)
        self.img = Image.open(self.filename)
        self.img_size = self.img.size
        self.img_resized = self.img.resize((400, 400))
        self.img_tk = ImageTk.PhotoImage(self.img_resized)
        self.image_container = self.canvas.create_image(0, 0, image=self.img_tk, anchor = NW)
        global_variable.image_container = self.image_container
        global_variable.image = self.img
        global_variable.root_image = self.img.copy()

    def save_file(self):
        if global_variable.isDrawed == True:
            ps = self.canvas.postscript(colormode='color', pagewidth=2000)
            global_variable.image = Image.open(io.BytesIO(ps.encode('utf-8'))).resize(self.img_size)
        rgb_img = global_variable.image.convert('RGB')
        self.filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
        if not self.filename:
            return
        rgb_img.save(self.filename)
    
    def export_file(self):
        if global_variable.isDrawed == True:
            ps = self.canvas.postscript(colormode='color', pagewidth=2000)
            global_variable.image = Image.open(io.BytesIO(ps.encode('utf-8'))).resize(self.img_size)
        rgb_img = global_variable.image.convert('RGB')
        files = [('PNG files', '*.png'), ('JPG files', '*.jpg'), ('GIF files', '*.gif')]
        self.filename = filedialog.asksaveasfile(mode='w', defaultextension=files, filetypes=files)
        print(self.filename.name)

