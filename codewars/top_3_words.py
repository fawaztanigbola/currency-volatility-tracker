def top_3_words(text):
    text = text.split()
    
    for word in text:
        pass
    return

def iswrd(word):
    for chr in word:
        if not (chr.isalpha() or chr == "'"):
            return False
        return True