
"""
Special thanks to Peter Norvig for providing this amazing solution.

Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

import re
from collections import Counter

def words(text): return re.findall(r'\w+', text)

WORDS_ENGLISH = Counter(words(open('bigText.txt', encoding="UTF-8").read()))

#Corpus with Irish files are not added to repo due to copyright
WORDS_IRISH = Counter(words(open('legal.txt', encoding="UTF-8").read() + open('bible.txt', encoding="UTF-8").read() + open('news.txt', encoding="UTF-8").read() ))

def P(word, N=sum(WORDS_IRISH.values())): 
    "Probability of `word`."
    return WORDS_IRISH[word] / N

def correction(word, lng):
  "Most probable spelling correction for word."
  return max(candidates(word, lng), key=P)

def candidates(word, lng): 
    "Generate possible spelling corrections for word."    
    return (known([word], lng) or known(edits1(word, lng), lng) or known(edits2(word, lng), lng) or [word])

def known(wordsToCheck, lng): 
    "The subset of `words` that appear in the dictionary of WORDS."
    if lng == "ga":
        WORDS_LIST = WORDS_IRISH 
    else: 
        WORDS_LIST = WORDS_ENGLISH
    return set(w for w in wordsToCheck if w in WORDS_LIST)

def edits1(word, lng):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'

    if lng == "ga":
        #print('checking Irish characters...')
        letters += "ÁḂĊḊÉḞĠÍṀÓṖṠṪÚáḃċḋéḟġíṁóṗṡṫú"

    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word, lng): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word, lng) for e2 in edits1(e1, lng))


def checkPhrase(phrase, lng):
    #print(type(phrase))
    textList = phrase.split()
    errorList=[]
    
    #print(textList)
    for word in textList: 
        word = re.sub('^[^a-zA-ZáéíóúÀ-ÿ]','',word) 
        word = re.sub('[^a-zA-ZáéíóúÀ-ÿ]*$','',word)
        #print('word: '+word)
        suggestions=candidates(word, lng)
        if word not in suggestions:
            suggestionsArray = []
            for suggestion in suggestions:
                suggestionsArray.append(suggestion)
            #errorWord= (word+':'+str(suggestion))
            errorWord = {"word":word,"suggestions": suggestionsArray}
            errorList.append(errorWord)
    return errorList

