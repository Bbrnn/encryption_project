"""
Asymmetric encryption: is a type of encryption that uses two different keys for encryption and decryption.

Steps:
Import rsa library
Generate public and private keys with rsa.newkeys() method.
Encode the string to byte string.
Then encrypt the byte string with the public key.
Then the encrypted string can be decrypted with the private key.
The public key can only be used for encryption and the private can only be used for decryption
"""
import rsa
message ="I love all aspects of cybersecurity✌"

# Generate a key for encryption and decryption
#the key length must be atleast 16
public_key, private_key = rsa.newkeys(512)
#print("This is the public key:",public_key)
#print("This is the private key:",private_key)

#Original message
print("Original message:",message)

# Encrypt the message with the public key
encoded_message = rsa.encrypt(message.encode(),public_key)
print("Encoded message:",encoded_message)

# Decrypt the message with the private key
decoded_message =rsa.decrypt(encoded_message,private_key).decode()
print("Decoded message:",decoded_message)