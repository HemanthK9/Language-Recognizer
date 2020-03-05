from keras.models import Sequential
from keras.layers import Dense
from config import *
from word_downloader import convertDictToVector as convert_dic_to_vector
import numpy as np

#Rediefine the network
network = Sequential()
network.add(Dense(200, input_dim=26*wordLength, activation='sigmoid'))
network.add(Dense(150, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(len(articles), activation='softmax'))

#Load the weights stored previously in the weights.hdf5 file
network.load_weights('weights.hdf5')
network.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])


#Run an infinite loop to read words until the user terminates with a stop runtime or keyboard interrupt
while True:
    dic = []
    valid = False
    while not valid:
        word = input('Enter word to predict:\n')
        if len(word) <= wordLength:
            word = word.lower()
            valid = True
        else:
            print('Word must be less than ' + str(wordLength + 1) + ' letters long')
    dic.append(word)

    #THe input word is converted into the one-hot vector form
    vct_str = convert_dic_to_vector(dic, wordLength)
    vct = np.zeros((1, 26 * wordLength))
    count = 0
    for digit in vct_str[0]:
        vct[0,count] = int(digit)
        count += 1
    
    #The encoded word is sent to model for prediction and the output vector is returned
    prediction_vct = network.predict(vct)

    #The predicted probabilites are displayed
    langs = list(articles.keys())
    for i in range(len(articles)):
        lang = langs[i]
        score = prediction_vct[0][i]
        print(lang + ': ' + str(round(100*score, 2)) + '%')
    print('\n')



