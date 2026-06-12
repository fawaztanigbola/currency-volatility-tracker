def pig_it(text):
    """
    Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

    Examples
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
    """
    ans = ""
    for word in text.split():
        if len(word) == 1 and not word.isalpha() :
            ans += word + ' '
        else:
            ans += word[1::] + word[0] +'ay' + ' '
    return ans.strip()
    #your code here