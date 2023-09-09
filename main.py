#!/usr/bin/env python
import argparse

from crypto.caeser import CaeserCipher

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='A simple python program to encrypt and decrypt data based on options.')

    parser.add_argument('-a', '--algorithm', default='caeser', help='Name of the algorithm to use')
    parser.add_argument('-k', '--key', default='12', help='Key to use for encryption or path of the public key file.')
    parser.add_argument('-d', '--data', default='Life is beautiful, isn\'t it?', help='Default message')

    args = parser.parse_args()

    algorithm = args.algorithm
    key = args.key
    data = args.data

    match algorithm:
        case 'caeser':
            crypto = CaeserCipher(key)
        case '-':
            crypto = None

    cipher_data = crypto.caeser_encrypt(data)

    print('plaintext = %s' % data)
    print('ciphertext = %s' % cipher_data)
    print('decrypted = %s' % crypto.caeser_decrypt(cipher_data))
