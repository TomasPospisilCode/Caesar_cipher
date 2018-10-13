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
        elif usrText.isalpha():
            return True
        else:
            errorMessage = "Imput is not alphanumeric you prick!"
            self.errorMessageSetter(errorMessage)
            return False

    # Takes input text from user - if not correct, prompt user again, if correct, return text
    def usrInputText(self):
        while (True):
            usrText = input("Enter text you want to cipher: ")
            if self.isInputValid(usrText):
                return usrText
            else:
                print(self.errorMessage)

    def printText(self, usrText):
        print("User entered this text: " + usrText)

#Takes alphabet shift
def usrAlphabetShift():
    input("Enter shift: ")


#Includes all function
def Program():
    inputChecker = InputChecker()
    usrText = inputChecker.usrInputText()
    inputChecker.printText(usrText)

Program()