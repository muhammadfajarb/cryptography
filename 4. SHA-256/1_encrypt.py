from Crypto.Hash import SHA256

password = b'IniP@sswordS4y4'
hash_object = SHA256.new(data=password)

encrypted_data = hash_object.hexdigest()
print(encrypted_data)

file_out = open("encrypted_password.txt", "wb")
file_out.write(encrypted_data.encode())
file_out.close()