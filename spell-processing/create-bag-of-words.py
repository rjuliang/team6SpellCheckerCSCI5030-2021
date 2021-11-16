#Found instructions on https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/

import nltk  
#nltk.download('punkt')
import re  
import heapq
from irishCorpus import corpus_text
 

corpus = nltk.sent_tokenize(corpus_text)

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

def wordContainsNumber(word):
    if containsNumber(word) == True:
        return True
    return False

for i in range(len(corpus)):
    #if wordContainsNumber(corpus [i]) == False:
    corpus [i] = corpus [i]
    corpus [i] = re.sub(r'\W',' ',corpus [i])
    corpus [i] = re.sub(r'\s+',' ',corpus [i])


wordfreq = {}
for sentence in corpus:
    tokens = nltk.word_tokenize(sentence)
    for token in tokens:
        if token not in wordfreq.keys():
            wordfreq[token] = 1
        else:
            wordfreq[token] += 1


most_freq = heapq.nlargest(10200, wordfreq, key=wordfreq.get)

arranged = set()

for word in most_freq:
    if wordContainsNumber(word) == False:
        arranged.add(word)


file=open('text.txt','w', encoding="utf-8")


for word in arranged:
    file.writelines(word+'\n')
file.close()