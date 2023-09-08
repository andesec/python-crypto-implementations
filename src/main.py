import os
import sys

from src.caeser import CaeserCipher

if __name__ == '__main__':

    # TODO: Use argparse which is the recommended CLI args parser for Python
    # https://stackabuse.com/creating-command-line-utilities-with-pythons-argparse/
    # https://docs.python.org/3/howto/argparse.html
    # Extract parameters for execution
    algorithm = sys.argv[1]
    key = sys.argv[2]
    plain_text = sys.argv[3]
    crypto = CaeserCipher(key)
    crypto.key = sys.argv[2]

    # # If the arg is not provided assume we want to Dry Run.
    # try:
    #     dryRun = sys.argv[3].lower() == 'true'
    # except IndexError as ie:
    #     dryRun = True
    #
    # if dryRun:
    #     print('This is a dry run, nothing will be actually deleted')

    # match algorithm:
    #     case 'caeser': crypto = CaeserCipher(key)
    #     case '-': crypto = None

    print('plaintext = %s' % plain_text)
    print(os.linesep)
    print('ciphertext = %s' % crypto.caeser_encrypt(plain_text))
    print(os.linesep)
    print('decrypted = %s' % plain_text)
