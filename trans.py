from tkinter import *
import backend as bk
import tkinter.font as font
import cv2 as cv
from PIL import ImageTk,Image


window = Tk()
background_color='lightgreen'
foreground_color='purple'
window.configure(bg=background_color)


my_font=font.Font(size=23,family='Garamond')
t_font=font.Font(size=15, family='Garamond')
_img=Image.open('app_img/robot_translator.jpg')
_img=_img.resize((80,60), Image.ANTIALIAS)
trans_img=ImageTk.PhotoImage(_img)

def transfo(img, language):
    image_input.delete(0,'end')
    lang_inp.delete(0,'end')
    translated1_.config(text=bk._translator(img, bk.lang(language)),fg=foreground_color,bg='yellow',padx=50)



labl_1 = Label(window,text=' Image Translator',padx=30,bg=background_color,fg=foreground_color)
labl_1['font']=my_font
#robot_img=Label(image=trans_img, bg=background_color)

space_ = Label(window,text='',pady=40,bg=background_color,fg=foreground_color,image=trans_img)
space1_ = Label(window,text='',pady=10,bg=background_color,fg=foreground_color)
img_lbl = Label(window,text='Image',bg=background_color,fg=foreground_color,pady=10)
img_lbl['font']=my_font 
image_input=Entry(window, borderwidth=2)

lang_lbl = Label(window, text='Your language!',bg=background_color,fg=foreground_color)
lang_lbl['font']=my_font
lang_inp = Entry(window,borderwidth=2)

labl_1.grid(row=0,column=1)
#robot_img.grid(row=0,column=2,columnspan=2)
space_.grid(row=1,column=1)

img_lbl.grid(row=2,column=1)
image_input.grid(row=3,column=1)
space1_.grid(row=4,column=1)
lang_lbl.grid(row=5,column=1)
lang_inp.grid(row=6,column=1)

translated1_=Label(window, text='Translated text will appear here',pady=20)
translated1_.config(bg='orange',fg='purple')
translated1_['font']=t_font
space2_=Label(window,text='',pady=10,bg=background_color,fg=foreground_color)
space2_.grid(row=8,column=1)
translated1_.grid(row=9,column=1)
#space_3=Label(bg=background_color,text='',pady=1)
#space_3.grid(row=10,column=1)

btn_img=Image.open('app_img/translate.jpg')
btn_img=btn_img.resize((50,50), Image.ANTIALIAS)
btn_img=ImageTk.PhotoImage(btn_img)

btn=Button(window,text='Click to Translate',image=btn_img,command=lambda: transfo(image_input.get(),lang_inp.get()   ))
btn.grid(row=11,column=1)



window.mainloop()