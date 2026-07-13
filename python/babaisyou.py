import pygame
pygame.init()

background_color = "#383838"


class Baba:
    def __init__(self, pos) -> None:
        self.color = "#ffffff"
        self.pos = pos
        self.istext = False
        self.stop = False
        self.push = False
    def draw(self,screenPropreties):
        cell_size = screenPropreties[1][0]/20
        screen = screenPropreties[0]
        radius = cell_size/2
        canvas_center_pos = (self.pos[0]*cell_size+radius,self.pos[1]*cell_size+radius)
        pygame.draw.circle(screen, self.color, canvas_center_pos, radius)

class Baba_Text:
    def __init__(self, pos) -> None:
        self.type = 0 # Object text
        self.text = "BABA"
        self.color = "#9f3aa1"
        self.pos = pos
        self.istext = True
        self.obj = Baba
        self.stop = False
        self.push = True
    def draw(self,screenPropreties):
        text_font = screenPropreties[2]
        screen = screenPropreties[0]
        cell_size = screenPropreties[1][0]/20
        radius = cell_size/2
        canvas_center_pos = (self.pos[0]*cell_size+radius,self.pos[1]*cell_size+radius)
        rendered_text = text_font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=canvas_center_pos)
        screen.blit(rendered_text,text_rect)

class Wall:
    def __init__(self, pos) -> None:
        self.color = "#3d4e40"
        self.pos = pos
        self.istext = False
        self.stop = False
        self.push = True
    def draw(self,screenPropreties):
        cell_size = screenPropreties[1][0]/20
        screen = screenPropreties[0]
        radius = cell_size/2
        canvas_center_pos = (self.pos[0]*cell_size+radius,self.pos[1]*cell_size+radius)
        pygame.draw.circle(screen, self.color, canvas_center_pos, radius)

class Is_Text:
    def __init__(self, pos) -> None:
        self.type = 1 # Conjunction text
        self.text = "is"
        self.color = "#afafaf"
        self.pos = pos
        self.istext = True
        self.stop = False
        self.push = True
    def draw(self,screenPropreties):
        text_font = screenPropreties[2]
        screen = screenPropreties[0]
        cell_size = screenPropreties[1][0]/20
        radius = cell_size/2
        canvas_center_pos = (self.pos[0]*cell_size+radius,self.pos[1]*cell_size+radius)
        rendered_text = text_font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=canvas_center_pos)
        screen.blit(rendered_text,text_rect)

class You_Text:
    def __init__(self, pos) -> None:
        self.type = 2 # Action text
        self.text = "YOU"
        self.color = "#dc14d9"
        self.pos = pos
        self.istext = True
        self.stop = False
        self.push = True
    def draw(self,screenPropreties):
        text_font = screenPropreties[2]
        screen = screenPropreties[0]
        cell_size = screenPropreties[1][0]/20
        radius = cell_size/2
        canvas_center_pos = (self.pos[0]*cell_size+radius,self.pos[1]*cell_size+radius)
        rendered_text = text_font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=canvas_center_pos)
        screen.blit(rendered_text,text_rect)


