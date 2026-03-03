import math
import random


# def AskForInput():
#     while True:
#         try:
#             number = int(input("Random Number between 0-99: "))
#             if 0 > number or number > 99:
#                 print("Invalid input")
#             else:
#                 return number
#         except:
#             print("Invalid input")
        
# # Inputs = [ AskForInput() for _ in range(10)]
# # print(Inputs)

# ProbVec = [1/math.sqrt(100) for _ in range(100)]
# print(ProbVec)


def AskForInput(numberRange):
    while True:
        try:
            number = int(input(f"Random Number between 0-{numberRange-1}: "))
            if 0 > number or number > numberRange-1:
                print("Invalid input")
            else:
                return number
        except:
            print("Invalid input")
        
# Inputs = [ AskForInput() for _ in range(10)]
# print(Inputs)

def nComponentVec_to_2Componet(vec:list,target):
    sum = 0
    for i in range(len(vec)):
        if i != target:
            sum += (vec[i]**2)
    small_vec = [math.sqrt(sum),vec[target]]
    return small_vec

def MatrixRotation2D(vec,angle):
    x, y = vec[0], vec[1]
    cos, sin = math.cos(angle), math.sin(angle)
    return [x*cos-y*sin,x*sin+y*cos]
    
def GenerateEqualVector(nbComponents):
    ProbVec = [1/math.sqrt(nbComponents) for _ in range(nbComponents)]
    return ProbVec

def GetProportions(sum,originalValues,indexToNotuse):
    proportions = []
    for i in range(len(originalValues)):
        if i != indexToNotuse:
            proportions.append(originalValues[i]/sum)
        else:
            proportions.append(None)
    return proportions
    
def GetMagnitude(vec):
    sum = 0
    for i in vec:
        sum += (i**2)
    return math.sqrt(sum)

def ReconstructVec(proportions,bigsum):
    vec = []
    for i in range(len(proportions)):
        if proportions[i] != None:
            vec.append(bigsum*proportions[i])
    return vec

# print(MatrixRotation2D((0,1),math.pi/2))

def MoveVectorTowardsIndex(vec,index,angle):
    # print(ProbVec,GetMagnitude(ProbVec))
    vec_2D = nComponentVec_to_2Componet(vec,index)
    # print(vec_2D,GetMagnitude(vec_2D))
    proportionalMults = GetProportions(vec_2D[0],vec,index)
    # print(proportionalMults)
    rotatedVec = MatrixRotation2D(vec_2D,angle)
    # print(rotatedVec,GetMagnitude(rotatedVec))
    reconstructedVec = ReconstructVec(proportionalMults,rotatedVec[0])
    reconstructedVec.insert(index,rotatedVec[1])
    # print(reconstructedVec,GetMagnitude(reconstructedVec))
    return reconstructedVec

def GuessFromVec(vec):
    odds = []
    for i in vec:
        try:
            odds.append((i**2)+odds[-1])
        except:
            odds.append(i**2)
    randomValue = random.random()
    for i in range(len(vec)):
        if i == 0:
            if 0 < randomValue <= odds[i]:
                return i
        else:
            if odds[i-1] < randomValue <= odds[i]:
                return i
    

def mainLoop(numberRange,influence,repeatAmount):
    ProbVec = GenerateEqualVector(numberRange)
    for _ in range(repeatAmount):
        Guess = GuessFromVec(ProbVec)
        ProbVec = MoveVectorTowardsIndex(ProbVec,AskForInput(numberRange),influence)


mainLoop(4,math.pi/24,10)

def Experience(repeatAmount)