'''
Created on Jun 6, 2016

@author: castonkr

''' 
import pygame, math, random
from pygame.constants import K_DOWN, K_UP, K_RIGHT, K_LEFT, K_SPACE
from pygame.draw import circle
from shutil import which
from pygame import sprite
 
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


# def distance(a , b):
#     return math.sqrt((a.x - b.x)**2 + (a.y - b.y) **2)

class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, dx, dy, color):
        super().__init__()
        self.image = pygame.Surface((radius*2,radius*2));
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.circle(self.image, color, [radius , radius], radius);
        
        self.rect = self.image.get_rect()
#         self.rect = pygame.rect(x, y, radius*2,radius*2);
        self.rect = self.rect.move(x, y)
#         self.rect.x = x
#         self.rect.y = y
        self.radius = radius
        self.dx = dx
        self.dy = dy
#         self.color = color
        
#     def draw(self, surface):
#         pygame.draw.circle(surface, self.color, [self.rect.x , self.rect.y], self.radius);
        
    def update(self):
        self.rect = self.rect.move(self.dx, self.dy)
#         self.rect.x += self.dx
#         self.rect.y += self.dy
        
        if self.rect.x >= WIDTH - self.radius or self.rect.x <= self.radius:
            self.dx *= -1
         
        if self.rect.y >= HEIGHT - self.radius or self.rect.y <= self.radius:
            self.dy *= -1

def randomCircle():
    return Circle(random.randrange(0, WIDTH), random.randrange(0, HEIGHT), 10, 1, 1, WHITE)


class Objs(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, RED, [0, 0,5,5])
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(WIDTH/2, HEIGHT/2)
     
    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.rect.x,self.rect.y,5,5])
    
    def eaten(self):
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, HEIGHT)
        
 

# UP = 1
# DOWN = 2
# RIGHT = 3
# LEFT = 4
class Hero:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 30)
        self.d = K_SPACE
        self.o = K_UP
        
    def update(self):
        if self.d == K_DOWN and self.rect.y < HEIGHT:
            self.rect = self.rect.move(0, 2)
#             hero.y += 2
        elif self.d == K_UP and self.rect.y > 0:
            self.rect = self.rect.move(0, -2)
#             hero.y -= 2
        elif self.d == K_RIGHT and self.rect.x < WIDTH:
            self.rect = self.rect.move(2, 0)
#             hero.x += 2
        elif self.d == K_LEFT and self.rect.x > 0:
            self.rect = self.rect.move(-2, 0)
#             hero.x -= 2
        
    def draw(self, surface):
        # p = [(0 , -30) , (10 , 0) , (20 , -30)]
        p = [(-10 , -10) , (10 , -10) , (0 , 20)]
        if self.o == K_DOWN:
            pos = [(self.rect.x + p[0][0], self.rect.y + p[0][1]), (self.rect.x + p[1][0],self.rect.y + p[1][1]), (self.rect.x + p[2][0],self.rect.y + p[2][1])];
        elif self.o == K_UP:
            pos = [(self.rect.x + p[0][0], self.rect.y - p[0][1]), (self.rect.x + p[1][0],self.rect.y - p[1][1]), (self.rect.x + p[2][0],self.rect.y - p[2][1])];
        elif self.o == K_RIGHT:
            pos = [(self.rect.x + p[0][1], self.rect.y - p[0][0]), (self.rect.x + p[1][1],self.rect.y - p[1][0]), (self.rect.x + p[2][1],self.rect.y - p[2][0])];
        elif self.o == K_LEFT:
            pos = [(self.rect.x - p[0][1], self.rect.y + p[0][0]), (self.rect.x - p[1][1],self.rect.y + p[1][0]), (self.rect.x - p[2][1],self.rect.y + p[2][0])];
        pygame.draw.polygon(surface, BLUE, pos)


class Score:
    def __init__(self):
        self.points = 0
        self.lives = 3
        
    def draw(self,surface):        
        font = pygame.font.SysFont('Calibri', 20, True, False)
        points = font.render("Score: " + str(self.points), True, RED)
        if self.lives > 0:
            lives = font.render("Lives: " + str(self.lives), True, RED)
        else:
            lives = font.render("Game Over", True, RED)
        surface.blit(points,[0,0])
        surface.blit(lives,[0,20])
     

  
# circLs = [Circle(20, 20, 10, 5, 5, WHITE) , Circle(40, 120, 10, 1, 1, WHITE) ]     
obj = Objs()

circLs = pygame.sprite.Group()
circLs.add(Circle(20, 20, 10, 5, 5, GREEN) , Circle(40, 120, 10, 1, 1, GREEN))

hero = Hero(WIDTH/2, HEIGHT/2)
score = Score()           
            
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
    if hero.rect.colliderect(obj.rect):
        obj.eaten()
        score.points += 1
        circLs.add(randomCircle())
    # Draw objects on screen
    
    for c in circLs:
        if hero.rect.colliderect(c.rect):
            print("Hero get hitten")
            score.lives -= 1
#         c.update()
#         c.draw(screen)
#     if pygame.sprite.spritecollide(hero, ci, dokill, collided)
    circLs.update()
    circLs.draw(screen)
    
    hero.update()
    hero.draw(screen)
    obj.draw(screen)
    score.draw(screen)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
