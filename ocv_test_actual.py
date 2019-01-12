import cv2
import pytesseract
from googletrans import Translator
import re
from PIL import Image
import numpy as np

# config
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
translator = Translator()

def parse_img(img, lang):
	try:
	    f = open(img, 'rb').read()
	    nparr = np.frombuffer(f, np.uint8)
	    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
	    img = Image.fromarray(img_np)
	    text = pytesseract.image_to_string(img, lang=lang)
	    return clean_text(text)
	except Exception as e:
		return str(e)

def translate(text, og, target):
    translated = translator.translate(text, src=og, dest=target)
    return translated

def generate_vocab(text, og):
	try:
                i = 0
                dic = {}
                k = 0
                pronun_list_old = (translator.translate(text, og, og).pronunciation).split(" ")
                pronun_list = [re.sub("\W+", '', pron).lower() for pron in pronun_list_old]
                # print(pronun_list)
                while i < len(text):
                        translator = Translator()
                if translator.translate(text[i], src=og, dest=og).pronunciation.lower() == pronun_list[k].lower():
                        dic[text[i]] = pronun_list[k] + " | " + translate(text[i], og, "en").text
                        k += 1
                        i += 1
                else:
                        word = translator.translate(text[i], src=og, dest=og).pronunciation.lower()
                        result = text[i]
                        while word != pronun_list[k].lower():
                            i += 1
                            result = result + text[i]
                            word = translator.translate(result, src=og, dest=og).pronunciation.lower()
                            word = re.sub("\W+", '', word).lower()
                        dic[result] = pronun_list[k] + " | " + translate(result, og, "en").text
                        k += 1
                        i += 1
                return dic
	except Exception as e:
		return str(e)

def clean_text(text):
	return text.replace('\n', '').strip()

if __name__ == '__main__':
    # text = parse_img(img="image1.jpg", lang="chi_sim")
    text = parse_img("test_img/img3.jpg", "chi_sim")
    print(generate_vocab(text, "zh-tw"))
    # print(translate(text, "zh-tw", "en"))
    print(translator.translate(text, src="zh-tw", dest="en").text)