class Grid:
    def __init__(self) -> None:
        self.grid = [[[] for _ in range(20)] for _ in range(11)]
        self.you = None
    def draw(self,screenPropreties):
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    obj.draw(screenPropreties)
    def placeObj(self,pos,obj):
        self.grid[pos[1]][pos[0]].append(obj(pos))
    def changeEveryObj(self,old_obj,new_obj):
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj,old_obj):
                        pos = obj.pos
                        self.grid[pos[1]][pos[0]].remove(obj)
                        self.grid[pos[1]][pos[0]].append(new_obj(pos))
    def moveObj(self,obj,dir):
        match dir:
            case "up":
                if obj.pos[1]-1 >= 0:
                    if self.checkPosAndPush([obj.pos[0],obj.pos[1]-1],dir):
                        self.grid[obj.pos[1]][obj.pos[0]].remove(obj)
                        obj.pos[1] -= 1
                        self.grid[obj.pos[1]][obj.pos[0]].append(obj)
            case "left":
                if obj.pos[0]-1 >= 0:
                    if self.checkPosAndPush([obj.pos[0]-1,obj.pos[1]],dir):
                        self.grid[obj.pos[1]][obj.pos[0]].remove(obj)
                        obj.pos[0] -= 1
                        self.grid[obj.pos[1]][obj.pos[0]].append(obj)
            case "down":
                if obj.pos[1]+1 <= 10:
                    if self.checkPosAndPush([obj.pos[0],obj.pos[1]+1],dir):
                        self.grid[obj.pos[1]][obj.pos[0]].remove(obj)
                        obj.pos[1] += 1
                        self.grid[obj.pos[1]][obj.pos[0]].append(obj)
            case "right":
                if obj.pos[0]+1 <= 19:
                    if self.checkPosAndPush([obj.pos[0]+1,obj.pos[1]],dir):
                        self.grid[obj.pos[1]][obj.pos[0]].remove(obj)
                        obj.pos[0] += 1
                        self.grid[obj.pos[1]][obj.pos[0]].append(obj)
                        
    def checkPosAndPush(self,pos,dir):
        isMovementBlocked = False
        movements_to_do = []
        for obj_in_spot in self.grid[pos[1]][pos[0]]:
            if obj_in_spot.stop:
                isMovementBlocked = True
            elif obj_in_spot.push:
                movements_to_do.append((obj_in_spot,dir))
        if isMovementBlocked:
            return False
        else:
            for movement in movements_to_do:
                if not self.moveObj(movement[0],movement[1]):
                    return False
        return True
            
        
    def moveEveryObj(self,obj_to_move,dir):
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj, obj_to_move):
                        self.moveObj(obj,dir)
    def checkGrid(self):
        is_texts = []
        self.you = None
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj,Is_Text):
                        is_texts.append(obj)

        for is_text in is_texts:
            # left
            if is_text.pos[0]-1 >= 0:
                for obj_left in self.grid[is_text.pos[1]][is_text.pos[0]-1]:
                    if obj_left.istext:
                        if obj_left.type == 0:
                            # right
                            if is_text.pos[0]+1 <= 19:
                                for obj_right in self.grid[is_text.pos[1]][is_text.pos[0]+1]:
                                    if obj_right.istext:
                                        if obj_right.type == 0:
                                            self.changeEveryObj(type(obj_left),type(obj_right))
                                        elif obj_right.type == 2:
                                            match obj_right.text:
                                                case "YOU":
                                                    self.you = obj_left.obj
                                                    
                                                    
                                                
                                        
                                            
                                            
class Game:
    def __init__(self, res=(1920,1080)) -> None:
        
        self.res = res
        self.screen = pygame.display.set_mode(res)
        self.screen.fill(background_color)
        pygame.display.flip()
        
        self.text_font = pygame.font.SysFont('Segoe UI Symbol', 30, bold=True)
        
        self.running = False
        self.grid = Grid()
        
        self.grid.placeObj([10,5],Baba)
        self.grid.placeObj([9,7],Baba_Text)
        self.grid.placeObj([10,7],Is_Text)
        self.grid.placeObj([11,7],You_Text)
        self.grid.placeObj([10,2],Wall)
    def run(self):
        self.running = True
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                elif e.type == pygame.KEYDOWN:
                    match e.key:
                        case pygame.K_ESCAPE:
                            self.running = False
                            pygame.quit()
                            quit()
                        case pygame.K_UP:
                            self.grid.checkGrid()
                            if self.grid.you != None:
                                self.grid.moveEveryObj(self.grid.you, "up")
                        case pygame.K_LEFT:
                            self.grid.checkGrid()
                            if self.grid.you != None:
                                self.grid.moveEveryObj(self.grid.you, "left")
                        case pygame.K_DOWN:
                            self.grid.checkGrid()
                            if self.grid.you != None:
                                self.grid.moveEveryObj(self.grid.you, "down")
                        case pygame.K_RIGHT:
                            self.grid.checkGrid()
                            if self.grid.you != None:
                                self.grid.moveEveryObj(self.grid.you, "right")
                                
            # Main loop
            self.update()
            
    def update(self):
        self.screen.fill(background_color)
        self.grid.draw([self.screen, self.res, self.text_font])
        pygame.display.flip()
    


game = Game()
game.run()