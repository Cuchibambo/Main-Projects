import random
import numpy as np

words = [('Lord Of The Rings','The Hobbit'),('London','Paris'),('Fire','Sun')]
currentWords = random.choice(words)

[2,0,1,0,0,0,1,0]

NUM_PLAYER = 0

def StartGame():
    try: 
        NUM_PLAYER = int(input('Number of players:'))
    except Exception as e:
        print(f'try again: {e}')
    except NUM_PLAYER < 4:
        print('try again')


    
PlayerRoles = np.zeros(NUM_PLAYER)
PlayerRoles[0] = 2
for i in range(1,NUM_PLAYER//2):
    PlayerRoles[2*i] = 1

PlayerWords = ['h','h','h','h','h','h','h','h']
for i in range(NUM_PLAYER):
    if PlayerRoles[i] == 0:
        PlayerWords[i] = currentWords[0]
    elif PlayerRoles[i] == 1:
        PlayerWords[i] = currentWords[1]
    elif PlayerRoles[i] == 2:
        PlayerWords[i] = 'Mister White'
    else:
        print('Something went terribly wrong')

for i in range(NUM_PLAYER):
    print(f'Player {i+1}: {PlayerWords[i]}')