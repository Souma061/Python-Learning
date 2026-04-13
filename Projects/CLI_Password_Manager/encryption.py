from cryptography.fernet import Fernet
import base64
import hashlib


# key = Fernet.generate_key()
# print(f"Generated key: {key.decode()}")
# print(key)
# cipher = Fernet(key)

# # Encrypt a message
# message = "Password123"
# encrypt = cipher.encrypt(message.encode())
# print(f"Encrypted message: {encrypt.decode()}")
# devrypt = cipher.decrypt(encrypt).decode()
# print(f"Decrypted message: {devrypt}")


def generate_key(master_pass):
    key = hashlib.sha256(master_pass.encode()).digest()
    return base64.urlsafe_b64encode(key)


def get_cipher(master_pass):
    key = generate_key(master_pass)
    return Fernet(key)


def encrypt_pass(password,master_pass):
    cipher = get_cipher(master_pass)
    return cipher.encrypt(password.encode()).decode()



def decrypt_pass(encrypted_pass, master_pass):
    cipher = get_cipher(master_pass)
    return cipher.decrypt(encrypted_pass.encode()).decode()


# Fernet expects a 32-byte key, so we hash the master password to create a consistent key length. The encrypted data is stored as a string for easy storage in JSON.

