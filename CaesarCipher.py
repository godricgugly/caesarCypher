import string
import copy
from random import randint

alphabet = string.ascii_lowercase + string.ascii_lowercase
text = list(input("input text: \n").lower())
action = input("encrypt (write: e) or decipher (write: d) \n").lower()
if action == "e":
    shiftNum = int(input("number of  shifts \n"))%25

run = True
while run == True:
    if action == "e":
        for index, letter in enumerate(text):
            if letter.isalpha():
                newLetter = alphabet.index(text[index]) + shiftNum
                text[index] = alphabet[newLetter]
        print ("\nYour cipher text: ")
        print ("".join(map(str,text))) 
        run = False
        
    if action == "d":
        attemptText = copy.deepcopy(text)
        startNum = randint (0, 25)
        for num in range(1, 26):
            shiftNum = (startNum + num) %25
            if shiftNum == 0:
                continue
            for i, letter in enumerate(text):
                if letter.isalpha():
                    newLetter = alphabet.index(text[i]) - shiftNum
                    attemptText[i] = alphabet[newLetter]
            print ("Attempt: ", num)
            print ("".join(map(str, attemptText))) 
            correct = input("does this look correct? y/n \n")
            if correct == "y":
                run = False
                print("\nYour cipher was encrypted by shifting each letter", shiftNum, " times.")
                print ("Original cipher text: ","".join(map(str, text)))
                print ("\nDeciphered text: ", "".join(map(str, attemptText)))
                break
            if num == 25 and correct != "y":
                print("your cipher seems to be gibberish!")
        run = False
    
    if action != "e" and action != "d":
        tryAgain = input("something went wrong, try again? y/n \n")
        if tryAgain == "y":
            text = list(input("input text: \n").lower())
            action = input("encrypt (write: e) or decipher (write: d): \n").lower()
            if action == "e":
                shiftNum = int(input("number of  shifts \n"))%25
        else:
            run = False
