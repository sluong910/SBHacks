import cv2
import pytesseract
from googletrans import Translator
import re
from PIL import Image
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from google.cloud import translate
import os

<<<<<<< HEAD
credential_path = r"C:\Users\miche\Desktop\UCI\Projects\Ngan-d75258a9f7a3.json"
=======
credential_path = r"F:\\VAULT 419\\Files\\projects\\Python\\test\\Ngan-d75258a9f7a3.json"
>>>>>>> 1176e020460653c9476d7a4a3f5f7a58647c85b4
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
translate_client = translate.Client()

# config
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

def parse_img(img, lang):
    try:
        # f = open(img, 'rb').read()
        nparr = np.fromstring(img, np.uint8)
        img_np = cv2.imdecode(nparr, 0)
        img = Image.fromarray(img_np)
        text = pytesseract.image_to_string(img, lang=lang)
        # return clean_text(text)
        return text
    except Exception as e:
        return str(e)

def alt_translate(text):
                target = 'en'
                return translate_client.translate(text, target_language=target)['translatedText']

def generate_vocab(text, og, choice):
    try:
                i = 0
                dic = {}
                k = 0
                global n
                n = choice
                pronun_list_old = (translator.translate(text, og, og).pronunciation).split(" ")
                pronun_list = [re.sub("\W+", '', pron).lower() for pron in pronun_list_old]
                # print(pronun_list)
                while i < len(text):
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
    except:
        return alt_generate_vocab(text, n)

def alt_generate_vocab(text, n):
    global translate_client
    target = 'en'
    dic = {}
    if " " in text:
        text = text.split(" ")
        if n == 1 or n == 0:
            for char in text:
                dic[char] = translate_client.translate(char, target_language=target)['translatedText']
        if n == 2 or n == 0:
            bucket = [text[i] + " " + text[i + 1] for i in range(len(text) - 1)]
            for piece in bucket:
                dic[piece] = translate_client.translate(piece, target_language=target)['translatedText']
        if n == 3 or n == 0:
            barrel = [text[i] + " " + text[i + 1] + " " + text[i + 2] for i in range(len(text) - 2)]
            for thing in barrel:
                dic[thing] = translate_client.translate(thing, target_language=target)['translatedText']
    else:
        text = text.split(" ")
        if n == 1 or n == 0:
            for char in text:
                dic[char] = translate_client.translate(char, target_language=target)['translatedText']
        if n == 2 or n == 0:
            bucket = [text[i] + text[i + 1] for i in range(len(text) - 1)]
            for piece in bucket:
                dic[piece] = translate_client.translate(piece, target_language=target)['translatedText']
        if n == 3 or n == 0:
            barrel = [text[i] + text[i + 1] + text[i + 2] for i in range(len(text) - 2)]
            for thing in barrel:
                dic[thing] = translate_client.translate(thing, target_language=target)['translatedText']
    return dic

def clean_text(text):
    return text.replace('\n', '').strip()

def main(file, lang, trans_lang, choice):
    text = parse_img(file, lang)
    translated = alt_translate(text)
    vocab_dict = generate_vocab(text, trans_lang, choice)
    return (text, translated, vocab_dict)
