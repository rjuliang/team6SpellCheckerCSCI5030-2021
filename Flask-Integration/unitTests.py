from collections import Counter
import csv
from spellCheck import *

def wordTestirish(word):  
    if  (word.isalnum() == False and len(word) == 1) or (any(chr.isdigit() for chr in word)) or (any(not c.isalnum() for c in word)) or word == "\n" or word == "USER":
        correct = word
    else:
        correct = correction(str(word), 'ga')

    return correct

def unitTests():
    INPUT_WORDS = []
    with open('input-test.txt','r', encoding="UTF-8") as file:
        for line in file:     
            for word in line.split():         
                INPUT_WORDS.append(word)
    
    with open('input_test_team6-1.tsv', 'w', encoding="UTF-8", newline='') as out_file:
        tsv_writer = csv.writer(out_file, delimiter="\t")

        for word in INPUT_WORDS:
            correct = wordTestirish(word)
            tsv_writer.writerow([word, correct])

unitTests()