def pig_it(text):
    ans = ""
    for word in text.split():
        if len(word) == 1 and not word.isalpha() :
            ans += word + ' '
        else:
            ans += word[1::] + word[0] +'ay' + ' '
    return ans.strip()
    #your code here