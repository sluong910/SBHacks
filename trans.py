# Imports the Google Cloud client library
from google.cloud import translate
import os

credential_path = "F:\\VAULT 419\\Files\\projects\\Python\\SBHacks\\My First Project-4d14c9eb3507.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u'Hello, world!'
# The target language
target = 'ru'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
print(translation)