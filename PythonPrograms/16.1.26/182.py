import re
#*regex question

def regex_finder(string1):
    '''Accepts a string and prints uppercase letters , lowercase letters , special characters , numbers '''
    lowercaseLetters = re.findall("[a-z]", string1)
    uppercaseLetters = re.findall("[A-Z]",string1)
    specialCharacters = re.findall("[^\w]",string1)
    numberCharacters = re.findall("[\d]+",string1)

    print("Lowercase ->"+str(lowercaseLetters))
    print("Uppercase ->"+str(uppercaseLetters))
    print("Special Characters ->"+str(specialCharacters))
    print("Numbers ->"+str(numberCharacters))
    




regex_finder("abcA@123")