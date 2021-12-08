#athrú - correct
#athru 
from collections import Counter
from distances import addSingleCharacter, deleteSingleCharacter, edits1
from irishCorpus import corpus_text
from wordRead import words

WORDS = Counter(words(corpus_text))

#word = 'atmaiféar'

errorModel = open('IrishCorpus/irish_substitutions.txt',encoding="UTF-8").readlines()

#print('Count of ', word,":",WORDS[word])

def countTwoWords(word1, word2):
    return WORDS[word1] + WORDS[word2]

#results = []

word_results = set()

word_dict = {}

def findProbability(wordGroup, word):
    #main_results = []
    for wordOption in wordGroup:
        if wordOption in WORDS:
            # countOftargetWord = str(WORDS[wordOption])
            # countoftwoWords = str(countTwoWords(word, wordOption))
            probabilityOfWords =  WORDS[wordOption] / countTwoWords(word, wordOption)
            #main_results.append( wordOption + ": "+countOftargetWord + "/" + countoftwoWords + "=" + str(probabilityOfWords))
            if probabilityOfWords > 0.00011:
                word_dict[wordOption] = probabilityOfWords

    # if len(main_results) > 0:
    #     return main_results
    # else:
    #     return

def checkIrishWordUnsupervised(word):
    
    #print('word1',word)
    for character in word:
        for line in errorModel:
            fullError = line.split('|')
            removedCharacter = fullError[0]
            splittledSecondpart = fullError[1].split()
            addedCharacter = splittledSecondpart[0]

            if removedCharacter != "" and character != removedCharacter:
                continue
            elif removedCharacter == "":
                insertedCharacterWords = addSingleCharacter(word, character)
                checkProbability = findProbability(insertedCharacterWords, word)
                if len(insertedCharacterWords) > 0 and checkProbability is not None:
                    #results.append(checkProbability)
                    for item in checkProbability:
                        word_results.add(item)
        
            elif removedCharacter != "" and addedCharacter != "":
                letters = removedCharacter+addedCharacter
                alteredWords = edits1(word, True, letters)

                checkProbability = findProbability(alteredWords, word)

                if len(alteredWords) > 0  and checkProbability is not None:
                    #results.append(checkProbability)
                    for item in checkProbability:
                        word_results.add(item)

            elif addedCharacter == "":
                deletedCharacterWords = deleteSingleCharacter(word)
                checkProbability = findProbability(deletedCharacterWords, word)
                if len(alteredWords) > 0 and checkProbability is not None:
                    #results.append(checkProbability)
                    for item in checkProbability:
                        word_results.add(item)                


    # print(results)
    # print(results[5])

    #print(word_results)
    #print(word_dict)

    if len(word_dict) > 0:
        sortedWords = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)

        #print(dict(sortedWords))
        
        final_words = dict(sortedWords)
        suggestions = []

        for correction in final_words:
            #print(correction ,":", final_words[correction])
            suggestions.append(correction)

        return final_words
    else:
        return word_dict

checkIrishWordUnsupervised('bliain')


def oneUnsupervisedCorrection(checkingWord):
    #print(checkingWord)
    correctionSet = checkIrishWordUnsupervised(checkingWord)
    corrections = list(correctionSet)
    word_dict.clear()
    if len(corrections) > 0:
        if checkingWord != corrections[0]:
            #print(corrections[0])
            return corrections[0]
        else:
            return checkingWord
    else:
        return checkingWord

#print(oneUnsupervisedCorrection('hAmasóine'))