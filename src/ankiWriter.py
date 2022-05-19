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

# constants
_CSS_STRING_ = ".card {font-family: arial; font-size: 20px; text-align: center; color: black; " \
               "background-color: white;}.nightMode .card { color: white;}"


class Writer:
    """
    Writer class modifying Anki deck files (.apkg).
    TODO:
      * anki card modules
      * collection and deck info
    """

    def __init__(self, path_to_anki_apkg):
        # TODO sanity check anki path
        self.anki = Anki(path_to_anki_apkg)

    def _add_to_deck(self, deck, card: dict):
        """
        Adds cards contained as dict in cards parameter to specified deck.
        deck: Deck nae (str)
        cards: Key -> list dict with cards data
        """

        # TODO check model compatibility
        # assert len(card.keys()) ==

        # add card
        deck.add_item(*card.values())

    def add_cards_to_deck(self, deck: str, cards: list):
        """

        """

        # TODO add anki card model parameter
        # open deck
        anki_deck = self.anki.deck(deck)

        for card in cards:
            self._add_to_deck(anki_deck, card)

        self.anki.close()
