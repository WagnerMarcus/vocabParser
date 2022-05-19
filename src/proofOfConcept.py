#!/usr/bin/python

"""
Writing Anki files using AnkiPy library.
https://github.com/patarapolw/AnkiPy

TODO: check out https://github.com/patarapolw/ankisync2

Datastructure of anki decks info:
https://github.com/ankidroid/Anki-Android/wiki/Database-Structure

Media adding
https://gist.github.com/androidfred/5562973ac1ae5ce58d305a2e81c0ebd1

Ideas:
* represent cards as table (e.g. pandas data frame to compare field names and be able to write to .csv or .xlsx)

author: marcus.wagner@tum.de
"""

from ankiParser import Anki
from ankiWriter import _CSS_STRING_
from merriamWebster_parsing import ParserMW

# TODO:
#   * automatically remove test .apkg and copy backup when debugging
#   * input interface for words


# define words
words = ['azul', 'verde', 'blance']

# get translations
translation_list = list()
mw_parser = ParserMW(dictionary='spanish')
for word in words:
    translation = mw_parser.translate_merriam_webster(word=word)
    if len(translation) > 0:
        translation_list.append(translation)

print('Obtained translation')
print(translation_list)

# open anki .apkg file
test_anki = Anki('/home/mpjw/PycharmProjects/vocabParser/data/EnglishautomationTest.apkg')

# open deck
test_deck = test_anki.deck("English::Vocabulary::automationTest")

# define anki model
# TODO: resolve import error in anki
test_anki.new_model(
    name='test_english_spanish',
    fields=["English", "Spanish", 'WordType'],
    # templates=["{0} - {1} \n<hr id=answer>\n {2}"],
    templates=["{0}<div style='font-family: calibri; font-size: 18px; font-style:italic'>{2}</div>"
               "<hr id=answer><div style='font-size: 30px; color:lightblue;'>{1}</div>"],
    css=_CSS_STRING_
)

# WIP germanEnglish model
# test_anki.new_model(
#     name='test_english_german',
#     fields=["English", "German", "Examples", 'WordType', 'Hint', 'Synonym', 'Antonym', 'Definitions'],
#     templates=["{0}<br><div style='font-family: calibri; font-size: 18px; font-style:italic'>{3}</div> <p><br>"
#                "<div style='font-family: calibri; font-size: 16px; font-style:italic'>Hint: {4}</div></p>\n<hr "
#                "id=answer>\n<div style='font-size: 30px; color:lightblue;'>{1}</div><p><br>Examples:<div "
#                "style='font-family: calibri; font-size: 20px;'>{2}</div>{5} - {7}"],
#     css=_CSS_STRING_
# )

# add cards
for translation in translation_list:
    test_deck.add_item(*translation.values(), model='test_english_spanish')

# close anki
test_anki.close()
