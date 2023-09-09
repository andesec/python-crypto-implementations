#!/usr/bin/env python

class CaeserCipher:
    key = 0
    CHARACTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ123~!@abcdefghijklmnopqrstuvwxyz456#$%7890^&*()_+-=\\|/?.,{}[]`'

    def __init__(self):
        pass

    @classmethod
    def caeser_encrypt(cls, plain_text):
        cipher_text = ''

        for c in plain_text:
            current_index = cls.CHARACTERS.find(c)
            new_index = (current_index + cls.key) % len(cls.CHARACTERS)

            cipher_text += cls.CHARACTERS[new_index]

        return cipher_text

    @classmethod
    def caeser_decrypt(cls, cipher_text):
        plain_text = ''

        for c in cipher_text:
            current_index = cls.CHARACTERS.find(c)
            new_index = (current_index - cls.key) % len(cls.CHARACTERS)

            plain_text += cls.CHARACTERS[new_index]

        return cipher_text

    @classmethod
    def caeser_init(cls, key):
        cls.key = key
