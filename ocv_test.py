import cv2
import sys
import pytesseract
from googletrans import Translator
import numpy as np
from PIL import Image


# config
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
translator = Translator()
# translate_map

def parse_img(f):
	nparr = np.fromstring(f, np.uint8)
	img_np = cv2.imdecode(nparr, 0)

	img = Image.fromarray(img_np)
	text = pytesseract.image_to_string(img, lang="chi_sim")
	translated = translator.translate(clean_text(text), src="zh-cn", dest="en")

	return (text, translated.text)



def clean_text(text):
	return text.replace('\n', '')

if __name__ == '__main__':
	parse_img("image1.jpg")
