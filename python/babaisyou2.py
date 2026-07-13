import pygame

import pygame
pygame.init()

background_color = "#383838"            

class Wall:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.isPush = False
        self.isStop = False
        self.color = "#8a8a8a"
        self.isText = False
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
    
        # pygame.draw.rect(self.screen,"#ffffff",(canvas_top_left[0],canvas_top_left[1],canvas_size[0],canvas_size[1]))
        pygame.draw.rect(self.screen,self.color,(cell_top_left[0],cell_top_left[1],cell_size,cell_size))


class Wall_Text:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.font = screen_param[2]
        self.isPush = True
        self.isStop = False
        self.color = "#6f4928"
        self.text = "WALL"
        self.obj = Wall
        self.isText = True
        self.text_type = 0 # Objects
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
        radius = cell_size/2
        rendered_text = self.font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=(cell_top_left[0]+radius,cell_top_left[1]+radius))
        self.screen.blit(rendered_text,text_rect)


class Baba:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.isPush = False
        self.isStop = False
        self.color = "#bfa2c0"
        self.isText = False
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
        radius = cell_size/2
        
        # pygame.draw.rect(self.screen,"#ffffff",(canvas_top_left[0],canvas_top_left[1],canvas_size[0],canvas_size[1]))
        pygame.draw.circle(self.screen,self.color,(cell_top_left[0]+radius,cell_top_left[1]+radius),radius)
            
class Baba_Text:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.font = screen_param[2]
        self.isPush = True
        self.isStop = False
        self.color = "#b84abc"
        self.text = "BABA"
        self.obj = Baba
        self.isText = True
        self.text_type = 0 # Objects
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
        radius = cell_size/2
        rendered_text = self.font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=(cell_top_left[0]+radius,cell_top_left[1]+radius))
        self.screen.blit(rendered_text,text_rect)
        

class Is_Text:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.font = screen_param[2]
        self.isPush = True
        self.isStop = False
        self.color = "#949494"
        self.text = "IS"
        self.isText = True
        self.text_type = 1 # Conjunctions
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
        radius = cell_size/2
        rendered_text = self.font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=(cell_top_left[0]+radius,cell_top_left[1]+radius))
        self.screen.blit(rendered_text,text_rect)

class You_Text:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.font = screen_param[2]
        self.isPush = True
        self.isStop = False
        self.color = "#9B4BC7"
        self.text = "YOU"
        self.isText = True
        self.text_type = 2 # Actions
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
        radius = cell_size/2
        rendered_text = self.font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=(cell_top_left[0]+radius,cell_top_left[1]+radius))
        self.screen.blit(rendered_text,text_rect)
        

class Stop_Text:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.font = screen_param[2]
        self.isPush = True
        self.isStop = False
        self.color = "#865B22"
        self.text = "STOP"
        self.isText = True
        self.text_type = 2 # Actions
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
        radius = cell_size/2
        rendered_text = self.font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=(cell_top_left[0]+radius,cell_top_left[1]+radius))
        self.screen.blit(rendered_text,text_rect)
        
class Push_Text:
    def __init__(self,pos,screen_param) -> None:
        self.pos = pos
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.font = screen_param[2]
        self.isPush = True
        self.isStop = False
        self.color = "#D1D863"
        self.text = "PUSH"
        self.isText = True
        self.text_type = 2 # Actions
    def draw(self,canvas):
        canvas_top_left = canvas[0]
        canvas_size = canvas[1]
        cell_size = canvas[2]
        cell_top_left = [(cell_size*self.pos[0]*canvas_size[0]/self.res[0])+canvas_top_left[0],(cell_size*self.pos[1]*canvas_size[1]/self.res[1])+canvas_top_left[1]]
        radius = cell_size/2
        rendered_text = self.font.render(self.text,True,self.color)
        text_rect = rendered_text.get_rect(center=(cell_top_left[0]+radius,cell_top_left[1]+radius))
        self.screen.blit(rendered_text,text_rect)

