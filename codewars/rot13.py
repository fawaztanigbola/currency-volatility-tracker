def rot13(message):

    """
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

    Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should 
    be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
    
    Please note that using encode is considered cheating.
    """
    
    ans = ''
    
    for i, char in enumerate(message):
        # for small letters 
        if (ord(char) >= 97 and ord(char) <= 122): 
            i = ord(char) + 13
            if i > 122:
                rem = i - 123
                i = 97 + rem
            ans += chr(i)
        #  For capital letters
        elif (ord(char) >= 65 and ord(char) <= 90):
            i = ord(char) + 13
            if i > 90:
                rem = i - 91
                i = 65 + rem
            ans += chr(i)
        else:
            ans += char
    return ans

# check