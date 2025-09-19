
GRIDSIZE = 3
numberOfCards = (GRIDSIZE**2)+GRIDSIZE+1
numberOfSimboles = GRIDSIZE+1

class card():
    def __init__(self,Simbole):
        self.simbole = Simbole
        self.simboles = []
    def __str__(self):
        return ' '.join([str(self.simbole),str(self.simboles)])

cards = []

for i in range(numberOfCards):
    cards.append(card(i))
    # if i % GRIDSIZE == 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Blue 1")
    # if (i-1) % GRIDSIZE == 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Blue 2")
    # if (i-2) % GRIDSIZE == 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Blue 3")
        
    # if i < GRIDSIZE and i >= 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Red 1")
    # if (i-GRIDSIZE) < GRIDSIZE and (i-GRIDSIZE) >= 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Red 2")
    # if (i-(2*GRIDSIZE)) < GRIDSIZE and (i-(2*GRIDSIZE)) >= 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Red 3")
        
    # if i % (GRIDSIZE+1) == 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Green 1")
    # if (i-1) % (GRIDSIZE+1) == 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Green 2")
    # if (i-2) % (GRIDSIZE+1) == 0 and i < GRIDSIZE**2:
    #     cards[i].simboles.append("Green 3")
    
    for j in range(GRIDSIZE**2):
        for k in range():
            if i < GRIDSIZE and i >= 0:
                cards[i].simboles.append(j)
            
        
for Card in cards:
    print(Card)