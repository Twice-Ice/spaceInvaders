import pygame
import random

pygame.init()
pygame.display.set_caption("Space Invaders")
screenX = 800
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
gameover = False
armada = []

#vars
playerX = 400
playerY = 750
moveLeft = False
moveRight = False
runSpeed = 5
vx = 0

#classes/aliens
class Alien:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
    def adjustColor(self):
        r = random.randint(-10, 10)
        if self.r + r > 255:
            self.r = 255
        elif self.r + r < 0:
            self.r = 0
        else:
            self.r += r
        g = random.randint(-10, 10)
        if self.g + g > 255:
            self.g = 255
        elif self.g + g < 0:
            self.g = 0
        else:
            self.g += g
        b = random.randint(-10, 10)
        if self.b + b > 255:
            self.b = 255
        elif self.b + b < 0:
            self.b = 0
        else:
            self.b += b
    def draw(self):
        pygame.draw.rect(screen, (self.r, self.g, self.b), (self.xpos, self.ypos, 40, 40))

#functions
def moveLeft():
    global vx
    if vx > -runSpeed:
        vx -= 1
        
def moveRight():
    global vx
    if vx < runSpeed:
        vx += 1
        
def friction():
    global vx
    if abs(vx) < 1:
        vx = 0
    elif vx < 0:
        vx += 1
    elif vx > 0:
        vx -= 1

def gameInit():
    global armada
    for i in range(5):
        for j in range(10):
            armada.append(Alien(j*60+50, i*50+50))
    
gameInit()

while not gameover:
    clock.tick(60)
    
    #input section
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        moveLeft()
    if keys[pygame.K_d]:
        moveRight()
    if not keys[pygame.K_d] and not keys[pygame.K_a]:
        friction()
                
    #physics section
    playerX += vx
            
    #render section
    screen.fill((25, 25, 75))
    
    #player renderer
    pygame.draw.rect(screen, (200, 200, 100), (playerX, playerY, 60, 20))
    pygame.draw.rect(screen, (200, 200, 100), (playerX + 5, playerY - 5, 50, 20))
    pygame.draw.rect(screen, (200, 200, 100), (playerX + 45/2, playerY - 15, 15, 20))
    pygame.draw.rect(screen, (200, 200, 100), (playerX + 55/2, playerY - 20, 5, 20))
 
    for i in range(len(armada)):
        
        armada[i].draw()
        armada[i].adjustColor()
 
    pygame.display.flip()
    
pygame.quit()