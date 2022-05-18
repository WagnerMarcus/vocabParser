#!/usr/bin/python

"""
Main app tying together parsing and anki card creation.

author: marcus.wagner@tum.de
"""

from merriamWebster_parsing import ParserMW

mw_parser = ParserMW(dictionary='spanish')
print(mw_parser.translate_merriam_webster(word='travel'))

