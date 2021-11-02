from .helpers import readfile, get_rsa_cipher
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
import base64
import ntpath
import string
import random
import os

def encrypt(filepath, publicKeyPath):
    """
    our decryptor function.
    -payload- variable is consist of 6 main sections:
        --1th section is encrypted AES key that we need for decrypting data,
        --2th section is AES nonce that we need for recreating AES key,
        --3th section is tag that we need it for decrypting files(along with AES key)
        --4th section is filename size in bytes, we need it for extracting original filename
        --5th section is filename in bytes format.
        --6th section is our encrypted data(encrypted with AES)
    then we will base64 encode the whole payload and write it down to a file
    """
    head, filename = ntpath.split(filepath)
    filename_size = len(filename)
    filename_size_in_bytes = int.to_bytes(filename_size, 2, 'big')
    contents_in_binary = readfile(filepath)

    letters = string.ascii_letters
    new_random_filename = ''.join(random.choice(letters) for i in range(15))

    # create AES key
    session_key = get_random_bytes(16)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    # encrypt the compressed text
    cipherdata, tag = cipher_aes.encrypt_and_digest(contents_in_binary)

    cipher_rsa, _ = get_rsa_cipher(publicKeyPath) # Getting our public key
    encrypted_session_key = cipher_rsa.encrypt(session_key) # Encrypting AES Key with our RSA Public Key
    
    # This is our final encrypted data
    payload = encrypted_session_key + cipher_aes.nonce + tag
    payload += filename_size_in_bytes # 2 byte, it will contain the size of filename
    payload += bytes(filename, 'utf-8') # filename in bytes
    payload += cipherdata

    encrypted = base64.encodebytes(payload)
    output_path = os.path.join(head, new_random_filename)
    with open(f"{output_path}.encrypted", 'wb') as output:
        output.write(encrypted)
    return(encrypted)

