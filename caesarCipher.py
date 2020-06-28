# Caesar Cipher
# Taken from inventwithpython.com/cracking/chapter5.html

from pyperclip import copy

# The string to be encrypted or decrypted
message = input("What is your message?\n")

# Set to "encrypt" or "decrypt", for
# encryption or decryption, respectively
mode = input("encrypt or decrypt: ").lower()

# The key
key = int(input("What is your " + mode + "ion key? "))

# Every single symbol that can be encrypted
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# To increase the encryption level, if desired
# SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/"

# To store the new text
translated = ""
translated_index = 0

for symbol in message:

    # NB: Only symbols in SYMBOLS can
    # be encrypted/decrypted
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)

        # Perform encryption or decryption
        if mode == "encrypt":
            translated_index = symbol_index + key
        elif mode == "decrypt":
            translated_index = symbol_index - key

        # In case SYMBOLS needs to wrap around
        if translated_index >= len(SYMBOLS):
            translated_index -= len(SYMBOLS)
        elif translated_index < 0:
            translated_index += len(SYMBOLS)

        translated += SYMBOLS[translated_index]
        
    else:

        # Append the symbol without encrypting or decrypting
        translated += symbol

# Output the translated string
print("Your " + mode + "ion returned:\n" + translated)
copy(translated)
