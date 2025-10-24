import argparse
from encrypt import generate_key, encrypt, decrypt

parser = argparse.ArgumentParser(description='Encrypt or decrypt a message with AES-128')
parser.add_argument("--encrypt", metavar="TEKST", help="Text to Encrypt.")
parser.add_argument("--decrypt", metavar="VERSLEUTELD", help="Text to Decrypt.")
parser.add_argument("--key", metavar="SLEUTEL", help="Key for Encryption/Decryption.")
parser.add_argument("--generate-key", action="store_true", help="Generate a new key.")

args = parser.parse_args()
if args.generate_key:
    print("New key:", generate_key().decode())
elif args.encrypt and args.key:
    print("Encrypted:", encrypt(args.encrypt, args.key.encode()))
elif args.decrypt and args.key:
    print("Decrypted:", decrypt(args.decrypt.encode, args.key.encode()))