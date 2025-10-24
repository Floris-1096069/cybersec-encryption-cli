from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt(message, key):
    f = Fernet(key)
    return f.decrypt(message).decode()