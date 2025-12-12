import math
def ProduitVectoriel(vec1:tuple,vec2:tuple) -> tuple:
    x = (vec1[1]*vec2[2])-(vec1[2]*vec2[1])
    y = (vec1[2]*vec2[0])-(vec1[0]*vec2[2])
    z = (vec1[0]*vec2[1])-(vec1[1]*vec2[0])
    return (x,y,z)

def isColinaire(vec1:tuple, vec2:tuple) -> bool:
    try:
        k = vec1[0]/vec2[0]
    except:
        try:
            k = vec1[1]/vec2[1]
        except:
            try:
                k = vec1[0]/vec2[0]
            except:
                return None # pyright: ignore[reportReturnType]
    if (vec1[0] == k*vec2[0]
    and vec1[1] == k*vec2[1]
    and vec1[2] == k*vec2[2]):
        return True
    else:
        return False

def GetDivisor(a:int) -> list:
    Divisors = []
    for i in range(1,int(math.sqrt(a))+1):
        if a%i == 0:
            Divisors.append(i)
            if int(a/i) != i:
                Divisors.append(int(a/i))
    Divisors.sort()
    return Divisors

def PGCD(a:int,b:int) -> int:
    Divisora, Divisorb = GetDivisor(a), GetDivisor(b)
    PGCDcandidates = []
    for i in Divisora:
        if i in Divisorb:
            PGCDcandidates.append(i)
    return PGCDcandidates[-1]

def isPrime(a:int) -> bool:
    if len(GetDivisor(a)) == 2:
        return True
    else:
        return False

def isCarreparfait(a:int) -> bool:
    if len(GetDivisor(a))%2 == 1:
        return True
    else:
        return False
    
def GetMagnitude(vec:tuple) -> float:
    return math.sqrt(ProduitScalaire(vec,vec))

def NormalizeVector(vec:tuple) -> tuple:
    mag = GetMagnitude(vec)
    if mag != 0:
        return (vec[0]/mag, vec[1]/mag, vec[2]/mag)
    else:
        return (0,0,0)

def GetNormalVector(vec1:tuple, vec2:tuple) -> tuple:
    return NormalizeVector(ProduitVectoriel(vec1,vec2))

def ProduitScalaire(vec1:tuple,vec2:tuple) -> float:
    return vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]

def isVecOnPlane(vec:tuple,normal:tuple) -> bool:
    a = normal[0]
    b = normal[1]
    c = normal[2]
    return round(a*vec[0]+b*vec[1]+c*vec[2]) == 0

def FindIntersectionBetweeenLineAndPlane(normal:tuple,Point1:tuple,Point2:tuple) -> tuple:

    div1 = -(normal[0]*Point1[0]+normal[1]*Point1[1]+normal[2]*Point1[2])
    div2 = (normal[0]*(Point2[0]-Point1[0])+normal[1]*(Point2[1]-Point1[1])+normal[2]*(Point2[2]-Point1[2]))
    t = div1/div2

    IntersectionPoint = (Point1[0]+t*(Point2[0]-Point1[0]),
                 Point1[1]+t*(Point2[1]-Point1[1]),
                 Point1[2]+t*(Point2[2]-Point1[2]))

    return IntersectionPoint

def GetLinearCoeficientsRepresentationOfPointOnPlane(vec1:tuple,vec2:tuple,point:tuple) -> tuple:

    x = 'None'
    y = 'None'

    for i in range(len(vec1)): # len(vec1) should always be 3
        if vec1[i] != 0 and vec2[i] == 0:
            x = point[i]/vec1[i]

    for i in range(len(vec1)): # len(vec1) should always be 3
        if vec2[i] != 0 and vec1[i] == 0:
            y = point[i]/vec2[i]

    if x != 'None' and y != 'None':
        return (x,y)
    
    if x != 'None':
        for i in range(len(vec1)): # len(vec1) should always be 3
            if vec2[i] != 0 and vec1[i] != 0:
                y = (point[i]-(x*vec1[i]))/vec2[i]

    if y != 'None':
        for i in range(len(vec1)): # len(vec1) should always be 3
            if vec1[i] != 0 and vec2[i] != 0:
                x = (point[i]-(y*vec2[i]))/vec1[i]
    
    if x != 'None' and y != 'None':
        return (x,y)

    y = ((point[0]*vec1[1])-(point[1]*vec1[0]))/((vec2[0]*vec1[1])-(vec2[2]*vec1[0]))
    x = (point[0]-(y*vec2[0]))/vec1[0]
    return (x,y)
    
                
def ChangeRange(x:float,min1:float,max1:float,min2:float,max2:float) -> float:
    return (((x-min1)/(max1-min1))*(max2-min2))+min1

def X_RotationMatrix(vec:tuple,angle:float) -> tuple:
    rotatedVec = (
        vec[0],
        (vec[1]*math.cos(angle))+(vec[2]*math.sin(angle)),
        -(vec[1]*math.sin(angle))+(vec[2]*math.cos(angle))
    )
    return rotatedVec

def Y_RotationMatrix(vec:tuple,angle:float) -> tuple:
    rotatedVec = (
        (vec[0]*math.cos(angle))-(vec[2]*math.sin(angle)),
        vec[1],
        (vec[0]*math.sin(angle))+(vec[2]*math.cos(angle))
    )
    return rotatedVec

def Z_RotationMatrix(vec:tuple,angle:float) -> tuple:
    rotatedVec = (
        (vec[0]*math.cos(angle))+(vec[1]*math.sin(angle)),
        -(vec[0]*math.sin(angle))+(vec[1]*math.cos(angle)),
        vec[2]
    )
    return rotatedVec

def Average(data:list) -> float:
    sum = 0
    for num in data:
        sum += num
    return sum/len(data)

def Convert_HSV_to_RGB(color:tuple) -> tuple:
    H = color[0]
    S = color[1]
    V = color[2]
    # H in degrees
    # S in 0-1
    # V in 0-1
    hR, hG, hB = 0, 0, 0
    H = H%360
    if H >= 0 and H < 60:
        hR = 1
        hG = H/60
        hB = 0
    elif H >= 60 and H < 120:
        hR = (-H/60)+2
        hG = 1
        hB = 0
    elif H >= 120 and H < 180:
        hR = 0
        hG = 1
        hB = (H/60)-2
    elif H >= 180 and H < 240:
        hR = 0
        hG = (-H/60)+4
        hB = 1
    elif H >= 240 and H < 300:
        hR = (H/60)-4
        hG = 0
        hB = 1
    elif H >= 300 and H < 360:
        hR = 1
        hG = 0
        hB = (-H/60)+6
        
    R = hR+1-S
    G = hG+1-S
    B = hB+1-S
    if R>1: R=1
    if G>1: G=1
    if B>1: B=1
    R = R*V
    G = G*V
    B = B*V
    return (int(R*255),int(G*255),int(B*255))

def Clamp(x:float,rangeUp:float,rangeDown:float) -> float:
    if x > rangeUp:
        x = rangeUp
    elif x < rangeDown:
        x = rangeDown
    return x