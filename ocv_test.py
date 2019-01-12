import cv2
import sys
import pytesseract
from googletrans import Translator

# config
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
translator = Translator()
# translate_map

def parse_img(img):
	words = {}
	im = cv2.imread(img, 0)
	text = pytesseract.image_to_string(im, lang="chi_sim")
	translated = translator.translate(clean_text(text), src="zh-cn", dest="en")
	return (text, translated.text)

def clean_text(text):
	return text.replace('\n', '')

if __name__ == '__main__':
	parse_img(img="image1.jpg")