
import string

alphabet = string.ascii_lowercase + string.ascii_lowercase

text = list(input("input text: \n").lower())

action = input("encrypt or decipher \n").lower()

if action == "encrypt":
    shiftNum = int(input("number of  shifts \n"))%25


run = True

while run == True:
    if action == "encrypt":
        for index, letter in enumerate(text):
            if letter.isalpha():
                newLetter = alphabet.index(text[index]) + shiftNum
                text[index] = alphabet[newLetter]
        print ("".join(map(str,text))) 
        run = False
    if action == "decipher":
        for index, letter in enumerate(text):
            if letter.isalpha():
                newLetter = alphabet.index(text[index]) - shiftNum
                text[index] = alphabet[newLetter]
        print ("".join(map(str,text))) 
        run = False
    if action != "encrypt" and action != "decipher":
        tryAgain = input("something went wrong, try again? y/n \n")
        if tryAgain == "y":
            text = list(input("input text: \n").lower())
            action = input("encrypt, decipher or exit: \n").lower()
            if action == "encrypt":
                shiftNum = int(input("number of  shifts \n"))%25
        else:
            run = False
