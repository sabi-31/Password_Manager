import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# salt = os.urandom(16)      Salt is not randomly generated as of this implementation


def encrypt_vault(name,password):
    """
	This function will encrypt an user's vault

	Args:
        name: name of the user
        password: password of the user, used for encryption

	Returns:
		None
	"""
    password_in_bytes = bytes(password, 'utf-8')
    vault_name = 'User-Data/.' + name + '.txt'
    salt = b'\xe7\xf5\xdd"o \x98\xaf\xc4\xaf\x80"0\xa6\xb8P'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=390000,)
    key = base64.urlsafe_b64encode(kdf.derive(password_in_bytes))
    f = Fernet(key)
    
    with open(vault_name, 'rb') as file:
        original = file.read()
    
    encrypted = f.encrypt(original)

    with open(vault_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt_vault(name, password):
    """
	This function will decrypt an user's vault

	Args:
        name: name of the user
        password: password of the user, used for encryption

	Returns:
		None
	"""
    password_in_bytes = bytes(password, 'utf-8')
    vault_name = 'User-Data/.' + name + '.txt'
    salt = b'\xe7\xf5\xdd"o \x98\xaf\xc4\xaf\x80"0\xa6\xb8P'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=390000,)
    key = base64.urlsafe_b64encode(kdf.derive(password_in_bytes))
    f = Fernet(key)
    
    with open(vault_name, 'rb') as file:
        encrypted = file.read()
    
    original = f.decrypt(encrypted)

    with open(vault_name, 'wb') as decrypted_file:
        decrypted_file.write(original)