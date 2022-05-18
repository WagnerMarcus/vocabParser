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

from AnkiPy import Anki

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

        anki_deck.close()


if __name__ == '__main__':
    # open anki .apkg file
    test_anki = Anki('../data/EnglishautomationTest.apkg')

    # open deck
    test_deck = test_anki.deck("English::Vocabulary::automationTest")

    # define anki model
    # TODO: resolve import error in anki
    test_anki.new_model(
        name='test_english_german',
        fields=["English", "German", 'WordType', 'Hint'],
        # templates=["{0} - {1} \n<hr id=answer>\n {2}"],
        templates=["{0}<div style='font-family: calibri; font-size: 18px; font-style:italic'>{2}</div> <p>"
                   "<div style='font-family: calibri; font-size: 16px; font-style:italic'>Hint: {3}</div></p>"
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
    test_deck.add_item("Hello", "Bonjour", "Hallo Example",
                       '[sound:yandex-49593260-a47e5d78-5b8f2d6d-4f6a0797-39be0e5f.mp3]', '', model='test_english_german')
    test_deck.add_item("How are you ?", "Comment ca va ?", "Example", '', '', model='test_english_german')
    test_deck.add_item("Flower", "fleur", "Example Blume", '', '', model='test_english_german')
    test_deck.add_item("House", "Maison", "Example Haus", '', '', model='test_english_german')

    test_anki.close()
