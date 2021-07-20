from tkinter import *
import backend as bk
import tkinter.font as font
import cv2 as cv


window = Tk()
my_font=font.Font(size=23,family='Garamond')
t_font=font.Font(size=15, family='Garamond')

def transfo(img, language):
    
    translated1_.config(text=bk._translator(img, bk.lang(language)))



labl_1 = Label(window,text='Image Translator :)',padx=30)
labl_1['font']=my_font
space_ = Label(window,text='',pady=10)
space1_ = Label(window,text='',pady=10)
img_lbl = Label(window,text='Image')
img_lbl['font']=my_font 
image_input=Entry(window, borderwidth=2)

lang_lbl = Label(window, text='Your language! :D')
lang_lbl['font']=my_font
lang_inp = Entry(window,borderwidth=2)

labl_1.grid(row=0,column=1)
space_.grid(row=1,column=1)

img_lbl.grid(row=2,column=1)
image_input.grid(row=3,column=1)
space1_.grid(row=4,column=1)
lang_lbl.grid(row=5,column=1)
lang_inp.grid(row=6,column=1)

translated1_=Label(window, text='Translated text will appear here',pady=20)
translated1_['font']=t_font
space2_=Label(window,text='',pady=10)
space2_.grid(row=8,column=1)
translated1_.grid(row=9,column=1)
print(lang_inp.get())

btn=Button(window,text='Click to Translate',command=lambda: transfo(f'images/{image_input.get()}',lang_inp.get()   ))
btn.grid(row=10,column=1)



window.mainloop()