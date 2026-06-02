def spin_words(sentence ):
    """
        This func takes in a sentence and spins any word with 5 or more letters 
        >>> spin_words('Stop Spinning My Words')
        >>> Stop gninnnipS My sdroW 
    """
    if sentence == '':
        return ''
    words = sentence.split()
    fin_sent = ''
    for i, word in enumerate(words):
        if len(word) >= 5 :
            word = word[::-1]
            fin_sent += word
        else:
            fin_sent += word
        if i != 0 or i != len(words)-1:
            fin_sent += ' '
    fin_sent = fin_sent.strip()
    return fin_sent