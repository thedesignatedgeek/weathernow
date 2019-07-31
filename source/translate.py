#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# ======================================================
#     translate.py
#  ------------------------------------------------------
# Created for the Learning Page Book Project
# Written by G.D. Walters
# Copyright (c) 2019 by G.D. Walters
# This source code is released under the MIT License
# (See MIT_License.txt)
# ======================================================

import requests
import urllib.parse

# ======================================================
# Based on https://ctrlq.org/code/19909-google-translate-api
# ======================================================
# See https://ctrlq.org/code/19899-google-translate-languages#languages
# for language codes
# ======================================================
# function translate()
# ------------------------------------------------------
# inputs: sourcelanguage - two letter code for source language (e.g. 'en')
#         targetlanguage - two letter code for target language (e.g. 'nb')
#         text - text to translate
# returns: translation text
# ======================================================
def translate(sourceLang, targetLang, text):
    sourceText = urllib.parse.quote(text)
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={0}&tl={1}&dt=t&q={2}".format(sourceLang, targetLang, sourceText)
    
    print(url)
    # k = input('press a key - >')
    # session = requests.Session()
    # resp = session.get(url).json()
    resp = requests.get(url).json()
    # print("Response statuscode: {0}".format(resp.status_code))
    translation = resp[0][0][0]
    return translation


if __name__ == '__main__':
    text = "['Wind: ', 'Humidity: ', 'Dew Point: ', 'UV Index: ', 'Visibility: ', 'Pressure: ']"
    info = translate('en','he',text)
    print(info)

