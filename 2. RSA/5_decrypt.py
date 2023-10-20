from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

ciphertext = b'???'

# Baca kunci private dari file
with open("private_key.pem", "rb") as file:
    private_key = RSA.import_key(file.read())

# Mendekripsi pesan
decipher = PKCS1_OAEP.new(private_key)
decrypted_message = decipher.decrypt(ciphertext)

print("Decrypted message:", decrypted_message.decode("utf-8"))