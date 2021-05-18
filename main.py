#import tkinter as tk
import tkinter as tk
#import PIL for more use of generalized image formats
from PIL import ImageTk, Image


# class FullScreenApp(object):
#     def __init__(self, master, **kwargs):
#         self.master=master
#         pad=3
#         self._geom='200x200+0+0'
#         master.geometry("{0}x{1}+0+0".format(
#             master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
#         master.bind('<Escape>',self.toggle_geom)
#     def toggle_geom(self,event):
#         geom=self.master.winfo_geometry()
#         print(geom,self._geom)
#         self.master.geometry(self._geom)
#         self._geom=geom
#         self.window.attributes("-fullscreen", False)

window = tk.Tk()

#REMOVE THIS
window.attributes("-fullscreen", True)
window.configure(background='black')

img = Image.open('testPng.png')
img = img.resize((250, 250), Image.ANTIALIAS)
pimg = ImageTk.PhotoImage(img)
#size = img.size

#create widget

#REMOVE THIS
canvas = tk.Canvas(window,bg="black",highlightthickness=0)
#canvas = tk.Canvas(window,width = 720, height = 576,bg="black",highlightthickness=0)

#project to screen
#REMOVE THIS
canvas.pack(fill=tk.BOTH, expand=True)
canvas.pack()
#update for fullscreeen
canvas.update()

#REMOVE THIS
#canvas.create_image(canvas.winfo_screenwidth()/2, canvas.winfo_screenheight()/2, anchor=tk.CENTER, image=pimg)
canvas.create_image(canvas.winfo_width()/2, canvas.winfo_height()/2, anchor=tk.CENTER, image=pimg)
canvas.create_image(0, 85, anchor=tk.W, image=pimg)
canvas.create_image(canvas.winfo_width(), 85, anchor=tk.E, image=pimg)
canvas.create_image(canvas.winfo_width(), canvas.winfo_height()-85, anchor=tk.E, image=pimg)
canvas.create_image(0, canvas.winfo_height()-85, anchor=tk.W, image=pimg)

print(canvas.winfo_height())
print(canvas.winfo_width())


#print("hello world!")
window.mainloop()
