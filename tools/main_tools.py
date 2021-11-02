from .encryptor import encrypt
from .decryptor import decrypt
from .helpers import generate
from rich import print
import os

def handle_directory(dir):
    """
    Will get all files in a directory and return them as a list
    """
    files_list = []
    for root, _, files in os.walk(dir, topdown=False):
        for name in files:
            full_filename = os.path.join(root, name)
            files_list.append(full_filename)
    return(files_list)

def handle_arguments(args):
    """
    a function for handling command line arguments.
    """
    if args.generate:
        print('[green][*] Generating RSA keys...[/green]')
        generate(args.generate)
        print(f'[blue][*] RSA keys has been generated and saved to {args.generate}[/blue]')
    
    if args.encrypt:
        for f in args.files:
            # check if it's a file
            if os.path.isfile(f):
                if args.extension:
                    if os.path.splitext(f)[1] not in args.extension:
                        continue
                print(f'[green][*] Encrypting {f}...[/green]')
                encrypt(f, args.PublicKey)
                print(f'[blue][*] {f} encrypted.[/blue]')
                if args.DELETE:
                    os.remove(f)
            # check if it's a directory
            elif os.path.isdir(f):
                # handling directory
                files = handle_directory(f)
                for file in files:
                    if args.extension:
                        if os.path.splitext(file)[1] not in args.extension:
                            continue
                    print(f'[green][*] Encrypting {file}...[/green]')
                    encrypt(file, args.PublicKey)
                    print(f'[blue][*] {file} encrypted.[/blue]')
                    if args.DELETE:
                        os.remove(file)
    
    elif args.decrypt:
        for f in args.files:
            # check if it's a file
            if os.path.isfile(f):
                # check if file is encrypted
                if os.path.splitext(f)[1] != '.encrypted':
                    continue
                print(f'[green][*] Decrypting {f}...[/green]')
                decrypt(f, args.PrivateKey)
                print(f'[blue][*] {f} decrypted.[/blue]')
                os.remove(f) 
            # check if it's a directory
            elif os.path.isdir(f):
                # handling directory
                files = handle_directory(f)
                for file in files:
                    if os.path.splitext(file)[1] != '.encrypted':
                        continue
                    print(f'[green][*] Decrypting {file}...[/green]')
                    decrypt(file, args.PrivateKey)
                    print(f'[blue][*] {file} decrypted.[/blue]')
                    os.remove(file)