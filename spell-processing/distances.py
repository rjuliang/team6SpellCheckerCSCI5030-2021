
"""
Special thanks to Peter Norvig for providing this amazing solution.

Spelling Corrector in Python 3; see http://norvig.com/spell-correct.html

Copyright (c) 2007-2016 Peter Norvig
MIT license: www.opensource.org/licenses/mit-license.php
"""

#Only for Unsupervised Irish model
def edits1(word, usingOtherletters = False, newLetters = "a"):
    "All edits that are one edit away from `word`."
    if usingOtherletters is False:
        letters    = 'ÁḂĊḊÉḞĠÍṀÓṖṠṪÚáḃċḋéḟġíṁóṗṡṫáéíóúabcdefghijklmnopqrstuvwxyz'
    else:
        letters = newLetters

    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

def addSingleCharacter(word, character):
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    inserts    = [L + c + R               for L, R in splits for c in character]
    return set(inserts)

def deleteSingleCharacter(word):
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    return set(deletes)
