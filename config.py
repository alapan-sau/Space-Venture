import pygame

flag1 = False  # flag values set
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False
flag7 = False
flag8 = False
flag9 = False


def checkCollision(x, y, l, t):  # collison checking
    global screen
    collisionState = False

    if y >= t-50 and y <= t+90:  # y co-ordinates

        if x+50 >= l and x <= l+90:  # x co -ordinates
            collisionState = True
    return collisionState


def mov_blocks(rx, moR, l, r, s, add):
    s += add  # speed changed with level
    if rx >= r:
        moR = False
    elif rx <= l:
        moR = True
    if moR is True:
        rx += s
    else:
        rx -= s
    return rx, moR

pygame.init()
screen = pygame.display.set_mode((1920, 980))

player1Image = pygame.image.load("player1.png")  # player 1
player1Image = pygame.transform.scale(player1Image, (50, 50))
player1Image = player1Image.convert_alpha()

player2Image = pygame.image.load("player2.png")  # player 2
player2Image = pygame.transform.scale(player2Image, (50, 50))
player2Image = player2Image.convert_alpha()

bg = pygame.image.load("bg.jpg")  # bg image
bg = pygame.transform.scale(bg, (1920, 1080))
bg = bg.convert_alpha()

planet1 = pygame.image.load("saturn.png")  # obstacles
planet1 = pygame.transform.scale(planet1, (90, 90))
planet1 = planet1.convert_alpha()

planet2 = pygame.image.load("saturn.png")
planet2 = pygame.transform.scale(planet2, (90, 90))
planet2 = planet2.convert_alpha()

planet3 = pygame.image.load("saturn.png")
planet3 = pygame.transform.scale(planet3, (90, 90))
planet3 = planet3.convert_alpha()

planet4 = pygame.image.load("saturn.png")
planet4 = pygame.transform.scale(planet4, (90, 90))
planet4 = planet4.convert_alpha()

planet5 = pygame.image.load("saturn.png")
planet5 = pygame.transform.scale(planet5, (90, 90))
planet5 = planet5.convert_alpha()

planet6 = pygame.image.load("saturn.png")
planet6 = pygame.transform.scale(planet6, (90, 90))
planet6 = planet6.convert_alpha()

planet7 = pygame.image.load("saturn.png")
planet7 = pygame.transform.scale(planet7, (90, 90))
planet7 = planet7.convert_alpha()

planet8 = pygame.image.load("saturn.png")
planet8 = pygame.transform.scale(planet8, (90, 90))
planet8 = planet8.convert_alpha()

planet9 = pygame.image.load("saturn.png")
planet9 = pygame.transform.scale(planet9, (90, 90))
planet9 = planet9.convert_alpha()

planet10 = pygame.image.load("saturn.png")
planet10 = pygame.transform.scale(planet10, (90, 90))
planet10 = planet10.convert_alpha()

ufo1 = pygame.image.load("ufo.png")  # moving obstacles
ufo1 = pygame.transform.scale(ufo1, (90, 90))
ufo1 = ufo1.convert_alpha()

ufo2 = pygame.image.load("ufo.png")
ufo2 = pygame.transform.scale(ufo2, (90, 90))
ufo2 = ufo2.convert_alpha()

ufo3 = pygame.image.load("ufo.png")
ufo3 = pygame.transform.scale(ufo3, (90, 90))
ufo3 = ufo3.convert_alpha()

ufo4 = pygame.image.load("ufo.png")
ufo4 = pygame.transform.scale(ufo4, (90, 90))
ufo4 = ufo4.convert_alpha()

ufo5 = pygame.image.load("ufo.png")
ufo5 = pygame.transform.scale(ufo5, (90, 90))
ufo5 = ufo5.convert_alpha()

ufo6 = pygame.image.load("ufo.png")
ufo6 = pygame.transform.scale(ufo6, (90, 90))
ufo6 = ufo6.convert_alpha()

ufo7 = pygame.image.load("ufo.png")
ufo7 = pygame.transform.scale(ufo7, (90, 90))
ufo7 = ufo7.convert_alpha()

ufo8 = pygame.image.load("ufo.png")
ufo8 = pygame.transform.scale(ufo8, (90, 90))
ufo8 = ufo8.convert_alpha()

ufo9 = pygame.image.load("ufo.png")
ufo9 = pygame.transform.scale(ufo9, (90, 90))
ufo9 = ufo9.convert_alpha()

ufo10 = pygame.image.load("ufo.png")
ufo10 = pygame.transform.scale(ufo10, (90, 90))
ufo10 = ufo10.convert_alpha()

ufo11 = pygame.image.load("ufo.png")
ufo11 = pygame.transform.scale(ufo11, (90, 90))
ufo11 = ufo11.convert_alpha()

