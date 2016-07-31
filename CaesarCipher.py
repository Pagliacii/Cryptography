#!/usr/bin/env python3
#_*_ coding : utf-8 _*_
# author : jason huang
# version: 1.0

char_list = [s for s in 'abcdefghijklmnopqrstuvwxyz']

def Caesarcipher(Strings, num=0, mode='decrypt'):
	char = [c.lower() for c in Strings]
	if mode == 'decrypt':
		plaintext = []
		for ch in char:
			index = char_list.index(ch)
			plaintext.append(char_list[(index + num) % 26])

		print(('%s' if num > 9 else ' %s') % num + " " + ''.join(plaintext))
		return None
	else:
		ciphertext = []
		for ch in char:
			index = char_list.index(ch)
			ciphertext.append(char_list[(index + num) % 26].upper())

		ciphertext = ''.join(ciphertext)
		return ciphertext

if __name__ == '__main__':
	'''
	ciphertext = 'PELCGBTENCUL'
	for num in range(26):
		Caesarcipher(ciphertext, num)
	'''
	plaintext = 'helloworld'
	ciphertext = Caesarcipher(plaintext, 15, 'encrypt')
	print(ciphertext)
	#for num in range(26):
	#	Caesarcipher(Caesarcipher(plaintext, 15, 'encrypt'), num)