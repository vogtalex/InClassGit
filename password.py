import string
import random

def generatePassword(num):
	char = string.ascii_letters
	randString = ''.join(random.choice(char) for i in range(num))
	print(randString)


print('\nWelcome to the password generator program')
num = int(input("Enter a number to generate a password of your designated length: "))

generatePassword(num)