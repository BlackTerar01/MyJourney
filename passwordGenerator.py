import random

# creating new password file which will store all passwords
passwordFile = open("passwordFile.txt", 'a')
# define Uppercase letters, lowercase, ints and special characters
upperCaseArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerCaseArray = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numArray = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specialChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", ":", ";", "<", ">", "?"]
listOfOptions = ["upperCaseArray", "lowerCaseArray", "numArray", "specialChars"]
# ask password details
numOfChars = int(input("How many characters do you wish to have? "))
passFor = input("What is this password for? Name of website/app: ")

passwordFile.write(passFor + " - ")

passwordSet = []

def set_password():
    for x in range(numOfChars):
        charType = random.choice(listOfOptions)
        match charType:
            case "upperCaseArray":
                character = random.choice(upperCaseArray)
            case "lowerCaseArray":
                character = random.choice(lowerCaseArray)
            case "numArray":
                character = random.choice(numArray)
            case "specialChars":
                character = random.choice(specialChars)
        passwordSet.append(character)
        passwordFile.write(character)

    passwordFile.write("\n")
    passwordFile.close()
    return(passwordSet)

print(set_password())