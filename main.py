import pygame
import random
from Tree import Tree
from Mm import Mm

# PYGAME=====================
pygame.init()
clock = pygame.time.Clock()
running = True
gameover=False
win=False

#HANDLE BIRD ======================
k=0
birdx=1400
birdy=500
birdCollision=False

# DISPLAY CONFIGS =========
width = 1500
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('CHERYL')


#============================================


score = 0
lives=5

new_size = (100, 100)  # Example size, adjust as needed
dogs=[]
birds=[]
# Load and resize the images

n=0
j=0
dogx=100
dogy=600

gravity=1
acceleration=-20
state='run'


marshmellows=[]
trees =  []

# IMAGE PROCESSING ===========================
bg_i = pygame.image.load('cherylforest.jpg')
bgWidth=bg_i.get_width()
bg_xcoord=0

def ProcessSpritesheets(folder,animal,length):
    for i in range(0, 5):
        image = pygame.image.load(f"{folder}/{animal}" + str(i + 1) + ".png")
        resized_image = pygame.transform.scale(image, new_size)
        if animal=='dog':
            dogs.append(resized_image)
        else:
            birds.append(resized_image)


ProcessSpritesheets("spritesheet","dog",5)
ProcessSpritesheets("spritesheet2","bird",5)

def processImage(image_path, size):
    return pygame.transform.scale(pygame.image.load(image_path), size)
images = {
    "black": ("black.jpeg", (1500, 700)),
    "marshmellow": ("marshmellow.png", (75, 50)),
    "heart": ("heart.png", (25, 25)),
    "tree": ("stump.webp", (100, 100))
}

black_i = processImage(*images["black"])
marshmellow_i = processImage(*images["marshmellow"])
heart_i = processImage(*images["heart"])
tree_i = processImage(*images["tree"])

#HANDLE ANIMATIONS=============================================
def displaydog(i,state,x,y):
    if state=='run':
        window.blit(dogs[i],(x,y))
    elif state=='jump':
        window.blit(dogs[4],(x,y))

def displaybird(i,x,y):
    window.blit(birds[i],(x,y))

def handleCollisions(iter,image,allowance,harm):
        global score,lives
        if harm==False:
            if len(iter)>0:
                for i in iter:
                    i.move()
                    window.blit(image,(i.getx(),i.gety()))
                    if abs(i.getx()-dogx)<allowance and abs(i.gety()-dogy)<allowance:
                        score+=1
                        iter.remove(i)
                    if i.getx()<0:
                        iter.remove(i)
        else:
            if len(iter)>0:
                for i in iter:
                    i.move()
                    window.blit(image,(i.getx(),i.gety()))
                    if abs(i.getx()-dogx)<allowance and abs(i.gety()-dogy)<allowance:
                        lives-=1
                        iter.remove(i)
                    if i.getx()<0:
                        iter.remove(i)

def printScore():
    text=f"SCORE: {score}"
    font = pygame.font.Font('pixelsans.ttf', 32)
    text_surface = font.render(text, True, (200,200,200))
    text_rect = text_surface.get_rect()
    text_rect.center = (750,50)
    window.blit(text_surface, text_rect)

def printMessage(msg):
    font = pygame.font.Font('pixelsans.ttf', 32)
    text=f"{msg}"
    text_surface = font.render(text, True, (200,200,200))
    text_rect = text_surface.get_rect()
    text_rect.center = (700,350)
    window.fill((0,0,0))
    window.blit(text_surface, text_rect)

#========================================GAME LOOOOOOP===================================================

while running:
    k+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:    
                print('jump')
                state='jump'


    window.blit(bg_i, (bg_xcoord, 0))
    window.blit(bg_i,(bg_xcoord+bgWidth,0))

    printScore()

    for i in range (0,lives):
        window.blit(heart_i,(50+i*50,50))

    
    if state=='jump':
        if dogy<=600:
            dogy+=acceleration
            acceleration+=gravity
        else:
            dogy=600
            acceleration=-20
            state='run'


    if bg_xcoord<-bgWidth:
        bg_xcoord=0
    else:
        bg_xcoord-=2
    
    if j==10:
        j=0
    else:
        j+=1
    
    if n==30:
        n=0
    else:
        n+=1
    
    if birdx==0:
        birdx=1400
    else:
        birdx-=5
    
    
    r=random.randint(0,100)

    if lives<=0:
        gameover=True
        printMessage('GAMEOVER, TRY AGAIN')
    

    if score==5:
        win=True
    
    if win:
        window.blit(black_i,(1400,0))
        if 1400>0:
            printMessage("[INSERT TEXT HERE]")


    if r == 1:
        mm_instance = Mm(1400, 630)  
        marshmellows.append(mm_instance) 
    elif r == 2:
        if k>60:
            tree=Tree(1400,590,True)
            trees.append(tree)
            k=0
            
    if gameover==False and win==False:
        displaybird(n//10,birdx,birdy)
        handleCollisions(marshmellows,marshmellow_i,50,False)
        handleCollisions(trees,tree_i,50,True)
        displaydog(n//10,state,dogx,dogy)




    if abs(birdx-dogx)<50 and abs(birdy-dogy)<50:
        if birdCollision:
            if state=='jump':
                lives-=1
                birdCollision=False
    
    if state=='run':
        birdCollision=True

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()

