from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.PublicKey import RSA

from rich import print
import os
import sys

def get_rsa_cipher(path_to_key):
    """
    import rsa keys from given file.
    """
    with open(path_to_key) as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    return (PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes())

def generate(path_to_save):
    """
    Generates RSA Public Key and RSA Private Key.
    """
    new_key = RSA.generate(2048) # Generating key with size of 2048
    private_key = new_key.exportKey() # Exporting private key
    public_key = new_key.publickey().exportKey() # Exporting public key
    # Saving Keys
    try:
        with open(os.path.join(path_to_save, 'private.key'), 'wb') as f:
            f.write(private_key)
        with open(os.path.join(path_to_save, 'public.key'), 'wb') as f:
            f.write(public_key)     
    except Exception as e:
        print(f'[red][!][/red] An error occured during saving RSA keys: {e}')
        sys.exit()


def readfile(filepath):
    """
    read given file as binary and return results.
    """
    with open(filepath, 'rb') as file:
        contents_in_binary = file.read()
    return contents_in_binary
