from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Buat pasangan kunci RSA (untuk demonstrasi)
key = RSA.generate(2048)

# Buat objek kunci public dan private
private_key = key.export_key()
public_key = key.publickey().export_key()

# Simpan kunci public dan private ke dalam file
with open("private_key.pem", "wb") as private_file:
    private_file.write(private_key)

with open("public_key.pem", "wb") as public_file:
    public_file.write(public_key)

# Pesan yang akan dienkripsi
message = b'Ini adalah pesan rahasia.'

# Baca kunci public dari file
with open("public_key.pem", "rb") as file:
    public_key = RSA.import_key(file.read())

# Enkripsi pesan menggunakan kunci public
cipher = PKCS1_OAEP.new(public_key)
ciphertext = cipher.encrypt(message)

print("Ciphertext:", ciphertext)