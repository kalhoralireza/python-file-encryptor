# python-file-encryptor

A hybrid(AES + RSA) encryptor in python.
Tasted on Windows and Linux(Kali).

## Install Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install pycryptodome rich
```
## Usage
```bash
python cryptor.py -g path/to/save/rsa_keys # Generating RSA Public and RSA Private Keys
python cryptor.py -e -f ["file1" "path1" ...] -x ["ext1" "ext2" ...] -Pub path/to/public.key -DEL # encrypte and delete originals(-DEL) after encryption.
python cryptor.py -d -f ["file1" "path1" ...] -Priv path/to/private.key # decrypt files and then remove encrypted ones.
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
