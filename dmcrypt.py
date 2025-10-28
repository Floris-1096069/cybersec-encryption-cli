import argparse
import pyperclip
from cryptography.fernet import Fernet

parser = argparse.ArgumentParser(description='Encrypt or decrypt a message with AES-128')
parser.add_argument("--encrypt", metavar="TEXT", help='python dmcrypt.py --encrypt "[YOUR MESSAGE TO ENCRYPT]" --key "[YOUR ENCRYPTION KEY]"')
parser.add_argument("--decrypt", metavar="ENCRYPTED", help='python dmcrypt.py --decrypt "[YOUR ENCRYPTED MESSAGE]" --key "[YOUR ENCRYPTION KEY]"')
parser.add_argument("--key", metavar="KEY", help="Key argument for Encryption/Decryption.")
parser.add_argument("--generate-key", action="store_true", help="Generate a new key and copy to clipboard")

args = parser.parse_args()

def generate_key():
    return Fernet.generate_key()

def encrypt(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt(message, key):
    f = Fernet(key)
    return f.decrypt(message).decode()

try:
    if args.generate_key:
        key = generate_key().decode()
        pyperclip.copy(key)
        print("New key:", key)
        print("Key copied to clipboard")

    elif args.encrypt and args.key:
        print("Encrypted message:", encrypt(args.encrypt, args.key.encode()))

    elif args.decrypt and args.key:
        print("Decrypted message:", decrypt(args.decrypt.encode(), args.key.encode()))

    else:
        parser.print_help()

except Exception as e:
    print(f"Error: {str(e)}. Check your key and input.")