class Grid:
    def __init__(self ,size,screen_param):
        self.screen_param = screen_param
        self.size = size
        self.grid = [[[] for _ in range(size[0])] for _ in range(size[1])]
        self.screen = screen_param[0]
        self.res = screen_param[1]
        self.size = size
        self.canvas = self.getCanvas()
    def placeObj(self,pos,obj):
        self.grid[pos[1]][pos[0]].append(obj(pos,self.screen_param))
    def draw(self):
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    obj.draw(self.canvas)
    def getCanvas(self):
        screen_aspect_ratio = self.res[0]/self.res[1] # Change if res changes
        grid_aspect_ratio = self.size[0]/self.size[1]
        aspect_ratios_diffrence = screen_aspect_ratio - grid_aspect_ratio
        if aspect_ratios_diffrence >= 0:
            canvas_top_left = [aspect_ratios_diffrence*self.res[0]/2, 0] # Change if res changes
            canvas_size = [self.res[0]*(1-aspect_ratios_diffrence), self.res[1]] # Change if res changes
            self.cell_size = self.res[1]/self.size[1]
        else:
            x = screen_aspect_ratio/grid_aspect_ratio
            canvas_top_left = [0, self.res[1]*(1-x)/2] # Change if res changes
            canvas_size = [self.res[0], self.res[1]*x] # Change if res changes
            self.cell_size = canvas_size[0]/self.size[0]
        return [canvas_top_left,canvas_size,self.cell_size]
    def movementLogic(self,obj,dir):
        x,y = obj.pos[0],obj.pos[1]
        match dir:
            case "up":
                next_pos = (x,y-1)
            case "left":
                next_pos = (x-1,y)
            case "down":
                next_pos = (x,y+1)
            case "right":
                next_pos = (x+1,y)
        if self.isBound(next_pos):
            if not self.checkStop(next_pos):
                if self.checkPush(next_pos):
                    for obj_to_push in self.grid[next_pos[1]][next_pos[0]]:
                        if obj_to_push.isPush:
                            if self.movementLogic(obj_to_push,dir):
                                self.moveObj(obj,next_pos)
                                return True
                            else:
                                return False
                else:
                    self.moveObj(obj,next_pos)
                    return True
            else:
                return False
    def moveEverything(self,obj_class,dir):
        objects_to_move = []
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj,obj_class):
                        objects_to_move.append(obj)
        for obj in objects_to_move:
            self.movementLogic(obj,dir)
    def moveObj(self,obj,pos):
        self.grid[obj.pos[1]][obj.pos[0]].remove(obj)
        self.grid[pos[1]][pos[0]].append(obj)
        obj.pos = pos
    def isBound(self,pos):
        x = pos[0]
        y = pos[1]
        if x < 0 or x >= self.size[0] or y < 0 or y >= self.size[1]:
            return False
        return True
    def checkStop(self,pos):
        isStop = False
        for obj in self.grid[pos[1]][pos[0]]:
            if obj.isStop: isStop = True
        return isStop
    def checkPush(self,pos):
        isPush = False
        for obj in self.grid[pos[1]][pos[0]]:
            if obj.isPush: isPush = True
        return isPush
    def replaceEveryObj(self,old_obj_class,new_obj_class):
        isChanging = False
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj,old_obj_class):
                        self.grid[obj.pos[1]][obj.pos[0]].remove(obj)
                        self.grid[obj.pos[1]][obj.pos[0]].append(new_obj_class(obj.pos,self.screen_param))
                        isChanging = True
        if isChanging:
            print('hello')
            self.checkGrid()
    def changeStop(self,obj_class,value):
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj,obj_class):
                        obj.isStop = value
    def changePush(self,obj_class,value):
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj,obj_class):
                        obj.isPush = value         
    def resetVars(self):
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if not obj.isText:
                        obj.isPush = False        
                        obj.isStop = False        
    def checkGrid(self):
        self.resetVars()
        lefties_group = []
        righties_group = []
        you = None
        for line in self.grid:
            for cell in line:
                for obj in cell:
                    if isinstance(obj, Is_Text):
                        if self.isBound((obj.pos[0]-1,obj.pos[1])):
                            lefties_group = self.grid[obj.pos[1]][obj.pos[0]-1]
                        if self.isBound((obj.pos[0]+1,obj.pos[1])):
                            righties_group = self.grid[obj.pos[1]][obj.pos[0]+1]
                        if self.isBound((obj.pos[0],obj.pos[1]-1)):
                            up_group = self.grid[obj.pos[1]-1][obj.pos[0]]
                        if self.isBound((obj.pos[0],obj.pos[1]+1)):
                            down_group = self.grid[obj.pos[1]+1][obj.pos[0]]
                        you = self.checkNextToIs(lefties_group,righties_group) + self.checkNextToIs(up_group,down_group)
        return you
    def checkNextToIs(self,group1,groupe2):
        you = []
        for lefty in group1:
            if lefty.isText:
                if lefty.text_type == 0:
                    for righty in groupe2:
                        if righty.isText:
                            if righty.text_type == 0:
                                self.replaceEveryObj(lefty.obj,righty.obj)
                            elif righty.text_type == 2:
                                if isinstance(righty,You_Text):
                                    you.append(lefty.obj)
                                if isinstance(righty,Stop_Text):
                                    self.changeStop(lefty.obj,True)
                                if isinstance(righty,Push_Text):
                                    self.changePush(lefty.obj,True)
        return you
                                                
                                                


class Game:
    def __init__(self, res=(1920,1080)) -> None:
        
        self.res = res
        self.screen = pygame.display.set_mode(res)
        self.screen.fill(background_color)
        pygame.display.flip()
        
        self.text_font = pygame.font.SysFont('Segoe UI Symbol', 30, bold=True)
        
        self.running = False
        self.grid = Grid([16,9],[self.screen, self.res, self.text_font])
        self.you = None
        
        self.grid.placeObj([7,4],Baba)
        self.grid.placeObj([6,3],Baba_Text)
        self.grid.placeObj([7,3],Is_Text)
        self.grid.placeObj([8,3],You_Text)
        self.grid.placeObj([10,3],You_Text)
        self.grid.placeObj([7,2],Wall)
        self.grid.placeObj([7,1],Wall_Text)
        self.grid.placeObj([8,1],Is_Text)
        self.grid.placeObj([10,1],Stop_Text)
        self.grid.placeObj([11,1],Push_Text)
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
                            self.you = self.grid.checkGrid()
                            if self.you != None : 
                                for yu in self.you : self.grid.moveEverything(yu,"up")
                            self.you = self.grid.checkGrid()
                        case pygame.K_LEFT:
                            self.you = self.grid.checkGrid()
                            if self.you != None : 
                                for yu in self.you : self.grid.moveEverything(yu,"left")
                            self.you = self.grid.checkGrid()
                        case pygame.K_DOWN:
                            self.you = self.grid.checkGrid()
                            if self.you != None : 
                                for yu in self.you : self.grid.moveEverything(yu,"down")
                            self.you = self.grid.checkGrid()
                        case pygame.K_RIGHT:
                            self.you = self.grid.checkGrid()
                            if self.you != None : 
                                for yu in self.you : self.grid.moveEverything(yu,"right")
                            self.you = self.grid.checkGrid()
                                
            # Main loop
            self.update()
            
    def update(self):
        self.screen.fill(background_color)
        self.grid.draw()
        pygame.display.flip()
    


game = Game()
game.run()

# TODO make text work vertical
