'''
Created on Jun 6, 2016

@author: castonkr

''' 
import pygame, math, random
from pygame.constants import K_DOWN, K_UP, K_RIGHT, K_LEFT, K_SPACE
from pygame.draw import circle
from shutil import which
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def distance(a , b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y) **2)

class Circle:
    def __init__(self, initX, initY, radius, dx, dy, color):
        self.x = initX
        self.y = initY
        self.radius = radius
        self.dx = dx
        self.dy = dy
        self.color = color
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, [self.x , self.y], self.radius);
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x >= WIDTH - self.radius or self.x <= self.radius:
            self.dx *= -1
         
        if self.y >= HEIGHT - self.radius or self.y <= self.radius:
            self.dy *= -1

def randomCircle():
    return Circle(random.randrange(0, WIDTH), random.randrange(0, HEIGHT), 10, 1, 1, WHITE)


circLs = [Circle(20, 20, 10, 5, 5, WHITE) , Circle(40, 120, 10, 1, 1, WHITE) ]

class Objs:    
    def __init__(self):
        self.x = 300
        self.y = 300
     
    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.x,self.y,5,5])
    
    def eaten(self):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        
        
obj = Objs()

# UP = 1
# DOWN = 2
# RIGHT = 3
# LEFT = 4
class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = K_SPACE
        self.o = K_UP
        self.lives = 3
        
    def update(self):
        if self.x >= WIDTH or self.x <= 0 or self.y >= HEIGHT or self.y <= 0:
            self.d = K_SPACE
        
        if self.d == K_DOWN:
            hero.y += 2
        elif self.d == K_UP:
            hero.y -= 2
        elif self.d == K_RIGHT:
            hero.x += 2
        elif self.d == K_LEFT:
            hero.x -= 2
                
        
    def draw(self, surface):
        # p = [(0 , -30) , (10 , 0) , (20 , -30)]
        p = [(-10 , -10) , (10 , -10) , (0 , 20)]
        if self.o == K_DOWN:
            pos = [(self.x + p[0][0], self.y + p[0][1]), (self.x + p[1][0],self.y + p[1][1]), (self.x + p[2][0],self.y + p[2][1])];
        elif self.o == K_UP:
            pos = [(self.x + p[0][0], self.y - p[0][1]), (self.x + p[1][0],self.y - p[1][1]), (self.x + p[2][0],self.y - p[2][1])];
        elif self.o == K_RIGHT:
            pos = [(self.x + p[0][1], self.y - p[0][0]), (self.x + p[1][1],self.y - p[1][0]), (self.x + p[2][1],self.y - p[2][0])];
        elif self.o == K_LEFT:
            pos = [(self.x - p[0][1], self.y + p[0][0]), (self.x - p[1][1],self.y + p[1][0]), (self.x - p[2][1],self.y + p[2][0])];
        pygame.draw.polygon(surface, BLUE, pos)

hero = Hero(WIDTH/2, HEIGHT/2)
     
            
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT:
                hero.d = event.key
                hero.o = event.key
        elif event.type == pygame.KEYUP:
            hero.d = K_SPACE
            
    #     print(pygame.KEYDOWN)
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    # Draw rectangle
    hero.update()
    if distance(hero, obj) < 10:
        obj.eaten();
        circLs.append(randomCircle())
    
    for c in circLs:
        if distance(hero, c) < 10:
            hero.lives -= 1;
            print("Hero get hitten")
            if hero.lives <= 0:
                print("Hero dies");
        c.update()
        c.draw(screen)
    
    hero.draw(screen)
    obj.draw(screen)
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
