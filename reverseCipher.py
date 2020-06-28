# Reverse Cipher
# Taken from inventwithpython.com/cracking/chapter4.html
# can also be achieved by message[::-1]

print("###################")
print("# Reverse Cipher! #")
print("###################\n")

message = input("Enter the message you wish to encrypt... ")
encrypted = ""

i = len(message) - 1
while i >= 0:
	encrypted += message[i]
	i -= 1

print(encrypted)
