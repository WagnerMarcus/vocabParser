#!/usr/bin/python

"""
Main app tying together parsing and anki card creation.

author: marcus.wagner@tum.de
"""

from merriamWebster_parsing import ParserMW
from ankiWriter import Writer

verbose = True

words = ['travel']

# get translations
translation_list = list()
mw_parser = ParserMW(dictionary='spanish')
translation = mw_parser.translate_merriam_webster(word='travel')

if verbose:
    print('Obtained translation')
    print(translation)

# create anki cards
writer = Writer('../data/EnglishautomationTest.apkg')
print('writing cards ...') if verbose else None
writer.add_cards_to_deck("English::Vocabulary::automationTest", [translation])


