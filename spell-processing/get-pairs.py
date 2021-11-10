import re
from collections import Counter

def words(text): return re.findall(r'\w+', text)

WORDS = Counter(words(open('text.txt', encoding='utf8').read()))

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

#print(edits2('mispelled'))

pairs = set()

for word in WORDS:
    editions1 = edits1(word)

    for wordEdited1 in editions1:
        if wordEdited1 in WORDS:
            pairs.add(word +","+wordEdited1)

    editions2 = edits2(word)

    for wordEdited2 in editions2:
        if wordEdited2 in WORDS:
            pairs.add(word+","+wordEdited2)

file=open('resultPairs1.txt','w', encoding="utf-8")
for pair in pairs:
    file.writelines(pair+'\n')
file.close()