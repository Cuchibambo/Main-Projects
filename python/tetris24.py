import pygame

class Test_Piece:
    def __init__(self,pos):
        self.color = "#d4701f"
        self.shape = []
        self.pos = pos

class Tetris:
    def __init__(self):
        self.running = False
        self.board = [None for _ in range(240)]

    def run(self):
        # Start Pygame
        pygame.init()
        self.text_font = pygame.font.SysFont('Segoe UI Symbol', 45, bold=False)
        self.width,self.height = 500, 500
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen.fill(self.background_color)
        pygame.display.flip()
        # Time and delta time
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.dt = 1/self.FPS

        self.running = True
        self.GRAVITY_EVENT = pygame.USEREVENT
        pygame.time.set_timer(self.GRAVITY_EVENT,1000,1)

        self.board[40] = Test_Piece([0,0])

        # Colors
        self.background_color = "#333333"
        self.outline_color = "#ffffff"
        self.cell_color = "#373737"

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            self.leftClick(pygame.mouse.get_pos())
                        case 3:
                            self.rightClick(pygame.mouse.get_pos())
                elif event.type == self.GRAVITY_EVENT:
                    self.active_block.pos[1] -= 1
                    self.update_cell_ownership()

            self.clock.tick(self.FPS) # appply fps
            self.update()
            pygame.display.flip() # Update Screen

    def update(self):
        self.screen.fill(self.background_color)
        self.drawboard()
    
    def leftClick(self,MousePos):
        return
    
    def rightClick(self,MousePos):
        return

    def move(self,direction):
        # -1 is left, 1 is right
        return

    def drop(self):
        return
    
    def drawboard(self):
        outline_width = 1
        board_size = (200,400)
        cell_size = board_size[0]//10
        top_left = ((self.width-board_size[0])/2,
                    (self.height-board_size[1])/2)
        pygame.draw.rect(self.screen,self.outline_color,(top_left[0],top_left[1],board_size[0],board_size[1]))
        for x in range(10):
            for y in range(20):
                current_piece = self.board[x + 10 * (y+4)]
                if current_piece == None: color = self.cell_color
                else: color = current_piece.color
                pygame.draw.rect(self.screen,color,(top_left[0]+outline_width+x*cell_size,top_left[1]+outline_width+y*cell_size,cell_size-outline_width*2,cell_size-outline_width*2))
        
    def update_cell_ownership(self):
        for i in range(240):
            if self.board[i] != None:
                

game = Tetris()
game.run()