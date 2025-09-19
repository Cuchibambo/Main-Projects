from string import *
import random

def encoder(text):
    
    # Make var
    alphabet = []
    unshuffledAlpha = []
    arrayTxt = []
    encoderDict = {" " : " ",
                   "!" : "!",
                   "?" : "?",
                   "." : ".",
                   "," : ",",
                   ":" : ":",
                   "/" : "/",
                   "'" : "'",
                   "0" : "0",
                   "1" : "1",
                   "2" : "2",
                   "3" : "3",
                   "4" : "4",
                   "5" : "5",
                   "6" : "6",
                   "7" : "7",
                   "8" : "8",
                   "9" : "9",
                   "-" : "-",
                   "[" : "[",
                   "]" : "]",
                   "(" : "(",
                   ")" : ")",
                   '"' : '"'}
    
    # Make lower into an array
    for i in ascii_lowercase:
        alphabet.append(i)
        unshuffledAlpha.append(i)
      
    # Randomize the alphabet
    random.shuffle(alphabet)
    
    # Make a dictionary for the encoder
    for i in range(len(unshuffledAlpha)):
        encoderDict[unshuffledAlpha[i]] = alphabet[i]

    # Make everything lower case
    LowerText = str.lower(text)
    
    # Make input a array
    for i in LowerText:
        arrayTxt.append(i)
    
    #Encode the text
    for i in range(len(arrayTxt)):
        arrayTxt[i] = encoderDict.get(arrayTxt[i])
    
    # Make array into string
    EncodedText = "".join(e for e in arrayTxt)
    print(EncodedText)
    
encoder(input("Text to encode: "))