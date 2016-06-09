'''
Created on Jun 6, 2016

@author: castonkr

''' 
import pygame, math, random
from pygame.constants import K_DOWN, K_UP, K_RIGHT, K_LEFT, K_SPACE, K_q,\
    K_RETURN
from pygame.draw import circle
from shutil import which
from pygame import sprite
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
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
#         self.color = color
#     def draw(self, surface):
#         pygame.draw.circle(surface, self.color, [self.rect.x , self.rect.y], self.radius);
        
    def update(self):
        self.rect = self.rect.move(self.dx, self.dy)
        
        if self.rect.x >= WIDTH - 2 * self.radius or self.rect.x <= 0:
            self.dx *= -1
         
        if self.rect.y >= HEIGHT - 2 * self.radius or self.rect.y <= 0:
            self.dy *= -1

def randomCircle():
    dx = random.randrange(1, 5)
    dy = random.randrange(1, 5)
    r = random.randrange(3, 15)
    return Circle(random.randrange(0, WIDTH - 2 * r), random.randrange(0, HEIGHT - 2 * r), r, dx, dy, RED)


class Objs(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, GREEN, [0, 0, 5, 5])
        self.rect = self.image.get_rect()
        x = random.randrange(0, WIDTH - 5)
        y = random.randrange(0, HEIGHT - 5)
        self.rect = self.rect.move(x, y)
     
    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.rect.x, self.rect.y, 5, 5])
    
    def eaten(self):
        self.rect.x = random.randrange(0, WIDTH - 5)
        self.rect.y = random.randrange(0, HEIGHT - 5)
        
 

# UP = 1
# DOWN = 2
# RIGHT = 3
# LEFT = 4
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 30))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = pygame.Rect(x, y, 20, 30)
        
#         p = [(0 , 0) , (20 , 0) , (10 , 30)]
        pos = [(0, 30), (20, 30), (10, 0)];
        pygame.draw.polygon(self.image, BLUE, pos)
        self.d = K_SPACE
        self.o = K_UP
    
    def update(self):
        if not self.d == K_SPACE and not self.d == self.o:
            if (self.d == K_UP and self.o == K_RIGHT) or (self.d == K_LEFT and self.o == K_UP) or (self.d == K_DOWN and self.o == K_LEFT) or (self.d == K_RIGHT and self.o == K_DOWN):
                self.image = pygame.transform.rotate(self.image, 90)
            elif (self.o == K_UP and self.d == K_RIGHT) or (self.o == K_LEFT and self.d == K_UP) or (self.o == K_DOWN and self.d == K_LEFT) or (self.o == K_RIGHT and self.d == K_DOWN):
                self.image = pygame.transform.rotate(self.image, -90)
            elif (self.o == K_UP and self.d == K_DOWN) or (self.o == K_DOWN and self.d == K_UP) or (self.o == K_RIGHT and self.d == K_LEFT) or (self.o == K_LEFT and self.d == K_RIGHT):
                self.image = pygame.transform.rotate(self.image, 180)
            self.o = self.d
        if self.d == K_DOWN and self.rect.y < HEIGHT - 30:
            self.rect = self.rect.move(0, 2)
#             hero.y += 2
        elif self.d == K_UP and self.rect.y > 0:
            self.rect = self.rect.move(0, -2)
#             hero.y -= 2
        elif self.d == K_RIGHT and self.rect.x < WIDTH - 30:
            self.rect = self.rect.move(2, 0)
#             hero.x += 2
        elif self.d == K_LEFT and self.rect.x > 0:
            self.rect = self.rect.move(-2, 0)
#             hero.x -= 2
        
#     def draw(self, surface):
#         # p = [(0 , -30) , (10 , 0) , (20 , -30)]
#         p = [(-10 , -10) , (10 , -10) , (0 , 20)]
#         if self.o == K_DOWN:
#             pos = [(self.rect.x + p[0][0], self.rect.y + p[0][1]), (self.rect.x + p[1][0],self.rect.y + p[1][1]), (self.rect.x + p[2][0],self.rect.y + p[2][1])];
#         elif self.o == K_UP:
#             pos = [(self.rect.x + p[0][0], self.rect.y - p[0][1]), (self.rect.x + p[1][0],self.rect.y - p[1][1]), (self.rect.x + p[2][0],self.rect.y - p[2][1])];
#         elif self.o == K_RIGHT:
#             pos = [(self.rect.x + p[0][1], self.rect.y - p[0][0]), (self.rect.x + p[1][1],self.rect.y - p[1][0]), (self.rect.x + p[2][1],self.rect.y - p[2][0])];
#         elif self.o == K_LEFT:
#             pos = [(self.rect.x - p[0][1], self.rect.y + p[0][0]), (self.rect.x - p[1][1],self.rect.y + p[1][0]), (self.rect.x - p[2][1],self.rect.y + p[2][0])];
#         pygame.draw.polygon(surface, BLUE, pos)


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
        pygame.draw.rect(surface,(150,0,0),(0,20,100,20))
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
    done = False
# -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == K_DOWN or event.key == K_UP or event.key == K_RIGHT or event.key == K_LEFT:
                    hero.d = event.key
                elif event.key == K_q:
                    pygame.quit()
                elif event.key == K_RETURN:
                    if score.lives == 1:
                        restart()
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
     
       
        hero.update()
        if hero.rect.colliderect(obj.rect):
            obj.eaten()
            score.points += 1
            newCircle = randomCircle()
            circLs.add(newCircle)
            all_items.add(newCircle)
        # Draw objects on screen
        
        for c in circLs:
            if hero.rect.colliderect(c.rect):
                print("Hero was hit!")
                score.lives -= 1
    #         c.update()
    #         c.draw(screen)
    #     if pygame.sprite.spritecollide(hero, ci, dokill, collided)
        circLs.update()
    #     circLs.draw(screen)
        
        hero.update()
    #     hero.draw(screen)
    #     obj.draw(screen)
        all_items.draw(screen)
        score.draw(screen)
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        if score.lives <= 0:
            score.lives = 1
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
