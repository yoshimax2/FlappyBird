#Imports necessary variables and starts Pygame
import sys, pygame, time, random
pygame.init()

#Scrolls left
def scrollX(screenSurf, offsetX):
    width, height = screenSurf.get_size()
    copySurf = screenSurf.copy()
    screenSurf.blit(copySurf, (offsetX, 0))
    if offsetX < 0:
        screenSurf.blit(copySurf, (width + offsetX, 0), (0, 0, -offsetX, height))
    else:
        screenSurf.blit(copySurf, (0, 0), (width - offsetX, 0, offsetX, height))

#Ends game - need to change this to show score on screen
def game_over():
    screen.blit(wp, wprect)
    screen.blit(pipe,piperect)
    screen.blit(pipebottom,pipebotrect)
    screen.blit(bird, birdrect)
    print("GAME OVER")
    print("You scored:", score)
    screen.blit(go, gorect)
    #pygame.display.update()
    pygame.display.flip()
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

#Checks for any collisions with the pipes
def check_collisions():
  if birdrect.colliderect(piperect):game_over()
  if birdrect.colliderect(pipebotrect):game_over()

#Gets information about display then sets size
display_inf = pygame.display.Info()
size = width, height = display_inf.current_w, display_inf.current_h

#Sets speed of moving right?
if width>800:
  right = width/800
else:
  right = 1

#Sets automatic move right speed
auto_right = width/30
auto_down = height/30

#Sets speed of moving down
if height>800:
  down = height/800
else:
  down = 1

#Additional right and down vars? This is messy - fix it
sp_right = width/10
sp_down = height/8

#Sets speed
speed = 2

#Offset of pipes moving
offset = -3*speed

#Creates some RGB colour variables
purple = 200, 0, 255
blue = 100, 100, 255
black = 0,0,0

#Sets up dowhile loop entry boolean
started = False

#Sets variables to 0
score = 0
counter = 0
num=0

#Creates clock to control execution speed
clock = pygame.time.Clock()
FPS = 120

#Sets up screen
screen = pygame.display.set_mode(size)

#Loads images
wp = pygame.image.load("flappybirdbg.png")
go = pygame.image.load("flappyBirdGameOver.png")
bird = pygame.image.load("flapbird.png")

#Resizes images
go = pygame.transform.scale(go, (width//3,height//4))
wp = pygame.transform.scale(wp, (width,height))
bird = pygame.transform.scale(bird, (width//15,height//13))

#Sets up rectangles for images
gorect = go.get_rect(center=(width//2, height//2))
birdrect = bird.get_rect(center = (width//2, height//2))
wprect = wp.get_rect()

#Sets up pipes
pipes=[]

#Adds top pipe
pipe = pygame.image.load("pipetop.png").convert_alpha()
pipe = pygame.transform.scale(pipe, (width//10,height//3))
piperect = pipe.get_rect(center=(width, pipe.get_height()//2))
screen.blit(pipe, piperect)

#Adds bottom pipe
pipebottom = pygame.image.load("pipebottom.png").convert_alpha()
pipebottom = pygame.transform.scale(pipebottom, (width//10,height//3))
pipebotrect = pipebottom.get_rect(center=(width, height-(pipebottom.get_height()//2)))
screen.blit(pipebottom,pipebotrect)

#Game loop
while True:
  clock.tick(FPS)

  if not started:
        
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN and event.key == 32:
        for i in range(20):
          started = True
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

  else:
    birdrect = birdrect.move(0, down*speed+1)
  
    
    scrollX(wp, offset)
    counter-=offset
    piperect = piperect.move(offset,0)
    pipebotrect = pipebotrect.move(offset,0)
    screen.blit(pipe,piperect)
    screen.blit(pipebottom,pipebotrect)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == 32:

            for i in range(15):
                screen.blit(pipe,piperect)
                screen.blit(pipebottom,pipebotrect)
                birdrect.y-=8

            pygame.display.update()
            check_collisions()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
  if birdrect.bottom > (height*(19/20)):
    game_over()
  if counter>width//2:
    score+=1
    counter = 0
  if piperect.right<=0:

    pipes.append(pygame.image.load("pipetop.png").convert_alpha())
    pipes[num] = pygame.transform.scale(pipes[num], (width//10,height//3))
    #piperect = pipes[num].get_rect(center=(width, piperect.h//2))
    heightdiv = random.randint(10,40)/10
    piperect = pipes[num].get_rect(center=(width, piperect.h//heightdiv))
    topheight = piperect.h
    screen.blit(pipes[num], piperect)
    num+=1
    pipes.append(pygame.image.load("pipebottom.png").convert_alpha())
    pipes[num] = pygame.transform.scale(pipes[num], (width//10,height//3))
    #pipebotrect = pipes[num].get_rect(center=(width, height-(pipes[num].get_height()//2)))
    pipebotrect = pipes[num].get_rect(center=(width, piperect.bottom+(height//2)))
    screen.blit(pipes[num],pipebotrect)
    num+=1
  check_collisions()
    
  
  #screen.fill(blue)
  screen.blit(wp, wprect)
  screen.blit(bird, birdrect)
  screen.blit(pipe, piperect)
  screen.blit(pipebottom, pipebotrect)
  pygame.display.flip()

