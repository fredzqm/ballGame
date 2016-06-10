'''
Created on Jun 6, 2016

@author: castonkr

''' 
import pygame, math, random
from pygame.constants import K_DOWN, K_UP, K_RIGHT, K_LEFT, K_SPACE, K_q, \
    K_RETURN, MOUSEBUTTONDOWN
from pygame.draw import circle
from shutil import which
from pygame import sprite
from math import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Distance Formula
def distance(point1, point2):
        return math.sqrt((point1[1] - point2[1]) ** 2 + (point1[0] - point2[0]) ** 2)
     
pygame.init()
 
# Set the width and height of the screen [width, height]
WIDTH = 700
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ball Game")

# Start Menu
ball = pygame.image.load("ball.png")
# background = pygame.image.load("ballgame_background.")
title_font = pygame.font.SysFont('Calibri',75)
title_text = title_font.render('Play Ball Game', True, WHITE)
other_font = pygame.font.SysFont('Calibri', 25, bold = True)
start_text = other_font.render("Start Game", True, WHITE)
screen.blit(ball,[315,300])
screen.blit(title_text, [125,125])
screen.blit(start_text, [300,325])
pygame.display.flip()
start_game = True
my_clock = pygame.time.Clock()
while start_game:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()  
            if distance((355,340), a) < 40:
                start_game = False
            if start_game is True:
                my_clock = 0
            
                

 
# Loop until the user clicks the close button.
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
all_items = pygame.sprite.Group()
circLs = pygame.sprite.Group()

# def distance(a , b):
#     return math.sqrt((a.x - b.x)**2 + (a.y - b.y) **2)

class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, dx, dy, color):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2));
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.circle(self.image, color, [radius , radius], radius);
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)
        self.radius = radius
        self.dx = dx
        self.dy = dy
        
    def update(self):
        self.rect = self.rect.move(self.dx, self.dy)
        
        if self.rect.x >= WIDTH - 2 * self.radius or self.rect.x <= 0:
            self.dx *= -1
         
        if self.rect.y >= HEIGHT - 2 * self.radius or self.rect.y <= 0:
            self.dy *= -1
            
# def circileCollide(a, b):
    

def randomCircle():
    dx = random.randrange(1, 5)
    dy = random.randrange(1, 5)
    r = random.randrange(3, 15)
    return Circle(random.randrange(0, WIDTH - 2 * r), random.randrange(0, HEIGHT - 2 * r), r, dx, dy, RED)


class Objs(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, GREEN, [0, 0, 5, 5])
        self.rect = self.image.get_rect()
        x = random.randrange(100, WIDTH - 5)
        y = random.randrange(40, HEIGHT - 5)
        self.rect = self.rect.move(x, y)
     
    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.rect.x, self.rect.y, 5, 5])
    
    def eaten(self):
        self.rect.x = random.randrange(0, WIDTH - 5)
        self.rect.y = random.randrange(0, HEIGHT - 5)
        
 
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 30))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = pygame.Rect(x, y, 20, 30)
        
        pos = [(0, 30), (20, 30), (10, 0)];
        pygame.draw.polygon(self.image, BLUE, pos)
        self.imageUp = self.image.copy()
        
        self.d = K_SPACE
        self.o = K_UP
        self.key = 0b0000
        
        
    def update(self):
        if self.key == 0b1000:
            self.rect.move_ip(0, -2)
            self.image = self.imageUp.copy()
        elif self.key == 0b0100:
            self.rect.move_ip(2, 0)  
            self.image = pygame.transform.rotate(self.imageUp, -90)
        elif self.key == 0b0010:
            self.rect.move_ip(0, 2)
            self.image = pygame.transform.rotate(self.imageUp, 180)
        elif self.key == 0b0001:
            self.rect.move_ip(-2, 0)  
            self.image = pygame.transform.rotate(self.imageUp, 90)
        elif self.key == 0b1100:
            self.rect.move_ip(1.414, -1.414)
            self.image = pygame.transform.rotate(self.imageUp, -45)
        elif self.key == 0b0110:
            self.rect.move_ip(1.414, 1.414)  
            self.image = pygame.transform.rotate(self.imageUp, -135)
        elif self.key == 0b0011:
            self.rect.move_ip(-1.414, 1.414)
            self.image = pygame.transform.rotate(self.imageUp, 135)
        elif self.key == 0b1001:
            self.rect.move_ip(-1.414, -1.414)
            self.image = pygame.transform.rotate(self.imageUp, 45)

        if self.rect.y + self.rect.h > HEIGHT:
            self.rect.y = HEIGHT - self.rect.h
        elif self.rect.y < 0:
            self.rect.y = 0
        if self.rect.x + 30 > WIDTH:
            self.rect.x = WIDTH - 30
        elif self.rect.x < 0:
            self.rect.x = 0

    
    def keyDown(self, key):
        if key == K_UP:
            self.key |= 0b1000
        elif key == K_RIGHT:
            self.key |= 0b0100
        elif key == K_DOWN:
            self.key |= 0b0010
        elif key == K_LEFT:
            self.key |= 0b0001
    
    def keyUp(self, key):
        if key == K_UP:
            self.key &= 0b0111
        elif key == K_RIGHT:
            self.key &= 0b1011
        elif key == K_DOWN:
            self.key &= 0b1101
        elif key == K_LEFT:
            self.key &= 0b1110
    
