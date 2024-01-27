"""
Steps:

Import Fernet
Then generate an encryption key, that can be used for encryption and decryption.
Convert the string to a byte string, so that it can be encrypted.
Instance the Fernet class with the encryption key.
Then encrypt the string with the Fernet instance.
Then it can be decrypted with Fernet class instance and it should be instanced with the same key used for encryption.

"""
from cryptography.fernet import Fernet

message ="I love all aspects of cybersecurity✌"

# Generate a key for encryption and decryption
key = Fernet.generate_key()
#print("This is the key:",key)-you can view the key by removingthe comment and running the program

# Instance the Fernet class with the key
f = Fernet(key)

#the original message
print("Original message:",message)

# Encrypt the message
encrypted_message = f.encrypt(message.encode())
print("Encrypted message:",encrypted_message)

# Decrypt the message
decrypted_message = f.decrypt(encrypted_message).decode()
print("This is the decrypted message",decrypted_message)

