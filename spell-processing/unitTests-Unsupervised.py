from collections import Counter
import csv
from unsupSpellCheck import *
#from spellCheck import *


def evaluateWord (token):
    return (token.isalnum() == False and len(token) == 1) or (any(chr.isdigit() for chr in token)) or (any(not c.isalnum() for c in token)) or token == "\n" or token == "USER"

def wordTestirish(word, beforeWord, afterWord):  
    #evaluateCharacter = (word.isalnum() == False and len(word) == 1) or (any(chr.isdigit() for chr in word)) or (any(not c.isalnum() for c in word)) or word == "\n" or word == "USER"

    if  evaluateWord(word):
        correct = word
    else:
        #print(word)
        if evaluateWord(beforeWord) is False and evaluateWord(afterWord) is False: 
            beforeWord = beforeWord
            afterWord = afterWord
        elif evaluateWord(beforeWord) is True and evaluateWord(afterWord) is True:
            beforeWord = ""
            afterWord = ""
        elif  evaluateWord(beforeWord) is True and evaluateWord(afterWord) is False:
            beforeWord = ""
            afterWord = afterWord
        elif evaluateWord(beforeWord) is False and evaluateWord(afterWord) is True:
            beforeWord = beforeWord
            afterWord = ""

        correct = oneUnsupervisedCorrection(str(word), str(beforeWord), str(afterWord))

    return correct

def unitTests():
    INPUT_WORDS = []
    with open('input-test.txt','r', encoding="UTF-8") as file:
        for line in file:     
            for word in line.split():         
                INPUT_WORDS.append(word)
    
    with open('FULL-UnSup-File-team6.tsv', 'w', encoding="UTF-8", newline='') as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")
        index = 0
        for word in INPUT_WORDS:
            #print(word)
            if index > 0:
                beforeWord = INPUT_WORDS[index - 1]
            else:
                beforeWord = ""

            if index + 1 == len(INPUT_WORDS):
                afterWord = ""
            else:
                afterWord = INPUT_WORDS[index + 1]

            correct = wordTestirish(word, beforeWord, afterWord)
            tsv_writer.writerow([word, correct])
            index = index+1

unitTests()