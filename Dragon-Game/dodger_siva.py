import pygame,random,sys,time
from pygame.locals import *

WIDTH=500
HEIGHT=500
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0,)
FPS = 60
BADDIE_MIN_SIZE=10
BADDIE_MAX_SIZE=40
BADDIE_MIN_SPEED=1
BADDIE_MAX_SPEED=8
ADDNEWBADDIE=6
PLAYERSPEED=5

def terminate():
    pygame.quit()
    sys.exit()
    
def PlayerKey():
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE: 
                    terminate()
                return
        
def drawText(text,font,surface,x,y):
    text=font.render(text,1,RED)
    textrect=text.get_rect()
    textrect.center=(x, y)
    surface.blit(text, textrect)

def playerBaddie(playerRect,baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

pygame.init()
mainClock=pygame.time.Clock()
windowSurface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Dodger')

gameOverSound=pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

playerImage=pygame.image.load('player.png')
playerRect=playerImage.get_rect()
baddieImage=pygame.image.load('baddie.png')

font=pygame.font.SysFont(None, 48)

windowSurface.fill(WHITE)
drawText('Dodger', font, windowSurface,windowSurface.get_rect().centerx,windowSurface.get_rect().centery

)
drawText('Press a key to start.', font, windowSurface,windowSurface.get_rect().centerx-30, windowSurface.get_rect().centery+50
)
pygame.display.update()
PlayerKey()

topScore=0
while True:
    baddies=[]
    score=0
    playerRect.topleft=(WIDTH/2,HEIGHT-50)
    moveLeft=moveRight=moveUp=moveDown=False
    reverseCheat=slowCheat=False
    baddieAddCounter=0
    pygame.mixer.music.play(-1,0.0)

    while True:  
        score += 1 

        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()

            if event.type==KEYDOWN:
                if event.key==K_z:
                    reverseCheat = True
                if event.key==K_x:
                    slowCheat=True
                if event.key==K_LEFT or event.key==K_a:
                    moveRight=False
                    moveLeft=True
                if event.key==K_RIGHT or event.key==K_d:
                    moveLeft=False
                    moveRight=True
                if event.key==K_UP or event.key==K_w:
                    moveDown=False
                    moveUp=True
                if event.key==K_DOWN or event.key==K_s:
                    moveUp=False
                    moveDown=True

            if event.type==KEYUP:
                if event.key==K_z:
                    reverseCheat=False
                    score=0
                if event.key==K_x:
                    slowCheat=False
                    score=0
                if event.key== K_ESCAPE:
                        terminate()
                if event.key==K_LEFT or event.key==K_a:
                    moveLeft=False
                if event.key==K_RIGHT or event.key==K_d:
                    moveRight=False
                if event.key==K_UP or event.key==K_w:
                    moveUp=False
                if event.key==K_DOWN or event.key==K_s:
                    moveDown=False

            if event.type==MOUSEMOTION:
                playerRect.centerx=event.pos[0]
                playerRect.centery = event.pos[1]
        
        if not reverseCheat or not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter==ADDNEWBADDIE:
            baddieAddCounter=0
            baddieSize=random.randint(BADDIE_MIN_SIZE, BADDIE_MAX_SIZE)
            newBaddie={'rect':pygame.Rect(random.randint(0,WIDTH-baddieSize),0-baddieSize,baddieSize,baddieSize),
                        'speed':random.randint(BADDIE_MIN_SPEED,BADDIE_MAX_SPEED),
                        'surface':pygame.transform.scale(baddieImage,(baddieSize,baddieSize)),
                        }

            baddies.append(newBaddie)

    
        if moveLeft and playerRect.left >0:
            playerRect.move_ip(-1*PLAYERSPEED,0)
        if moveRight and playerRect.right <WIDTH:
            playerRect.move_ip(PLAYERSPEED,0)
        if moveUp and playerRect.top >0:
            playerRect.move_ip(0,-1*PLAYERSPEED)
        if moveDown and playerRect.bottom < HEIGHT:
            playerRect.move_ip(0,PLAYERSPEED)
            
        for b in baddies:
            if not reverseCheat or not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        for b in baddies[:]:
            if b['rect'].top > HEIGHT:
                baddies.remove(b)

        windowSurface.fill(WHITE)

        drawText('Score: %s'%(score),font,windowSurface,100,20)
        drawText('Top Score: %s'%(topScore),font,windowSurface,100,60)

        windowSurface.blit(playerImage,playerRect)

        for b in baddies:
            windowSurface.blit(b['surface'],b['rect'])

        pygame.display.update()

        if playerBaddie(playerRect,baddies):
            if score>topScore:
                topScore=score
            break

        mainClock.tick(FPS)

    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER',font,windowSurface,windowSurface.get_rect().centerx,windowSurface.get_rect().centery)
    drawText('Press a key to play again.',font,windowSurface,windowSurface.get_rect().centerx-30,windowSurface.get_rect().centery+50)
    pygame.display.update()
    PlayerKey()

    gameOverSound.stop()
