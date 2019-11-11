def main():
	print("Welcome to Caesar shift\n")
	print("=======================\n")
	print("1. Encrypt\n2. Decrypt\n3. Read a file")

	option = int(input("Option: "))

	message = input("Please write your message: ")
	shift = int(input("Enter a shift value: "))

	if option == 1:
		encrypt(message, shift)
	elif option == 2:
		decrypt(message, shift)
	elif option == 3:
		fileRead()
	else:
		print ("Error- Incorrect input")
		main()
	
def encrypt(message, shift):
	encrypted = ''
	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) + shift
				if num > ord('z') :
					num -= 26
					encrypted += chr(num)
				else:
					encrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i]) + shift	
				if num > ord('Z') :
					num -= 26
					encrypted += chr(num)
				else:
					encrypted += chr(num)
		elif ord(message[i]) == 32:
			encrypted += ' '
		else:
			encrypted += message[i]

	fileWrite(encrypted)

def decrypt(message, shift):
	decrypted = ''
	for i in range(len(message)):
		if message[i].isalpha():
			if message[i].islower():
				num = ord(message[i]) + shift
				if num > ord('z') :
					num -= 26
					decrypted += chr(num)
				elif num < ord('a'):
					num += 26
					decrypted += chr(num)
				else:
					decrypted += chr(num)
			elif message[i].isupper():
				num = ord(message[i]) + shift	
				if num > ord('Z') :
					num -= 26
					decrypted += chr(num)
				elif num < ord('A'):
					num += 26
					decrpyted += chr(num)
				else:
					decrypted += chr(num)
		elif ord(message[i]) == 32:
			decrypted += ' '
		else:
			decrypted += message[i]

def fileWrite(encrypted):
	file = open("Encryption.txt", "w")
	file.write(encrypted)
	file.close()
	print (f"Message {encrypted}, has succesfully been written to the file Encryption.txt")


def fileRead():
	message = ''
	file = open("Encryption.txt", "r")
	message += file.readline()
	shift = int(input("Enter shift value: "))
	file.close()
	decrypt(message, shift)


if __name__ == "__main__":
	main()