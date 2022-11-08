from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:/Users/shahhar06/AppData/Local/Tesseract-OCR/tesseract.exe'

#Define path to image
path_to_image = 'images/fmc1.PNG'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)
# text = text.split('\n')

print(text)

from googletrans import Translator

tran = Translator()

tran_text = tran.translate(text, src='es', dest='en')
print(tran_text.text)

with open('text.csv', 'w') as t:
    t.write(tran_text.text)


print('DONE')
# to add text to our csv file
# with open('trial.csv', 'w') as trial:
#     trial.write(text)
# print('DOne') 

# import pandas as pd
# df = pd.read_csv('trial.csv', encoding='latin-1')
# # df = df.dropna()
# print(df)
# df[text[0]] = [text[i] for i in range(1, len(text))]
# print(df.head())





