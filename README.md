# Cybersecurity Symetric Encryption Tool
A simple CLI application for generating AES-128 keys and encrypting and decrypting text.
Using symmetric encryption.
<br>
The application uses the cryptography library (Fernet) for AES-128 Encryption. 

<h3>Dependencies:</h3>
``` pip install cryptography ```

``` pip install pyperclip ```

<h3>Features</h3>
- Generate Encryption Key: 

```main.py --generate-key```

On key generation, the key is automatically copied to the clipboard.

- Encrypt a Message:

```main.py --encrypt "[YOUR MESSAGE TO ENCRYPT]" --key "[YOUR ENCRYPTION KEY]"```

- Decrypt a Message:

```main.py --decrypt "[YOUR ENCRYPTED MESSAGE]" --key "[YOUR ENCRYPTION KEY]"```


<h3>Encryption Method</h3>
- **Algorithm:** AES-128 in CBC mode (via Fernet).
- **Why Fernet?**
  - Built-in integrity checking (HMAC).
  - Simple API for secure symmetric encryption.
  - Actively maintained and widely trusted.

<h3>Key Management</h3>
- **Generation:** Random 128-bit key using `Fernet.generate_key()`.
- **Storage:** Keys are **not stored** by the application. Users must securely store and share keys themselves.
- **Security Implications:**
  - If the key is lost, encrypted data is unrecoverable.
  - Keys must be shared securely (e.g., encrypted channels, in-person).

<h3>Kerckhoff's Principle</h3>
This tool adheres to Kerckhoffs's Principle:
- The algorithm (AES-128) and implementation (Fernet) are publicly known.
- Security relies **only** on the secrecy of the key, not the obscurity of the system.