def GetVerteciesFromOBJ(FileName:str,spacesAfterv:int) -> list:
    file = open(FileName) # Open File
    Vertecies = []
    for line in file: # Check every line in file
        if line[0] == 'v' and line[1] == ' ': # only keeps vertex data
            line = line[spacesAfterv+1:] # removes the 'v '
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
            LineStriped = []
            for vertex in line:
                LineStriped.append(int(vertex.split(('/'))[0]))
            Faces.append(tuple(LineStriped))
    return Faces

if __name__ == '__main__':
    Faces = GetFacesFromOBJ(r'3DModels\Suzanne.obj')
    for face in Faces:
        if len(face) > 4:
            print(face)