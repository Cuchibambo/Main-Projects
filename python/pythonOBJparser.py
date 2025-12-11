def GetVerteciesFromOBJ(FileName:str) -> list:
    file = open(FileName) # Open File
    Vertecies = []
    for line in file: # Check every line in file
        if line[0] == 'v' and line[1] == ' ': # only keeps vertex data
            line = line[2:] # removes the 'v '
            line = line.strip('\n')
            line = line.split(' ')
            pos = (float(line[0]),float(line[1]),float(line[2]))
            Vertecies.append(pos)
    return Vertecies

def GetFacesFromOBJ(FileName:str) -> list:
    file = open(FileName) # Open File
    Faces = []
    for line in file: # Check every line in file
        if line[0] == 'f' and line[1] == ' ': # only keeps face data
            line = line[2:] # removes the 'f '
            line = line.strip('\n')
            line = line.split(' ')
            Faces.append((int(line[0].split('/')[0]),int(line[1].split('/')[0]),int(line[2].split('/')[0])))
    return Faces