#!/usr/bin/env python

class CaeserCipher:
    CHARACTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ123~!@abcdefghijklmnopqrstuvwxyz456#$%7890^&*()_+-=\\|/?.,{}[]`'

    def __init__(self, key):
        self.key = int(key)
        pass

    def caeser_encrypt(self, plain_text):
        cipher_text = ''

        for c in plain_text:
            current_index = self.CHARACTERS.find(c)
            new_index = (current_index + self.key) % len(self.CHARACTERS)

            cipher_text += self.CHARACTERS[new_index]

        return cipher_text

    def caeser_decrypt(self, cipher_text):
        plain_text = ''

        for c in cipher_text:
            new_index = self.CHARACTERS.find(c)
            old_index = (new_index - self.key) % len(self.CHARACTERS)

            plain_text += self.CHARACTERS[old_index]

        return plain_text
