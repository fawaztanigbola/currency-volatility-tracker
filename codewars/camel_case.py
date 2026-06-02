def camel_case(text):
    if text == '':
        return ''
    final_word = ''
    text = text.replace('_', '-')
    for i, word in enumerate(text.split('-')):
        if i != 0 :
            final_word += word.capitalize()
        else:
            final_word += word
    return final_word

print(camel_case('the_stealth_warrior'),
      camel_case('the-stealth-warrior')
      )
