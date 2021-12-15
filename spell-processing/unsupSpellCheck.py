import re
from collections import Counter
from distances import addSingleCharacter, deleteSingleCharacter, edits1
from irishCorpus import corpus_text
from wordRead import words

#file not added to repo due to copyright
corpus_text_lngMdl = open('irish_corpus_file.txt', encoding='UTF-8').readlines()

WORDS = Counter(words(corpus_text))

errorModel = open('IrishCorpus/irish_substitutions.txt',encoding="UTF-8").readlines()


def countTwoWords(word1, word2):
    return WORDS[word1] + WORDS[word2]


word_results = set()

word_dict = {}

def findProbability(wordGroup, word):

    for wordOption in wordGroup:
        if wordOption in WORDS:
            probabilityOfWords =  WORDS[wordOption] / countTwoWords(word, wordOption)
            
            if probabilityOfWords > 0.2:
                word_dict[wordOption] = probabilityOfWords


def checkIrishWordUnsupervised(word):
    
    
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
                    
                    for item in checkProbability:
                        word_results.add(item)
        
            elif removedCharacter != "" and addedCharacter != "":
                letters = removedCharacter+addedCharacter
                alteredWords = edits1(word, True, letters)

                checkProbability = findProbability(alteredWords, word)

                if len(alteredWords) > 0  and checkProbability is not None:
                    
                    for item in checkProbability:
                        word_results.add(item)

            elif addedCharacter == "":
                deletedCharacterWords = deleteSingleCharacter(word)
                checkProbability = findProbability(deletedCharacterWords, word)
                if len(alteredWords) > 0 and checkProbability is not None:
                    
                    for item in checkProbability:
                        word_results.add(item)                



    if len(word_dict) > 0:
        sortedWords = sorted(word_dict.items(), key=lambda kv: kv[1], reverse=True)

        
        
        final_words = dict(sortedWords)
        suggestions = []

        for correction in final_words:
            suggestions.append(correction)

        return final_words
    else:
        return word_dict




def oneUnsupervisedCorrection(checkingWord, beforeWord, afterWord):
    correctionSet = checkIrishWordUnsupervised(checkingWord)
    corrections = list(correctionSet)
    word_dict.clear()
    phraseStatistics = {}

    if beforeWord == "" and afterWord == "":
            if len(corrections) > 0:
                if checkingWord != corrections[0]:
                    
                    return corrections[0]
                else:
                    return checkingWord
            else:
                return checkingWord
    else:
        correctionIndex = 0 
        for option in corrections:            

            if beforeWord == "":
                phrase = option + " " + afterWord
            elif afterWord == "":
                phrase = beforeWord + " "+ option
            else:
                phrase = beforeWord + " "+ option + " " + afterWord

            phraseStatistics[option] = timesStringPresent(phrase)

            if correctionIndex == 1:                
                break

            correctionIndex = correctionIndex + 1
        
        if checkingWord not in phraseStatistics:
            if beforeWord == "":
                original_phrase = checkingWord + " " + afterWord
            elif afterWord == "":
                original_phrase = beforeWord + " "+ checkingWord
            else:
                original_phrase = beforeWord + " "+ checkingWord + " " + afterWord

            phraseStatistics[checkingWord] = timesStringPresent(original_phrase)

        if len(phraseStatistics) > 0:
            sortedPhraseCorrections = sorted(phraseStatistics.items(), key=lambda kv: kv[1], reverse=True)
        
            dictOfCorrections = dict(sortedPhraseCorrections)
            final_phrases_options = list(dictOfCorrections)
            phraseStatistics.clear()
            if dictOfCorrections[final_phrases_options[0]] > 0:
                return final_phrases_options[0]
            else:
                return checkingWord
    


def searchPhrase(phrase, line):
    return re.search(r'\b' + phrase + r'\b', line)

def timesStringPresent(trio):
    times = 0
    index = 0
    for line in corpus_text_lngMdl:  

        index += 1 

        if trio in line:
            times += 1
    
    return times