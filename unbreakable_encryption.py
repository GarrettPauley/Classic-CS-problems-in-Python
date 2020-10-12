"""A one-time pad is a cryptographic tool that produces an 
unbreakable encryption if certain conditions  are met.  """

""" In this program, a string will be encrypted using a one-time pad. """

from secrets import token_bytes
from typing import Tuple
#We will use python's encode() method to turn the string into a series of UTF-8 bytes. 

def random_key(length): 
    #generate random bytes of a given length. 
    #token_bytes is a psuedo-random number generator, which will suffice for encryption
    tb = token_bytes(length)
    #convert those bytes to a bit string.
    # "big" is an argument that places the most significant bit at the beginning  
    return int.from_bytes(tb, "big") 

def encrypt(original): 
    #Turn the message into UTF-8
    original_bytes = original.encode()
    #
    dummy_data = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted = original_key ^ dummy_data #XOR operator performed on original message 
    return dummy_data, encrypted

def decrypt(key_1, key_2): 
    decryption = key_1 ^ key_2 #another XOR, 
    temp = decryption.to_bytes((decryption.bit_length()+7 )//8, "big")
    return temp.decode()

if __name__ == "__main__":
    key_1,key_2 = encrypt("Hello Comrade.")
    result = key_1
    result2 = key_2
    cleartext = decrypt(key_1, key_2)
    
    print(result)
    print(result2)
    print(cleartext)
    