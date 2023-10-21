from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Fungsi untuk mengenkripsi file
def encrypt_file(input_file, output_file, key):
    chunk_size = 64 * 1024
    init_vector = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, init_vector)

    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        outfile.write(init_vector)

        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += b' ' * (16 - len(chunk) % 16)

            outfile.write(cipher.encrypt(chunk))

# Key AES yang digunakan (harus 16, 24, atau 32 byte)
key = b'ContohPasswordOK'

# Penggunaan:
input_file = 'moon.jpg'
encrypted_file = 'file_encrypted.bin'

encrypt_file(input_file, encrypted_file, key)
