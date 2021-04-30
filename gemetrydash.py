import pygame
from random import randint

pygame.init()

walkRight = [
    pygame.image.load('img/pygame_right_1.png'),
    pygame.image.load('img/pygame_right_2.png'),
    pygame.image.load('img/pygame_right_3.png'),
    pygame.image.load('img/pygame_right_4.png'),
    pygame.image.load('img/pygame_right_5.png'),
    pygame.image.load('img/pygame_right_6.png')
]


font = pygame.font.Font(None, 25)
win = pygame.display.set_mode([900, 300])
bg = [170, 170, 255]
l = pygame.image.load('img/klipartz.com.png')
win.blit
pygame.display.set_caption("Geomtry dash")

back = pygame.image.load('img/moscow-3550477_1280_0.jpg')

#pygame.display.flip()


clock = pygame.time.Clock()

animCount = 0

y_let = 250
x_let = 900

x_floor = 0
y_floor = 280
width_floor = 1000
height_floor = 20

x_player = 50
y_player = 250
width_player = 60
height_player = 71

restart = False

isJump = False
jumpCount = 10


speed = 10


class let():
    def __init__(self, x_let, y_let):
        self.x_let = x_let
        self.y_let = y_let
        self.vel = 10

    def dr(self, win):
        #pygame.draw.rect(win, (255, 0, 0), (self.x_let, self.y_let, 40, 40))
        win.blit(l, (self.x_let, self.y_let, 40, 40))


def Draw():

    global animCount

    win.blit(back, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0
    
    pygame.draw.rect(win, (255, 255, 255), (790, 5, 100, 30))
    text = font.render("Score: "+str(sum),True, (0, 0, 0))
    win.blit(text, [792,12])

    pygame.draw.rect(win, (90, 90, 90), (x_floor, y_floor, width_floor, height_floor))
    #pygame.draw.rect(win, color_player, (x_player, y_player, width_player, height_player))
    win.blit(walkRight[animCount //  10 ], (x_player, y_player - 30, width_player, height_player))
    animCount += 1

    for lets in mas_let:
        lets.dr(win)
    
    pygame.display.update()


def app_mas(sum):

    if len(mas_let) <= 2 and sum < 19:
        mas_let.append(let(randint(1000, 1233), 250))
        mas_let.append(let(randint(1382, 1617), 250))
        mas_let.append(let(randint(1765, 2000), 250))
        
    if len(mas_let) <= 1 and sum >= 15 and sum < 30:
        mas_let.append(let(randint(1000, 1334), 250))
        mas_let.append(let(randint(1665, 2000), 250))
    
    if len(mas_let) <= 1 and sum >= 30:
        mas_let.append(let(randint(1000, 1500), 250))

sum = 0

Jumping = True

mas_let = []
run = True

while run:
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    for lets in mas_let:
        if ((lets.x_let <= x_player + 45 and x_player <= lets.x_let + 40) and lets.y_let == y_player) or ((x_player >= lets.x_let + 40 and x_player <=lets.x_let) and lets.y_let == y_player):
            Jumping = False
            x_player -= speed
            if(x_player <= -60):
                restart = True
        elif restart == False:
            lets.x_let -= speed

        if lets.x_let <= -40:
            mas_let.pop(mas_let.index(lets))
            sum += 1 

    app_mas(sum)

    if sum > 10 and sum < 32:
        speed += 0.01
    
    if sum >= 200:
        speed += 0.001

    mous = pygame.mouse.get_pressed()

    if not(isJump):
        if Jumping and keys[pygame.K_SPACE] or mous[0] and Jumping:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y_player += (jumpCount ** 2) / 5
            else:
                y_player -= (jumpCount ** 2) / 5
            jumpCount -= 1

        else:
            
            isJump = False
            jumpCount = 10


    Draw()



pygame.quit()
