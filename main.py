import argparse
import pyperclip
from encrypt import generate_key, encrypt, decrypt

parser = argparse.ArgumentParser(description='Encrypt or decrypt a message with AES-128')
parser.add_argument("--encrypt", metavar="TEXT", help="Text to Encrypt.")
parser.add_argument("--decrypt", metavar="ENCRYPTED", help="Text to Decrypt.")
parser.add_argument("--key", metavar="KEY", help="Key for Encryption/Decryption.")
parser.add_argument("--generate-key", action="store_true", help="Generate a new key.")

args = parser.parse_args()

if args.generate_key:
    key = generate_key().decode()
    pyperclip.copy(key)
    print("New key:", key)
    print("Key copied to clipboard")

elif args.encrypt and args.key:
    print("Encrypted message:", encrypt(args.encrypt, args.key.encode()))

elif args.decrypt and args.key:
    print("Decrypted message:", decrypt(args.decrypt.encode(), args.key.encode()))