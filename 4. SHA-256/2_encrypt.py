from Crypto.Hash import SHA256

user_input = input("Masukkan password anda: ")
byte_input = user_input.encode()  # Mengonversi string ke byte string
hash_object = SHA256.new(data=byte_input)

encrypted_input = hash_object.hexdigest().encode()

password_hash = open("encrypted_password.txt", "rb").read()

print('Encrypted Input : ' + encrypted_input.decode())
print('Password Hash   : ' + password_hash.decode())

if (encrypted_input.decode() == password_hash.decode()):
    print('Status : Valid')
else:
    print('Status : Tidak Valid')


