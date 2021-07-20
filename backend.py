import cv2 as cv
import pytesseract as loki
from googletrans import Translator, LANGUAGES
from tkinter import *


#cv.imshow('read',img)



cv.waitKey(0)
trans=Translator()

#print(text)


def lang(destini):
    for x, y in LANGUAGES.items():
        if destini=='chinese':
            destini='chinese (simplified)'
        if destini==y:
          print(x)
          return x
          

def _translator(img, destin):
    image = cv.imread(img)
    text = loki.image_to_string(image)
    print(text)
    translated_text=trans.translate(text, dest=destin)
    return translated_text.text

#lang('english')

#print(_translator('images/how_r.jpg', 'english'))





#print(translated_text.text)
