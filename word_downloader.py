import re
import wikipedia as wiki
import config
from unidecode import unidecode

wordLength = config.wordLength

'''
Returns a list of words present in all pages of the given language tag
'''
def generateDict(tag, maxLength):
    
    wiki.set_lang(tag)

    for article in config.articles[tag]:

        page = wiki.WikipediaPage(article)
        content = unidecode(page.content)
        wordList = generateWordList(content, maxLength)

    return wordList

'''
Generate a list of words from the given page content
'''
def generateWordList(pageContent, maxLength):

    words = re.sub(r'[^a-zA-Z ]', '', pageContent)
    words = words.lower()
    wordList = words.split()

    shortWords = []
    for word in wordList:
        if len(word) <= maxLength:
            shortWords.append(word)

    return shortWords

'''
Encode the words in their vector form.
abcdef.....xyz
000100.....000
Represents the character d
'''
def convertDictToVector(dic, wordLength):
    vecList = []

    for word in dic:
        vec = ''

        for i in word:

            currentLetter = i
            index = ord(currentLetter) - 97     #a = 0
            letter = ('0' * index) + '1' + ('0' * (25-index))
            vec += letter
        
        if len(word) < wordLength:

            for i in range(wordLength - len(word)):
                vec += '0' * 26

        vecList.append(vec)

    return vecList


'''
Creates the encoding for the output (languages)
'''
def createLanguageVector(tagIndex, numberOfLanguages):
    vec = ('0' * tagIndex) + '1' + ('0' * (numberOfLanguages - tagIndex - 1))
    return vec