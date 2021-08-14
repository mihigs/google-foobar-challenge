def solution(x):
    
    # edge case
    if type(x) != str:
        print("Invalid input: Expected a string")
        return
    
    # string to store the output in
    outputString = ""
    
    
    for letter in x:
        # convert the letter to ASCII
        letterASCII = ord(letter)
        # check if the letter is lowercase
        if letterASCII >= 97 and letterASCII <= 122:
            letterASCII = 122 + (97 - letterASCII)
        # fill the output string
        outputString += chr(letterASCII)
    return outputString