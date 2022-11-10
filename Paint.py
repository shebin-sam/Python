from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk
from tkinter import messagebox
root = Tk()
root.title = ("Paint")
root.geometry = ("800*800")

brush_color = "black"
#drawing in canvas function
def paint(e):

   # Brush parameters
   brush_width = int(slider.get())

   # brush types BUTT , ROUND ,PROJECTING
   brush_type2 = brush_type.get()


   # starting position
   x1 = e.x - 1
   y1 = e.y - 1

   # Ending position
   x2 = e.x + 1
   y2 = e.y + 1


   #drawing line in canvas
   paint_canvas.create_line(x1, y1, x2, y2, fill= brush_color,width = brush_width,capstyle = brush_type2 ,smooth = True)

#change the size of the brush
def change_brush_size(a):
   slider_label.config(text = int(slider.get()))


#create canvas
w = 600
h = 400
paint_canvas = Canvas(root,width = w,height = h,bg= 'white')
paint_canvas.pack(pady = 20 ,)

#change brush colour function
def change_brush_color():
   global brush_color
   brush_color = "Black"
   brush_color = colorchooser.askcolor(color=brush_color)[1]


#change canvas color function
def change_canvas_color():
   global canvas_color
   canvas_color = "Black"
   canvas_color = colorchooser.askcolor(color=brush_color)[1]
   paint_canvas.config(bg =canvas_color )
#clear function
def clear_screen():
   paint_canvas.delete(ALL)
   paint_canvas.config(bg='white')
#save funtion
def save_project():
   result = filedialog.asksaveasfilename(initialdir = "E:/images",filetypes = (("png files","*.png"),("all files","*.*")))
   if result.endswith(".png"):
       pass
   else:
       result = result + ".png"

   if result:
       x = root.winfo_rootx()+paint_canvas.winfo_rootx()
       y = root.winfo_rooty()+paint_canvas.winfo_rooty()
       x1 = x+paint_canvas.winfo_width()
       y1 = y + paint_canvas.winfo_height()
       ImageGrab.grab().crop((x,y,x1,y1)).save(result)
       #pop up
       messagebox.showinfo('Saved Successfully',"your image is saved successfully")


#paint_canvas.create_line(x1,y1,x2,y2,fill = "red")

paint_canvas.bind('<B3-Motion>',paint)

# Brush Options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady = 30)

# brush size
brush_size_frame = LabelFrame(brush_options_frame,text = "Brush Size")
brush_size_frame.grid(row = 0 , column = 0, padx = 50)

#brush slider
slider = ttk.Scale(brush_size_frame, from_ = 1 , to = 100 ,command = change_brush_size ,orient = VERTICAL, value = 10)
slider.pack(pady = 10 ,padx = 10)

#Brush Slider label
slider_label = Label(brush_size_frame,text=slider.get())
slider_label.pack(pady = 5)

#Brush Type button
brush_type_frame = LabelFrame(brush_options_frame,text = "Brush Type")
brush_type_frame.grid(row = 0, column = 1,padx = 50)

brush_type = StringVar()
brush_type.set("round")
#creating radio buttons
brush_type_radio1 = Radiobutton(brush_type_frame,text = 'Round', variable = brush_type,value = 'round')
brush_type_radio2 = Radiobutton(brush_type_frame, text = 'Slash',variable = brush_type,value ='butt')
brush_type_radio3 = Radiobutton(brush_type_frame, text = 'Diamond',variable = brush_type,value ='projecting')

brush_type_radio1.pack(anchor =W)
brush_type_radio2.pack(anchor =W)
brush_type_radio3.pack(anchor =W)

#change colors
brush_color_frame =LabelFrame(brush_options_frame,text = "Change Colour")
brush_color_frame.grid(row = 0,column = 2,padx = 50)

#brush color change button

brush_color_buttons = Button(brush_color_frame,text = "Brush Colour",command = change_brush_color,)
brush_color_buttons.pack(pady = 10 , padx =10)

#change canvas background colour
canvas_color_buttons = Button(brush_color_frame,text = "Canvas Colour",command = change_canvas_color,)
canvas_color_buttons.pack(pady = 10 , padx =10)

#options
options_frame =LabelFrame(brush_options_frame,text = "Options")
options_frame.grid(row = 0 , column = 3 ,padx = 50)
#clear button
clear_button =Button(options_frame,text = "Clear",command = clear_screen)
clear_button.pack(padx = 10,pady =10)
#save button
save_button = Button(options_frame,text = "Save", command = save_project)
save_button.pack(padx=10,pady =10)


root.mainloop()
