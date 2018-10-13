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

#Includes all function
def Program():
    inputChecker = InputChecker()#Initialization of class object
    usrText = inputChecker.usrInputText()#Save user text to variable
    shift = inputChecker.usrAlphabetShift()#Save alphabet shift to variable
    print("This is user text: " + usrText)
    print("This is user alphabet shift: " + shift)

Program()