import re

def encrypt(text, key):
	text = text.strip()

	if " " in text:
		words = list(text)
		print("testing",words)

		text.replace(' ', ' ss')
	else:
		words = text

	text = list(text)

	letter_tracker = 0


	encrypted_list = []
	#Loop through the string values
	for text in words:
		for letter in text:

			letter = ord(letter)
			new_letter = letter + key
			if letter == "":
				encrypted_list.append(" ")


			#Convert back to character
			letter = chr(new_letter)
			encrypted_list.append(letter)
	# e_word = ''
	encrypted_list


	result = "".join(encrypted_list)
	return str(result)




def decrypt(encrypted, key):
	text = list(text)

	encrypted_word = ""
	encrypted_list = ""
	# Loop through the string values
	for letter in text:
		letter = ord(letter)

		# Increment letter value by # of integers
		new_letter = letter + key

		# Convert back to character
		letter = chr(new_letter)
		encrypted_list = decrypted_list + letter
	for letter in decrypted_list:
		decrypted_list = decrypted_list + letter

	return str(decrypted_list)

	pass

def crack(encrypted):


	pass

# #Expected Output: 'movg'
#
# print("Gina encoded is:" + str(a))

a = encrypt('bqqmft boe cbobobt', 2)

print(a)