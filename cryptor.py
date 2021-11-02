from tools.main_tools import handle_arguments
import argparse
import textwrap
import sys

def usage():
    """
    pring usage of script.
    """
    print('''Example:
    python cryptor.py -g path/to/save/rsa_keys # Generating RSA Public and RSA Private Keys
    python cryptor.py -e -f ["file1" "path1" ...] -x ["ext1" "ext2" ...] -Pub path/to/public.key -DEL # encrypte and delete originals(-DEL) after encryption.
    python cryptor.py -d -f ["file1" "path1" ...] -Priv path/to/private.key # decrypt files and then remove encrypted ones.
    ''')

def main():
    parser = argparse.ArgumentParser(description='File Encryptor and Decryptor',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''Example:
    python cryptor.py -g path/to/save/rsa_keys # Generating RSA Public and RSA Private Keys
    python cryptor.py -e -f ["file1" "path1" ...] -x ["ext1" "ext2" ...] -Pub path/to/public.key -DEL # encrypte and delete originals(-DEL) after encryption.
    python cryptor.py -d -f ["file1" "path1" ...] -Priv path/to/private.key -DEL # decrypt files and then remove encrypted ones.
    '''))

    parser.add_argument('-g', '--generate', help='set path to generating RSA priv/public keys and save them.')
    parser.add_argument('-e', '--encrypt', action='store_true', help='Set script to encrypt files.')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Set script to decrypt files.')
    parser.add_argument('-f', '--files', nargs='+',help='Pass directory/file to decrypt/encrypt.')
    parser.add_argument('-x', '--extension', nargs='+', help='Set script to look for specific files.')
    parser.add_argument('-priv', '--PrivateKey', help='Pass directory to private.key.')
    parser.add_argument('-pub', '--PublicKey', help='Pass directory to public.key.')
    parser.add_argument('-DEL', '--DELETE', action='store_true', help='WILL REMOVE ORIGINAL FILES AFTER ENCRYPTING IT.')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        usage()

    # call a function to handle arguments
    handle_arguments(args)

if __name__ == '__main__':
    main()