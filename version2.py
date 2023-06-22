from tkinter import *
from PIL import Image, ImageTk
from file_processing import FileProcessor
from image_editing import ImageEditor
from filter_manipulating import FilterManipulator
from adjust import Adjustor
import global_variable
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.00.0\bin\gswin64c'

window = Tk()
window.title('Image Editor')
window.geometry('800x400')

my_menu = Menu(window)
window.config(menu=my_menu)
canvas = Canvas(window, height=400, width=400)
file_processor = FileProcessor(canvas=canvas)
image_editor = ImageEditor(canvas=canvas)
filter_manipulator = FilterManipulator(canvas=canvas)
adjustor = Adjustor(canvas=canvas)

# File
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New...', command=file_processor.new_file)
file_menu.add_separator()
file_menu.add_command(label='Save', command=file_processor.save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=window.quit)
file_menu.add_separator()
file_menu.add_command(label='Export', command=file_processor.export_file)

# Edit
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Flip', command=image_editor.flipping_image)
edit_menu.add_separator()
edit_menu.add_command(label='Rotate', command=image_editor.rotating_image)
edit_menu.add_separator()
edit_menu.add_command(label='Draw', command=image_editor.drawing_image)
edit_menu.add_separator()
edit_menu.add_command(label='Crop', command=image_editor.cropping_image)


# Filter
filters_menu = Menu(my_menu)
my_menu.add_cascade(label='Filter', menu=filters_menu)
filters_menu.add_command(label='Blur', command = lambda:filter_manipulator.apply(filter_manipulator.blur_filter))
filters_menu.add_separator()
filters_menu.add_command(label='Contour', command=filter_manipulator.contour_filter)
filters_menu.add_separator()
filters_menu.add_command(label='Emboss', command=filter_manipulator.emboss_filter)
filters_menu.add_separator()
filters_menu.add_command(label='Sharpen', command=filter_manipulator.sharpen_filter)
filters_menu.add_separator()
filters_menu.add_command(label='Smooth', command=filter_manipulator.smooth_filter)
filters_menu.add_separator()
filters_menu.add_command(label='Black White', command=filter_manipulator.black_white_filter)


# Adjust
my_menu.add_cascade(label='Adjust', command=adjustor.display)


# Clear
def clear(canvas):
    canvas.unbind("<ButtonPress>")
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease>")
    global_variable.isDrawed = False
    global_variable.image = global_variable.root_image
    root_image_resized = global_variable.root_image.resize((400, 400))
    root_image_tk = ImageTk.PhotoImage(root_image_resized)
    canvas.delete("line")
    canvas.delete("rect")
    canvas.imgref = root_image_tk
    canvas.itemconfig(global_variable.image_container, image=root_image_tk)


my_menu.add_cascade(label='Clear', command=lambda:clear(canvas))



canvas.pack()
window.mainloop()

