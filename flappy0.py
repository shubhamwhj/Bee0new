import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
#Add code to create an empty dictionary "images"

#add code to load the bird and the ground images in the dictionary("base.png", "redbird-midflap.png")

#uncomment this part to load rest of the images.
# images["bg1"] = pygame.image.load("bg1.png").convert_alpha()
# images["pipe"] = pygame.image.load("pipe-red.png").convert_alpha()
# images["message"] = pygame.image.load("message.png").convert_alpha()
# images["over"] = pygame.image.load("gameover.png").convert_alpha()
# images["cloud"]=pygame.image.load("cloud.png").convert_alpha()

#create a rectangle for the bee.


while True:    
    screen.fill((50,150,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #Add code to display bee and thr ground images.
   
    pygame.display.update()
    clock.tick(30)

