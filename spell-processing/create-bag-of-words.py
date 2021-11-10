#Found instructions on https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/

import nltk  
#nltk.download('punkt')
import re  
import heapq

def words(text): return re.findall(r'\w+', text)
 
corpus_text = open('news.txt', encoding='utf8').read()
corpus_text += open('tweets.txt', encoding='utf8').read()
corpus_text += open('wiki.txt', encoding='utf8').read()
corpus_text += open('blogs.txt', encoding='utf8').read()

corpus = nltk.sent_tokenize(corpus_text)

for i in range(len(corpus )):
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


most_freq = heapq.nlargest(10000, wordfreq, key=wordfreq.get)

file=open('text.txt','w', encoding="utf-8")
arranged = {}
for word in most_freq:
    file.writelines(word+'\n')
file.close()