ufo12 = pygame.image.load("ufo.png")
ufo12 = pygame.transform.scale(ufo12, (90, 90))
ufo12 = ufo12.convert_alpha()

ufo13 = pygame.image.load("ufo.png")
ufo13 = pygame.transform.scale(ufo13, (90, 90))
ufo13 = ufo13.convert_alpha()

par1 = pygame.image.load("par.jpg")  # partitions
par1 = pygame.transform.scale(par1, (1920, 120))
par1 = par1.convert_alpha()

par2 = pygame.image.load("par.jpg")
par2 = pygame.transform.scale(par2, (1920, 160))
par2 = par2.convert_alpha()

x1 = 0  # position of player 1
y1 = 0
x2 = 1920-50  # position of player 2
y2 = 980-50

p1 = 0
p2 = 0

player1 = True  # active player
player2 = False


def check_score(x, y, ob_score, p):

    global flag1
    global flag2
    global flag3
    global flag4
    global flag5
    global flag6
    global flag7
    global flag8
    global flag9

    if p is True:  # player 1

        if y > 220 and flag1 is False:
            if x >= 0 and x <= 640:
                ob_score += 5*10
            elif x <= 1280:
                ob_score += 8*10
            else:
                ob_score += 3*10
            flag1 = True

        elif y > 260 and flag6 is False:
            ob_score += 20
            flag6 = True

        elif y > 380 and flag2 is False:
            if x >= 0 and x <= 960:
                ob_score += 6*10
            else:
                ob_score += 10*10
            flag2 = True

        elif y > 420 and flag7 is False:
            ob_score += 20
            flag7 = True

        elif y > 540 and flag3 is False:
            if x >= 0 and x <= 640:
                ob_score += 8*10
            elif x <= 1280:
                ob_score += 4*10
            else:
                ob_score += 7*10
            flag3 = True

        elif y > 580 and flag8 is False:
            ob_score += 20
            flag8 = True

        elif y > 700 and flag4 is False:
            if x >= 0 and x <= 960:
                ob_score += 4*10
            else:
                ob_score += 5*10
            flag4 = True

        elif y > 740 and flag9 is False:
            ob_score += 20
            flag9 = True

        elif y > 860 and flag5 is False:
            if x >= 0 and x <= 640:
                ob_score += 3*10
            elif x <= 1280:
                ob_score += 8*10
            else:
                ob_score += 5*10
            flag5 = True
        return ob_score

    else:  # player 2

        if y < 100-30 and flag1 is False:
            if x >= 0 and x <= 640:
                ob_score += 5*10
            elif x <= 1280:
                ob_score += 8*10
            else:
                ob_score += 3*10
            flag1 = True

        elif y < 320-30 and flag6 is False:
            ob_score += 20
            flag6 = True

        elif y < 260-30 and flag2 is False:
            if x >= 0 and x <= 960:
                ob_score += 6*10
            else:
                ob_score += 10*10
            flag2 = True

        elif y < 380-30 and flag7 is False:
            ob_score += 20
            flag7 = True

        elif y < 420-30 and flag3 is False:
            if x >= 0 and x <= 640:
                ob_score += 8*10
            elif x <= 1280:
                ob_score += 4*10
            else:
                ob_score += 7*10
            flag3 = True

        elif y < 540-30 and flag8 is False:
            ob_score += 20
            flag8 = True

        elif y < 580-30 and flag4 is False:
            if x >= 0 and x <= 960:
                ob_score += 4*10
            else:
                ob_score += 5*10
            flag4 = True

        elif y < 700-30 and flag9 is False:
            ob_score += 20
            flag9 = True

        elif y < 740-30 and flag5 is False:
            if x >= 0 and x <= 640:
                ob_score += 3*10
            elif x <= 1280:
                ob_score += 8*10
            else:
                ob_score += 5*10
            flag5 = True
        return ob_score
rx1 = 0  # moving block positions
rx2 = 640
rx3 = 1280
rx4 = 0
rx5 = 960
rx6 = 0
rx7 = 640
rx8 = 1280
rx9 = 0
rx10 = 960
rx11 = 0
rx12 = 640
rx13 = 1280

a = 0

moR1 = True
moR2 = True
moR3 = True
moR4 = True
moR5 = True
moR6 = True
moR7 = True
moR8 = True
moR9 = True
moR10 = True
moR11 = True
moR12 = True
moR13 = True

frame = pygame.time.Clock()

finished = False

scoreIncrementTimer = 0
lastFrameTicks = pygame.time.get_ticks()
time_score = 0

font = pygame.font.SysFont("comicsans", 60)

ob_score_p1 = 0
ob_score_p2 = 0

temp = 0
