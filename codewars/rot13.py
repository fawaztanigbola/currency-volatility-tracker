def rot13(message):
    ans = ''
    for i, char in enumerate(message):
        if (ord(char) >= 97 and ord(char) <= 122): 
            i = ord(char) + 13
            if i > 122:
                rem = i - 123
                i = 97 + rem
            ans += chr(i)
        elif (ord(char) >= 65 and ord(char) <= 90):
            i = ord(char) + 13
            if i > 90:
                rem = i - 91
                i = 65 + rem
            ans += chr(i)
        else:
            ans += char
    return ans
