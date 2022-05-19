#!/usr/bin/python

"""
Vocabulary parsing with Merriam-Webster API (https://dictionaryapi.com/products/index).

author: marcus.wagner@tum.de
"""

import requests

# authentication keys
auth_key_en = "111b176f-3472-4e30-9dab-d672c4183389"
auth_key_es = "36a65f71-eb84-4a85-8a05-b22de265f4b2"


class ParserMW:

    def __init__(self, dictionary='collegiate'):
        self.dictionary = dictionary
        self.auth_key = auth_key_en if self.dictionary == 'collegiate' else auth_key_es
        # TODO

    def translate_merriam_webster(self, word):
        """
        Translates a word using Merriam-Webster dictionary API.
        :param word: word to translate
        :param dictionary: either 'collegiate' or 'spanish'
        """
        if self.dictionary not in ['collegiate', 'spanish']:
            raise RuntimeError

        # "https://dictionaryapi.com/api/v3/references/spanish/json/test?key=36a65f71-eb84-4a85-8a05-b22de265f4b2"
        result = requests.get('https://dictionaryapi.com/api/v3/references/' + self.dictionary + '/json/' + word +
                              '?key=' + self.auth_key)
        result = result.json()
        try:
            # TODO adapt to cards
            returnDict = {
                "word": word,
                "definition": result[0]['shortdef'][0],
                "type": result[0]['fl'],
                # "offensive": str(result[0]['meta']['offensive'])
            }
        except:
            return dict()
            # returnDict = {
            #     "word": word,
            #     "definition": "N/A",
            #     # "type": "N/A",
            #     # "offensive": "N/A"
            # }
        return returnDict

# response format
#meta:{
#     id:"language",
#     uuid:"bb871fef-5605-4cdf-9c8a-254f67468e74",
#     lang:"en",
#     src:"spanish",
#     section:"alpha",
#     stems:[
#         "language",
#         "languages"
#     ],
#     syns:[
#
#     ],
#     ants:[
#
#     ],
#     offensive:false
# },
# hwi:{
#     hw:"language",
#     prs:[
#         {
#             mw:"ˈlæŋɡwɪʤ",
#             sound:{
#                 audio:"langua01"
#             }
#         }
#     ]
# },
# fl:"noun",
# def:[
#     {
#         sseq:[
#             [
#                 [
#                     "sense",
#                     {
#                         sn:"1",
#                         dt:[
#                             [
#                                 "text",
#                                 "{bc}{a_link|idioma} "
#                             ],
#                             [
#                                 "gl",
#                                 "masculine"
#                             ],
#                             [
#                                 "text",
#                                 ", {a_link|lengua} "
#                             ],
#                             [
#                                 "gl",
#                                 "feminine"
#                             ],
#                             [
#                                 "vis",
#                                 [
#                                     {
#                                         t:"the English language",
#                                         tr:"el idioma inglés"
#                                     }
#                                 ]
#                             ]
#                         ]
#                     }
#                 ]
#             ],
#             [
#                 [
#                     "sense",
#                     {
#                         sn:"2",
#                         dt:[
#                             [
#                                 "text",
#                                 "{bc}{a_link|lenguaje} "
#                             ],
#                             [
#                                 "gl",
#                                 "masculine"
#                             ],
#                             [
#                                 "vis",
#                                 [
#                                     {
#                                         t:"body language",
#                                         tr:"lenguaje corporal"
#                                     }
#                                 ]
#                             ]
#                         ]
#                     }
#                 ]
#             ]
#         ]
#     }
# ],
# shortdef:[
#     "idioma, lengua",
#     "lenguaje"
# ]
