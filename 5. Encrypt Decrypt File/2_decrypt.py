from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Fungsi untuk mendekripsi file
def decrypt_file(input_file, output_file, key):
    chunk_size = 64 * 1024

    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        init_vector = infile.read(16)
        cipher = AES.new(key, AES.MODE_CBC, init_vector)

        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            decrypted_chunk = cipher.decrypt(chunk)
            outfile.write(decrypted_chunk)

# Key AES yang digunakan (harus 16, 24, atau 32 byte)
key = b'ContohPasswordOK'

# Penggunaan:
encrypted_file = 'file_encrypted.bin'
decrypted_file = 'file_decrypted.jpg'

decrypt_file(encrypted_file, decrypted_file, key)
