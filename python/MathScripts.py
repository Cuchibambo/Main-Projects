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

def FindIntersectionBetweeenPointAndPlane(normal:tuple,Point1:tuple,Point2:tuple) -> tuple:

    div1 = -(normal[0]*Point1[0]+normal[1]*Point1[1]+normal[2]*Point1[2])
    Div2 = (normal[0]*(Point2[0]-Point1[0])+normal[1]*(Point2[1]-Point1[1])+normal[2]*(Point2[2]-Point1[2]))
    t = div1/Div2

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
    return (((x-min1)*(max2-min2))/(max1-min1))+min1

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