import json
import requests
from flask_babel import gettext
from config import TRANSLATE_API_KEY

def yandex_translate(text, sourceLang, destLang):
    if TRANSLATE_API_KEY == "":
        return gettext('Error: translation service not configured.')
    try:
        # translate
        params = {'key': TRANSLATE_API_KEY,
                  'text': text.encode("utf-8"),
                  'lang': sourceLang + '-' + destLang}
        response = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data=params)
        response = response.json()
        return response['text'][0]
    except:
    #    print (response)
        return gettext('Error: Unexpected error.')