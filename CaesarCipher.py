def encrypt(oldmessage, newmessage):
	key = int(input('Enter your key: ')) #store key
	for letter in oldmessage:
		if ord(letter) in range(65,91): #upper case
			x = ord(letter) + key
			while x > 90: # past Z
				# while loop in case of large key
				x -= 26
			newmessage += chr(x)

		elif ord(letter) in range(97,123): #lower case
			x = ord(letter) + key
			while x > 122: # past z
				x -= 26
			newmessage += chr(x)
		
		else:
			newmessage += letter
	return newmessage


def decrypt(oldmessage, newmessage):
	known = input('Do you have a key? (y/n): ')
	if known == 'y':
		key = int(input('Enter your key: ')) #store key
		for letter in oldmessage:
			if ord(letter) in range(65,91): #upper case
				x = ord(letter) - key
				while x < 65: # past Z
					# while loop in case of large key
					x += 26
				newmessage += chr(x)

			elif ord(letter) in range(97,123): #lower case
				x = ord(letter) - key
				while x < 97: # past z
					x += 26
				newmessage += chr(x)
			
			else:
				newmessage += letter
	else:
		pass
	return newmessage
givenmessage = input('Enter your message: ')
newmessage = ""

decision = input('Would you like to encrypt (e) or decrypt (d)? ')
if decision == 'd':
  print(decrypt(givenmessage, newmessage))
elif decision == 'e':
  print(encrypt(givenmessage, newmessage))
else:
  print("Not a valid response")
