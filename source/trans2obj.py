#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import json

# ======================================================
# An attempt to create a json object for the translations of the prompts
# ======================================================


def createobj():
    langs = {}
    langs['languages'] = []
    langs['languages'].append({
        "lang": "en",
        "prompts": ['Wind', 'Humidity', 'Dew Point', 'UV Index', 'Visibility', 'Pressure', 'Feels Like: ', 'Low: ', 'High: ', 'Locations', 'Language', 'Units', 'Hourly', 'Daily']
        })
    langs['languages'].append({
        "lang": "nb",
        "prompts": ['Vind', 'Fuktighet', 'Duggpunkt', 'UV-indeks', 'Synlighet', 'Trykk', 'Føles som:', 'Lav:', 'Høy:', 'Lokasjoner', 'Språk', 'Enheter', 'En time', 'Daglig']
        })
    langs['languages'].append({
        "lang": "sv",
        "prompts": ['Vind', 'Luftfuktighet', 'Daggpunkt', 'UV-index', 'Synlighet', 'Tryck', 'Känns som:', 'Låg:', 'Hög:', 'Platser', 'Språk', 'Enheter', 'En timme', 'Dagligen']
        })
    langs['languages'].append({
        "lang": "nl",
        "prompts": ['Wind', 'Vochtigheid', 'Dauwpunt', 'UV-index', 'Zichtbaarheid', 'Druk', 'Voelt als:', 'Laag:', 'Hoog:', 'Locaties', 'Taal', 'Eenheden', 'Elk uur', 'Dagelijks']
        })
    langs['languages'].append({
        "lang": "fr",
        "prompts": ['Vent', 'Humidité', 'Point de rosée', 'Indice UV', 'Visibilité', 'Pression', 'Ressenti:', 'Bas:', 'Haut:', 'Lieux', 'Langue', 'Unités', 'Toutes les heures', 'Quotidien']
        })
    langs['languages'].append({
        "lang": "fi",
        "prompts": ['Tuuli', 'Kosteus', 'Kastepiste', 'UV-indeksi', 'Näkyvyys', 'Paine', 'Tuntuu:', 'Matala:', 'Korkea:', 'Paikat', 'Kieli', 'Yksiköt', 'Tunnitunnit', 'Päivittäin']
        })
    langs['languages'].append({
        "lang": "es",
        "prompts": ['Viento', 'Humedad', 'Punto de rocío', 'Índice UV', 'Visibilidad', 'Presión', 'Se siente como:', 'Bajo:', 'Alto:', 'Ubicaciones', 'Idioma', 'Unidades', 'Por hora', 'Diario']
        })
    langs['languages'].append({
        "lang": "de",
        "prompts": ['Wind', 'Luftfeuchtigkeit', 'Taupunkt', 'UV-Index', 'Sichtbarkeit', 'Druck', 'Fühlt sich an wie:', 'Niedrig:', 'Hoch:', 'Standorte', 'Sprache', 'Einheiten', 'Stündlich', 'Täglich']
        })
    langs['languages'].append({
        "lang": "da",
        "prompts": ['Vind', 'Fugtighed', 'Dugpunkt', 'UV-indeks', 'Synlighed', 'Tryk', 'Føles som:', 'Lav:', 'Høj:', 'Lokationer', 'Sprog', 'Enheder', 'En time', 'Dagligt']
        })
# Maybe later...
# he ['רוח:', 'לחות:', 'נקודת הטל:', 'מדד UV:', 'ראות:', 'לחץ:']
    print(langs, type(langs))
    # resp = input('Press a key -> ')
    return langs


# ======================================================
# Write the config file
# ======================================================
def write_lang_file(obj):
    with open("langfile.json", 'w') as outfile:
        json.dump(obj, outfile)


# ======================================================
# Read the config file, if it exists, and get a list
# of locations.
# ======================================================
def read_lang_file():
    with open("langfile.json", 'r') as f:
        langs = json.load(f)
    return langs


def testit(jobj):
    # print(jobj)
    # print(type(jobj))
    ltest = jobj['languages']
    # print(type(ltest))
    print((ltest))
    for i in ltest:
        lan = i['lang']
        p = i['prompts']
        print(lan)
        # print(p)
        print(len(p))
        print(type(p))
        for i in p:
            print(i)


if __name__ == '__main__':
    obj = createobj()
    write_lang_file(obj)
    # ======================================================
    # The two lines below, will test your file.
    # ======================================================
    # lng = read_lang_file()
    # testit(lng)
