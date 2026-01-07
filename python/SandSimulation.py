import pygame
        
pygame.init()
width,height = 500, 500
backgroundColor = (100, 100, 150)
SandColor = (235, 201, 115)
FPS = 120
Surface = pygame.display.set_mode((width,height))
pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()
clock = pygame.time.Clock()

# SandParticlesPos = [(width//2,height//2),(width//2,0),(width//2,500),(width//2,400),(width//2,600),(width//2,602),(width//2,604),(width//2,606)]
SandParticlesPos = [((i*i)%width,(2*i)-(height//2)) for i in range(height)]

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(FPS)
    pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
        
    for sand in SandParticlesPos:
        if sand[1] >= height-1:
            SandParticlesPos[SandParticlesPos.index(sand)] = (sand[0],height-1)
        else:
            if (sand[0],sand[1]+1) in SandParticlesPos:
                if (sand[0]-1,sand[1]+1) in SandParticlesPos:
                    if (sand[0]+1,sand[1]+1) in SandParticlesPos:
                        pass
                    else:
                        SandParticlesPos[SandParticlesPos.index(sand)] = (sand[0]+1,sand[1]+1)
                else:
                    SandParticlesPos[SandParticlesPos.index(sand)] = (sand[0]-1,sand[1]+1)
            else:
                SandParticlesPos[SandParticlesPos.index(sand)] = (sand[0],sand[1]+1)
        
            
    for sand in SandParticlesPos:
        pygame.draw.rect(Surface, SandColor, pygame.Rect(sand[0],sand[1],1,1))
            
    pygame.display.flip()