from word_downloader import *
import numpy as np
import pandas as pd
from config import wordLength, articles, tags

actualWords = []
wordVectors = []
languageVectors = []
currentLanguage = 0

for tag in articles.keys():
    print('Generating dataset for ' + tags[tag])

    #Obtain a list of all words of all languages across all the wikipedia pages
    dic = generateDict(tag, wordLength)
    print(len(dic), 'words in', tags[tag])
    
    #Store all the actual words in the list
    for word in dic:
        actualWords.append(word)
    
    #Encode the words into the one-hot vector form, and store them in a list
    vectors = convertDictToVector(dic, wordLength)
    for vector in vectors:
        wordVectors.append(vector)

    #Encode the output vectors to serve as labels for the corresponding words
    outputVector = createLanguageVector(currentLanguage, len(articles))
    for i in range(len(vectors)):
        languageVectors.append(outputVector)
        
    currentLanguage += 1

'''
Create a dataframe to save as csv for visualization
col1    col2-6  col7-32
Word    Output  Vectorized word
'''
print('Creating a dataframe for dataset')
arr = []
for i in range(len(actualWords)):
    entry = []
    entry.append(actualWords[i])

    for digit in languageVectors[i]:
        entry.append(float(digit))

    for digit in wordVectors[i]:
        entry.append(float(digit))

    arr.append(entry)

#Save the array of encoded data into memory as a numpy array
arr = np.array(arr)
np.save('arr.npy', arr)

#Store the numpy array as a .csv file which can be opened in MS Excel
print('Storing dataframe as a .csv file')
df = pd.DataFrame(arr)
df.to_csv('data.csv')