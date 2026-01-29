Word = "forts"
WordArray = list(Word.lower())
Guess = ""
GuessArray = []
ArrayOfRight = []
ArrayOfOranges = []
def CheckDiff():
    global Guess, GuessArray, WordArray, ArrayOfRight, ArrayOfOranges
    ArrayOfRight = []
    ArrayOfOranges = []
    for i in range(5):
        if GuessArray[i] == WordArray[i]:
            ArrayOfRight.append(1)
        else:
            ArrayOfRight.append(0)
    for i in range(5):
        if GuessArray[i] in WordArray:
            ArrayOfOranges.append(-1)
        else:
            ArrayOfOranges.append(0)
    print(ArrayOfRight)
    print(ArrayOfOranges)
    Guessing()
def Output():
    global Guess, GuessArray, WordArray
    if GuessArray == WordArray:
        print('You Win!')
    else:
        CheckDiff()
def Guessing():
    global Guess, GuessArray
    Guess = str(input('Guess a word: '))
    if any(char.isdigit() for char in Guess) or any(not char.isalnum() for char in Guess) or ' ' in Guess: 
        print('Only letters allowed')
        Guessing()
    elif len(Guess) >= 6 or len(Guess) <= 4:
        print('That is not a valid lengh')
        Guessing()
    elif len(Guess) == 5:
        GuessArray = list(Guess.lower())
        Output()
Guessing()