def TEST1():
    class Livre():
        def __init__(self, index:int, isTaken, dure) -> None:
            self.index = index
            self.isTaken = isTaken
            self.dure = dure

    entree = input()
    entree = entree.split(' ')
    nbLivres = int(entree[0])
    nbJours = int(entree[1])
    Livres = [Livre(i,False,0) for i in range(nbLivres)]
    for jour in range(nbJours):
        nbClients = int(input())
        for client in range(nbClients):
            entre2 = input().split(' ')
            index = int(entre2[0])
            if Livres[index].isTaken:
                print(0)
            else:
                duree = int(entre2[1])
                Livres[index].isTaken = True
                Livres[index].dure = duree
                print(1)
        for livre in Livres:
            if livre.dure > 0:
                livre.dure -= 1
            if livre.dure == 0:
                livre.isTaken = False
                
nbLettres = int(input())
Lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lignes = []
for line in range(nbLettres):
    for lettre in range((nbLettres*2)-1):
        lignes.append(Lettres[line])
    lignes.append('\n')

for line in range(nbLettres-1):
    lignes.append(lignes[-1])

print(lignes)

Texttoprint = ''
Texttoprint = Texttoprint.join(lignes)
print(Texttoprint.strip())