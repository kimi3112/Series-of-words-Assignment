# -*- coding: utf-8 -*-
"""
Created on Thu May 27 09:54:57 2021

@author: IT LAB
"""
import re
from simple_colors import * #for highlighting the text
import pyperclip as pc
text=pc.paste()
print(text)
while True:
    print('Enter the word you would like to find')   
    keyWord = input()     #word you have to find in the given text
    if keyWord == '':
        print('Thank you for using basic search!')
    elif not keyWord.isalnum():  # to check the text with alpha and numeric propertiees
        print('Please enter a word or an alphanumeric string without spaces')
    else:
        wordList = text.split()     # splitting of text into series of words 
        matchCount = 0
        for i in range(len(wordList)):
            if wordList[i] == keyWord:
                wordList[i] = wordList[i].center((len(wordList[i])+4),'_')
                matchCount += 1
        print('There are %d matches to your key word, %s' % (matchCount,keyWord))
        print(green(keyWord,'bold'))   # to highlight the text
        newText = ' '.join(wordList)
        pc.copy(newText)
        result = re.findall(keyWord, text)   # to find the series of the same word in the given text
        print (red(result,'bold'))
        break
