from string import *

def decoder():
    
    # Make var
    stop = 0
    text = input("input text: ")
    replacementDict = {}
    
    # Main loop
    while stop == 0:
        
        # Variables for letters input
        letvarsetup = 0
        
        while letvarsetup == 0:
            
            letterToReplace = input("Letter to replace: ")
            letterReplace = input("Letter to replace it with: ")
            
            # Stop teh program if user says stop
            if letterReplace == "stop" or letterToReplace == "stop":
                stop = 1
                break
            
            # Check if letters are valid
            if str.isalpha(letterToReplace) and len(letterToReplace) == 1 and str.isalpha(letterReplace) and len(letterReplace) == 1:
                letvarsetup = 1
            else:
                print("try agin")
            
        # replace letter in text
        replacementDict[letterToReplace] = letterReplace
        
        new_text = []
        
        for char in text:
            new_text.append(replacementDict.get(char, char))

        newtext = ''.join(new_text)
        
        # Make newtext but with only letters
        cleanednewtext = "".join(char for char in newtext if str.isalpha(char))
        
        # Make new_text but with only letters
        cleanednew_text = []
        
        for i in cleanednewtext:
            cleanednew_text.append(i)
        
        # Get Frequency of every character appearing
        letfreqdict = {}
        for totalchar in range(len(cleanednew_text)):
            letfreqdict[cleanednew_text[totalchar]] = letfreqdict.get(cleanednew_text[totalchar], 0) + 1
        
        # Make it a fraction
        for i in (letfreqdict):
            letfreqdict[i] = letfreqdict[i]/(totalchar + 1)
        
        # Make it a %
        for i in (letfreqdict):
            letfreqdict[i] = letfreqdict[i]*100
        
        # Sort largest > smallest
        sortedDict = dict(sorted(letfreqdict.items(), key = lambda item : item[1], reverse = True))
        
        # Print frequencies
        for i in sortedDict:
            print(i, "=", sortedDict[i],"%")
        
        # Print newtext and oldtext
        
        print("Old text:",text)
        print("")
        print("New text:",newtext)
        
decoder()
