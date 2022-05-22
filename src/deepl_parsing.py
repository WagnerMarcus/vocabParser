#!/usr/bin/python

"""
Test script to parse vocabulary with [deepL API](https://pypi.org/project/deepl/).

author: marcus.wagner@tum.de
"""

import deepl

# Create a Translator object providing your DeepL API authentication key.
# Be careful not to expose your key, for example when sharing source code.
# TODO read auth key from config file
auth_key = ''


translator = deepl.Translator(auth_key)
# This example is for demonstration purposes only. In production code, the
# authentication key should not be hard-coded, but instead fetched from a
# configuration file or environment variable.

# Translate text into a target language, in this case, French
result = translator.translate_text("Hello, world!", target_lang="DE")
print(result)  # "Bonjour, le monde !"
# Note: printing or converting the result to a string uses the output text

# Translate multiple texts into British English
result = translator.translate_text(["お元気ですか？", "¿Cómo estás?"], target_lang="EN-GB")
print(result[0].text)  # "How are you?"
print(result[0].detected_source_lang)  # "JA"
print(result[1].text)  # "How are you?"
print(result[1].detected_source_lang)  # "ES"

# Translate a formal document from English to German
try:
    translator.translate_document_from_filepath(
        "Instruction Manual.docx",
        "Bedienungsanleitung.docx",
        target_lang="DE",
        formality="more"
    )
except deepl.DocumentTranslationException as error:
    # If an error occurs during translate_document_from_filepath() or
    # translate_document() and after the document was already uploaded, a
    # DocumentTranslationException is raised. The document_handle property
    # contains the document handle to later retrieve the document or contact
    # DeepL support.
    doc_id = error.document_handle.id
    doc_key = error.document_handle.key
    print(f"Error after uploading document ${error}, id: ${doc_id} key: ${doc_key}")
except deepl.DeepLException as error:
    # Errors during upload raise a DeepLException
    print(error)

# Glossaries allow you to customize your translations
glossary_en_to_de = translator.create_glossary(
    "My glossary",
    source_lang="EN",
    target_lang="DE",
    entries={"artist": "Maler", "prize": "Gewinn"},
)

with_glossary = translator.translate_text_with_glossary(
    "The artist was awarded a prize.", glossary_en_to_de
)
print(with_glossary)  # "Der Maler wurde mit einem Gewinn ausgezeichnet."

without_glossary = translator.translate_text(
    "The artist was awarded a prize.", target_lang="DE"
)
print(without_glossary)  # "Der Künstler wurde mit einem Preis ausgezeichnet."


# Check account usage
usage = translator.get_usage()
if usage.character.limit_exceeded:
    print("Character limit exceeded.")
else:
    print(f"Character usage: {usage.character.count} of {usage.character.limit}")

# Source and target languages
print("Source languages:")
for language in translator.get_source_languages():
    print(f"{language.code} ({language.name})")  # Example: "DE (German)"

print("Target languages:")
for language in translator.get_target_languages():
    if language.supports_formality:
        print(f"{language.code} ({language.name}) supports formality")
    else:
        print(f"{language.code} ({language.name})")



