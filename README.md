# Cybersecurity Symetric Encryption Tool
A simple CLI tool for generating AES-128 keys and encrypting and decrypting text, using symmetric encryption.

This tool uses the cryptography library (Fernet) for AES-128 Encryption. 

<h3>Dependencies:</h3>

``` pip install cryptography ```

``` pip install pyperclip ```

<h3>Features</h3>

- Help command:

```python main.py --help```

- Generate Encryption Key: 

```python main.py --generate-key```

On key generation, the key is automatically copied to the clipboard.

- Encrypt a Message:

```python main.py --encrypt "[YOUR MESSAGE TO ENCRYPT]" --key "[YOUR ENCRYPTION KEY]"```

- Decrypt a Message:

```python main.py --decrypt "[YOUR ENCRYPTED MESSAGE]" --key "[YOUR ENCRYPTION KEY]"```


<h3>Encryption Method</h3>

- **Algorithm:** AES-128 in CBC mode (via Fernet).
    
- **Why Fernet?**
  - Built-in integrity checking (HMAC).
  - Simple API for secure symmetric encryption.
  - Actively maintained and widely trusted.

<details>

```Fernet.generate_key()``` generates a 256-bit key (32 bytes).
- This key gets split into 2 parts internally:
  - 128 bits for the AES-128 encryption of the message.
  - 128 bits for HMAC-SHA256 which is used for integrity and authentication.
- The key is encoded in base64 for easy exchange while staying crypthographically strong.

A Fernet message consists of the following components (all base64-encoded and concatenated with a $ separator):
```Version (8 bits) | Timestamp (64 bits) | IV (128 bits) | Ciphertext | HMAC (256 bits)```
- Version identifies the Fernet Protocol version.
- Timestamp prevents replay attacks by limiting the messages validity.
- IV (Initialization Vector) is a random value ensuring the same input does not produce the same ciphertext twice.
- Ciphertext is the actual encrypted data using AES-128-CBC.
- HMAC is a hash-based message authentication code (SHA256) that verifies the message's integrity.

Fernet is secure because:

- AES-128 is a well-tested and widely accepted symmetric algorithm. While AES-256 is theoretically stronger, AES-128 is already secure enough for most applications and is faster.
- HMAC-SHA256 protects against message tampering (e.g., by a man-in-the-middle attacker).
- Per-message IV ensures semantic security—identical messages produce different ciphertexts.
- The timestamp prevents replay attacks by limiting the message's validity period.

</details>

<h3>Key Management</h3>

- **Generation:** Random 128-bit key using `Fernet.generate_key()`.

- **Storage:** Keys are **not stored** by the application. Users must securely store and share keys themselves.

  - I actively chose to keep Key storage in the hands of the user. To keep the tool both flexible for multiple usecases and keep the tool as simple as possible.
  
- **Security Implications:**
  - If the key is lost, encrypted data is unrecoverable.
  - Keys must be shared securely (e.g., encrypted channels, in-person).
  - If keys aren't shared trough a secure channel, through email for example, messages can be compromised by a third party.
  - On the upside, keys can be kept completely analogue. Including an option to share keys by pigeon post.

<h3>Kerckhoff's Principle</h3>
This tool adheres to Kerckhoffs's Principle:
- The algorithm (AES-128) and implementation (Fernet) are publicly known.
- Security relies **only** on the secrecy of the key, not the obscurity of the system.

<h3>Link to github repo:</h3>
https://github.com/Floris-1096069/cybersec-encryption-cli