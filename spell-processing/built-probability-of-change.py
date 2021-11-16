
import difflib
import re
from collections import Counter
from irishCorpus import corpus_text
from wordRead import words

pairsFile = open('resultPairs1.txt',encoding='UTF-8').read()
singlePairs = []
singlePairs = pairsFile.split('\n')

WORDS = Counter(words(corpus_text))

print(singlePairs[0])

print(WORDS['lathair'])

changes = []

for pair in singlePairs:
    separatedPair = pair.split(',')

    if len(separatedPair) > 1:
        left_word = separatedPair[0]
        right_word = separatedPair[1]
        if WORDS[left_word] >= (WORDS[right_word]*10):
            differences = difflib.ndiff(left_word, right_word)
            
            changesInWords = ""
            removed  = ""
            added = ""
            for difference in differences:
                if difference[0] == ' ':
                    continue
                elif difference[0] == '-':
                    removed += difference[-1]
                elif difference[0] == '+':
                    added += difference[-1]
            
            changesInWords += removed + "|" + added
            
            changes.append(changesInWords)
    
substitutions = []

for change in [ele for ind, ele in enumerate(changes,1) if ele not in changes[ind:]]:
    repetitions = changes.count(change)

    if change not in substitutions:
        substitutions.append({'change': change, 'repetitions':repetitions})

def myFunc(e):
  return e['repetitions']

substitutions.sort(reverse=True, key=myFunc)

file=open('subs2.txt','w', encoding="utf-8")
for subs in substitutions:
    file.writelines(subs['change'] +" "+ str(subs['repetitions']) +'\n')
file.close()