#Approach: Wrote a nice little personalized parser that implements a generator to be able
# to iterate over the tokens in the body of text.  Use of a default dictionary (factory int)
# to eaisly count frequencies (key is word, value is frequency).  Use of operator.itemgetter
# to eaisly obtain a key with the largest value

from collections import defaultdict
import operator


class Parser(object):
    #Add a trailing whitespace to string for parser generator (see note at end of class)
    def __init__(self, textToParse:str) -> None:  self.body = textToParse + " "
        
    #Blackspace: A character to keep; any letter [a-zA-Z] or apostrophy
    def _isBlackspace(self,char:str)->bool:  return (char.isalpha() or char=="'")

    #Whitespace: A character to toss out; anything that is not blackspace
    def _isWhitespace(self,char:str)->bool:  return (not self._isBlackspace(char))

    #Generator that produces tokens of blackspace that are not all apostrophes
    def tokenizer(self) ->str:
        token, consumingToken  = [], False
        for char in self.body:
            if self._isBlackspace(char):
                token.append(char)
                consumingToken = True
            if self._isWhitespace(char) and consumingToken:
                #To be a valid token, the token must contain atleast one letter [a-zA-Z]
                if any(c.isalpha() for c in token): 
                    yield ''.join(token)
                token = []
                consumingToken=False
    #end function

    #Note on the parser's addition of the trailing whitespace (in constructor): Manages an
    # edge case when the last character in the body of text to parse is a token.
    #      e.g: 'a b c c c' here 'c' is a valid token, and is the last character in the file
    # Since the trailing whitespace character is concatenated to the body of the text,
    # garantees that 'if self._isWhitespace(char) and consumingToken' is true for this edge
    # case scenario.
#end class


#Given a body of text, get at most the three words with the largest frequency
def top_3_words(text:str)->list:
    p = Parser(text)
    counter =  defaultdict(int)
    topWords = []

    for token in p.tokenizer():     #get word frequency
        counter[token.lower()]+=1
    
    for _ in range(3):              #get at most three words with higest freq
        if counter:
            maxKey = max(counter.items(), key=operator.itemgetter(1))[0]
            topWords.append(maxKey)
            counter.pop(maxKey)
        else:
            break

    return topWords
#end function