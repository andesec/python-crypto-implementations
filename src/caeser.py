#!/usr/bin/env python

class CaeserCipher:
    key = None
    CHARACTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+-=\\|/?.,{}[]`'

    def __init__(self, key):
        self.key = key

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
