'''
Created on Jun 6, 2016

@author: castonkr

''' 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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

# Starting position of Rectangle
rect_x = 50
rect_y = 50
 
# Rectangle speed and direction 
rect_vx = 2
rect_vy = 2
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    # Draw rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    
    # Move Rectangle
    rect_x += rect_vx
    rect_y += rect_vy
    
    if rect_x >= WIDTH - 50 or rect_x <= 0:
        rect_vx = -rect_vx
         
    if rect_y >= HEIGHT - 50 or rect_y <= 0:
        rect_vy = -rect_vy
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
