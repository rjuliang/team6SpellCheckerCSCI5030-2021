
from collections import Counter
from distances import edits1, edits2
from wordRead import words

WORDS = Counter(words(open('IrishCorpus/bag_of_words.txt', encoding='utf8').read()))

pairs =  set()

for word in WORDS:
    editions1 = edits1(word)

    for wordEdited1 in editions1:
        if wordEdited1 in WORDS:
            if wordEdited1 != word:
                pairs.add(word +","+wordEdited1)

    if len(word) > 6: 
        editions2 = edits2(word)

        for wordEdited2 in editions2:
            if wordEdited2 in WORDS:
                if wordEdited2 != word:
                    pairs.add(word+","+wordEdited2)

file=open('IrishCorpus/irish_pairs.txt','w', encoding="utf-8")
for pair in pairs:
    file.writelines(pair+'\n')
file.close()