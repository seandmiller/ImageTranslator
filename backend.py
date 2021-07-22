import cv2 as cv
import pytesseract as loki
from googletrans import Translator, LANGUAGES
from tkinter import *
import requests


#cv.imshow('read',img)



cv.waitKey(0)
trans=Translator()

#print(text)


def lang(destini):
    for x, y in LANGUAGES.items():
        if destini=='chinese':
            destini='chinese (simplified)'
        if destini==y:
          
          return x
          

def _translator(img, destin):

  
    
    if len(img) < 30:
      
      img=f'images/{img}'
      
    else: 
      response=requests.get(f'{img}')
      data=open('images/image_download.png','wb')
      data.write(response.content)
      data.close()
      img='images/image_download.png'
    
    image = cv.imread(img)
    text = loki.image_to_string(image)
    print(text)
    translated_text=trans.translate(text, dest=destin)
    return translated_text.text

#lang('english')

#print(_translator('images/how_r.jpg', 'english'))





#print(translated_text.text)