class Score:
    def __init__(self):
        self.init()
        
    def init(self):
        self.points = 0
        self.lives = 100
    
    def draw(self, surface):        
        font = pygame.font.SysFont('Calibri', 20, True, False)
        text1 = font.render("Score: " + str(self.points), True, WHITE)
        # health_bar 
        pygame.draw.rect(surface, (150, 0, 0), (0, 20, 100, 20))
        pygame.draw.rect(surface, (0, 150, 0), (0, 20, self.lives, 20))
        if self.lives > 0:
            text2 = font.render("Health: " + str(self.lives), True, WHITE)
        else:
            text2 = font.render("Game Over!", True, RED)            
        surface.blit(text1, [0, 0])
        surface.blit(text2, [0, 20])
     
     
hero = Hero(WIDTH / 2, HEIGHT / 2)
obj = Objs()
score = Score()         

def restart():
    score.init()
    circ1 = randomCircle()
    circ2 = randomCircle()
    circLs.add(circ1 , circ2)
    print("restart")
    global all_items
    all_items.empty()
    all_items.add(circ1, circ2, hero, obj)

    

def main():
# -------- Main Program Loop -----------
    while True:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT:
                    hero.keyDown(event.key)
                elif event.key == K_q:
                    exit()
                elif event.key == K_RETURN:
                    if score.lives == 0:
                        restart()
            elif event.type == pygame.KEYUP:
                hero.keyUp(event.key)
                
        screen.fill(BLACK)
     
       
        hero.update()
        if hero.rect.colliderect(obj.rect):
            obj.eaten()
            score.points += 1
            newCircle = randomCircle()
            circLs.add(newCircle)
            all_items.add(newCircle)
        # Draw objects on screen
        
        
        if pygame.sprite.spritecollide(hero, circLs, False):
            print("Hero was hit!")
            score.lives -= 1
        
#         ls = circLs.sprintes()
#         for i in range(len(ls)):
#             for j in range(i+1, len(ls)):
#                 if ls[i].rect.colliderect(ls[j].rect):
#                     circileCollide(ls[i], ls[j])
        
        circLs.update()
        
        hero.update()
        all_items.draw(screen)
        score.draw(screen)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        if score.lives <= 0:
            score.lives = 0
            all_items.empty() 
            circLs.empty()
            game_over = pygame.sprite.Sprite()
            message = pygame.Surface((400, 200))
            
            font = pygame.font.SysFont('Calibri', 20, True, False)
            text1 = font.render("Game Over, Press Enter to start new game", True, WHITE)
            text2 = font.render("Q to quit", True, WHITE)          
            message.blit(text1, [0, 0])
            message.blit(text2, [0, 20])
            
            game_over.image = message
      
            game_over.rect = message.get_rect()
            game_over.rect.move_ip(200, 200)
            all_items.add(game_over)
           
        clock.tick(60)
     
# Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    restart()
    main()
