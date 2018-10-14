''' ____                                  _       _
  / ___|__ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __
 | |   / _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | |__| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |
  \____\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|
                                          |_|
'''

#!/usr/bin/env
import string

#Class which contains functions for input checking
class InputChecker:
    #class variable
    errorMessage = ""

    #Constructor
    def __init__(self):
        pass

    #Getter and setter for error message
    def errorMessageSetter(self, value):
        self.errorMessage = value
    def errorMessageGetter(self):
        return self.errorMessage

    # Function that validates if user input is alphanumeric, if yes -> return true, if not -> set error message and return false
    def isInputValid(self, usrText):
        # If input is empty, return false
        if not usrText:
            errorMessage = "Imput is empty you prick!"
            self.errorMessageSetter(errorMessage)
            return False
        # If input is alphabetic only, return true

        elif usrText.replace(" ", "").isalpha():#We have to remove spaces
            return True
        else:
            errorMessage = "Imput is not alphanumeric you prick!"
            self.errorMessageSetter(errorMessage)
            return False
    def isShiftValid(self, alphabetShift):
        # If input is empty, return false
        if not alphabetShift:
            errorMessage = "You didn't enter any shift! you prick!"
            self.errorMessageSetter(errorMessage)
            return False
        # If input is numeric only, and if it is in correct range, return True
        elif alphabetShift.isnumeric():
            if int(alphabetShift) in range(1,27):#Range is from 1-26
                return True
            else:
                errorMessage = "Shift must be number from 1-26! You prick!"
                self.errorMessageSetter(errorMessage)
                return False
        else:
            errorMessage = "Imput is not numeric you prick!"
            self.errorMessageSetter(errorMessage)
            return False


    #Takes input text from user - if not correct, prompt user again, if correct, return text
    def usrInputText(self):
        while (True):
            usrText = input("Enter text you want to cipher: ")
            if self.isInputValid(usrText):
                return usrText
            else:
                print(self.errorMessage)

    # Takes alphabet shift
    def usrAlphabetShift(self):
        while(True):
            alphabetShift = input("Enter alphabet shift: ")
            if self.isShiftValid(alphabetShift):
                return alphabetShift
            else:
                print(self.errorMessage)

#Function that cipher text and return ciphered text
def doTheMagic(usrText, shift):
    cipheredText = ""

    for letter in usrText:
        # If there is space in text, we leave space also in ciphered text
        cipheredLetter = ""
        if letter ==  " ":
            cipheredLetter = " "
        else:
            #Default alphabet start and end, will change according if the letter is large or small
            alphabetStart = 0
            alphabetEnd = 0

            if ord(letter) in range(97,123):#97-122 - a-z
                alphabetStart = 97
                alphabetEnd = 122
            else:#Letters are big so A-Z
                alphabetStart = 65
                alphabetEnd = 90

            #Alphabet of small letters in ASCII is from 97 to 122
            #So if our ciphered can be more than 122 and less than 97
            #If it is, we must first count how distant is letter from end of alphabet, substract distance from shift and cipher letter by shift from the beginning of alphabet
            if (ord(letter) + int(shift)) > alphabetEnd:
                difference = alphabetEnd - (ord(letter))
                functionShift = int(shift) - difference#I had to assign shift to different variable otherwise it would lead to program fail
                cipheredLetter = chr(alphabetStart + (functionShift-1))#There must be -1 because in case 'overflow' letter would be shifted to one more character further
            else:
                # Convert actual letter to ASCII code, add shift and convert it back to letter
                cipheredLetter = chr(ord(letter) + int(shift))

        cipheredText += cipheredLetter

    return cipheredText

#Includes all function
def Program():
    inputChecker = InputChecker()#Initialization of class object
    usrText = inputChecker.usrInputText()#Save user text to variable
    shift = inputChecker.usrAlphabetShift()#Save alphabet shift to variable
    print("This is original text: " + usrText)
    print("This is user alphabet shift: " + shift)
    cipheredText = doTheMagic(usrText, shift)
    print("This is ciphered text: " + cipheredText)

Program()