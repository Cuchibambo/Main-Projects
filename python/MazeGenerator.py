import random

Maze = [
    [1,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

MazePathH = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]    
]

MazePathV = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]  
]

SelectedNode = [0],[0]

def SelectRadomNode(Maze):
    # Step 1: Select a random row index
    random_row_index = random.randint(0, len(Maze) - 1)

    # Step 2: Select a random column index from the selected row
    random_col_index = random.randint(0, len(Maze[random_row_index]) - 1)

    # Get the random node
    random_node = Maze[random_row_index][random_col_index]

    # Print the position and value of the random node
    print(f"Random node at position ({random_row_index}, {random_col_index}): {random_node}")
    
    return random_node, random_row_index, random_col_index
    
def FindRandomNewNode(Maze):
    random_node = SelectRadomNode(Maze)
    if random_node[0] == 0:
        return random_node[1], random_node[2]
    else:
        return FindRandomNewNode(Maze)

def Assign1toRadomNode(Maze,SelectedNode):
    SelectedNode = FindRandomNewNode(Maze)
    Maze[SelectedNode[0]][SelectedNode[1]] = 1
    
Assign1toRadomNode(Maze)

PossibleNodes = [SelectedNode[0],[1]]

print(Maze)