This project is about encryption and decryption of strings
I have imported some libraries such as cryprography ,fernet and rsa that have enabled the decyption and encryption process of the message
Encryption is the process of encoding the data. i.e converting plain text into ciphertext. This conversion is done with a key called an encryption key.
Decryption is the process of decoding the encoded data. Converting the ciphertext into plain text. This process requires a key that we used for encryption.
There are two main types of keys used for encryption and decryption. They are Symmetric-key and Asymmetric-key.

Symmetric-key Encryption:
In symmetric-key encryption, the data is encoded and decoded with the same key. This is the easiest way of encryption, but also less secure. The receiver needs the key for decryption, so a safe way need for transferring keys. Anyone with the key can read the data in the middle.
  I used this library called cryptography
   pip install cryptography
   from cryptography.fernet import fernet

Asymmetric-key Encryption:
In Asymmetric-key Encryption, we use two keys a public key and a private key. The public key is used to encrypt the data and the private key is used to decrypt the data. By the name, the public key can be public (can be sent to anyone who needs to send data). No one has your private key, so no one in the middle can read your data.
  I used this library called rsa
    pip install rsa
    import rsa