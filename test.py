'''
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import os

asdd = input(" >> ")
asd = "'" + asdd + "'"
salt = os.urandom(16)
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000,)
key = base64.urlsafe_b64encode(kdf.derive(b'asdd'))
print(key)
message = "Hello World".encode()
key_obj = Fernet(key)
encrypted_message = key_obj.encrypt(message)
print(encrypted_message)
decrypted_message = key_obj.decrypt(encrypted_message)
print(decrypted_message)
'''
'''
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64

asdd = input(" >> ")

backend = default_backend()
salt = os.urandom(16)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
    backend=backend
)
key = base64.urlsafe_b64encode(kdf.derive(b'asdd'))

f = Fernet(key)
print(key)
'''


import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def get_key(password):

    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())

def encrypt(password, token):
    f = Fernet(get_key(password))
    return f.encrypt(bytes(token))

def decrypt(password, token):
    f = Fernet(get_key(password))
    return f.decrypt(bytes(token))

password = input(" >> ")
get_key(password)
