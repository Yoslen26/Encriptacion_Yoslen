from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def encode(key, text):
    cipher = AES.new(key, AES.MODE_CBC)
    text_bytes = cipher.encrypt(pad(text.encode(), AES.block_size))
    vi = base64.b64encode(cipher.iv).decode('utf-8')
    text_encrypted = base64.b64encode(text_bytes).decode('utf-8')
    return vi, text_encrypted

def decode(key, iv, text):
    iv = base64.b64decode(iv)
    text = base64.b64decode(text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(text), AES.block_size)
    return pt.decode('utf-8')

key = get_random_bytes(32)
print("Ingrese un texto: ")
text = input()

iv, text_encoded = encode(key, text)

print("iv: ", iv)
print("Texto encriptado: ", text_encoded)

text_decoded = decode(key, iv, text_encoded)
print("Texto desencriptado: ", text_decoded)