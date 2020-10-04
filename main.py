import pygame

from config import *

while finished is False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    if player1 is True:  # time of player1
        pressed_keys1 = pygame.key.get_pressed()  # array containing key presses

        # moving blocks        

        rx1, moR1 = mov_blocks(rx1, moR1, 0, 640-100, 5, p1)
        rx2, moR2 = mov_blocks(rx2, moR2, 642, 1280-100, 8, p1)
        rx3, moR3 = mov_blocks(rx3, moR3, 1282, 1920-100, 3, p1)
        rx4, moR4 = mov_blocks(rx4, moR4, 0, 960-100, 6, p1)
        rx5, moR5 = mov_blocks(rx5, moR5, 960, 1920-100, 10, p1)
        rx6, moR6 = mov_blocks(rx6, moR6, 0, 640-100, 8, p1)
        rx7, moR7 = mov_blocks(rx7, moR7, 642, 1280-100, 4, p1)
        rx8, moR8 = mov_blocks(rx8, moR8, 1282, 1920-100, 7, p1)
        rx9, moR9 = mov_blocks(rx9, moR9, 0, 960-100, 4, p1)
        rx10, moR10 = mov_blocks(rx10, moR10, 960, 1920-100, 5, p1)
        rx11, moR11 = mov_blocks(rx11, moR11, 0, 640-100, 3, p1)
        rx12, moR12 = mov_blocks(rx12, moR12, 642, 1280-100, 8, p1)
        rx13, moR13 = mov_blocks(rx13, moR13, 1282, 1920-100, 5, p1)

        # time_score

        thisFrameTicks = pygame.time.get_ticks()
        ticksSinceLastFrame = thisFrameTicks - lastFrameTicks
        lastFrameTicks = thisFrameTicks
        scoreIncrementTimer = scoreIncrementTimer + ticksSinceLastFrame

        if scoreIncrementTimer > 100:
            time_score = time_score + 1
            scoreIncrementTimer = 0
        clock = "Clock : " + str(time_score)
        text_time_score = font.render(clock, True, (255, 255, 0))

        # obstacle pass score
        ob_score_p1 = check_score(x1, y1, ob_score_p1, player1)
        text_pass_score = font.render(str(ob_score_p1), True, (255, 255, 0))

        if pressed_keys1[pygame.K_DOWN] == 1:  # Down key pressed
            y1 += 5
            if y1 > 980-50:
                y1 = 980-50

        if pressed_keys1[pygame.K_UP] == 1:  # Up key pressed
            y1 -= 5
            if y1 < 0:
                y1 = 0
        if pressed_keys1[pygame.K_LEFT] == 1:  # Left key pressed
            x1 -= 5
            if x1 < 0:
                x1 = 0
        if pressed_keys1[pygame.K_RIGHT] == 1:  # Right key pressed
            x1 += 5
            if x1 > 1920-50:
                x1 = 1920-50
        if time_score > 0:  # calculate final score
            final_score = 10000//time_score + ob_score_p1
        else:
            final_score = 0
        # checking collisions with static obstales
        player1_collide = checkCollision(x1, y1, rx1, 130)
        player1_collide = player1_collide or checkCollision(x1, y1, rx2, 130)
        player1_collide = player1_collide or checkCollision(x1, y1, rx3, 130)
        player1_collide = player1_collide or checkCollision(x1, y1, rx4, 290)
        player1_collide = player1_collide or checkCollision(x1, y1, rx5, 290)
        player1_collide = player1_collide or checkCollision(x1, y1, rx6, 450)
        player1_collide = player1_collide or checkCollision(x1, y1, rx7, 450)
        player1_collide = player1_collide or checkCollision(x1, y1, rx8, 450)
        player1_collide = player1_collide or checkCollision(x1, y1, rx9, 610)
        player1_collide = player1_collide or checkCollision(x1, y1, rx10, 610)
        player1_collide = player1_collide or checkCollision(x1, y1, rx11, 770)
        player1_collide = player1_collide or checkCollision(x1, y1, rx12, 770)
        player1_collide = player1_collide or checkCollision(x1, y1, rx13, 770)
        # checking collisions with moving obstacles
        player1_collide = player1_collide or checkCollision(x1, y1, 0, 210)
        player1_collide = player1_collide or checkCollision(x1, y1, 910, 210)
        player1_collide = player1_collide or checkCollision(x1, y1, 1820, 210)
        player1_collide = player1_collide or checkCollision(x1, y1, 455, 370)
        player1_collide = player1_collide or checkCollision(x1, y1, 1365, 370)
        player1_collide = player1_collide or checkCollision(x1, y1, 0, 530)
        player1_collide = player1_collide or checkCollision(x1, y1, 910, 530)
        player1_collide = player1_collide or checkCollision(x1, y1, 1820, 530)
        player1_collide = player1_collide or checkCollision(x1, y1, 455, 690)
        player1_collide = player1_collide or checkCollision(x1, y1, 1365, 690)

        if player1_collide is True:  # on player 1 collision
            x1 = 0
            y1 = 0
            player1_died = True
            player1 = False
            player2 = True
            player1_reached = False
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = False
            flag5 = False
            flag6 = False
            flag7 = False
            flag8 = False
            flag9 = False
            final_player1 = ob_score_p1 + (300 - time_score)*5
            ob_score_p1 = 0
            final_score_p1 = 10000//time_score + ob_score_p1
            time_score = 0
            temp = 1

        if y1 >= 880:  #on player1 completion
            x1 = 0
            y1 = 0
            player1 = False
            player2 = True
            player1_reached = True
            player1_died = False
            flag1 = False
            flag2 = False
            flag3 = False
            flag4 = False
            flag5 = False
            flag6 = False
            flag7 = False
            flag8 = False
            flag9 = False
            final_score_p1 = 10000//time_score + ob_score_p1
            time_score = 0
            scoreIncrementTimer = 0
            lastFrameTicks = pygame.time.get_ticks()
            ob_score_p1 = 0
            temp = 1

    elif player2 is True:  # player2 active

        pressed_keys2 = pygame.key.get_pressed()  # taking key action in arrays

        if pressed_keys2[pygame.K_DOWN] == 1:  # Down key pressed
            y2 += 5
            if y2 > 980-50:
                y2 = 980-50

        if pressed_keys2[pygame.K_UP] == 1:  # Up key pressed
            y2 -= 5
            if y2 < 0:
                y2 = 0
        if pressed_keys2[pygame.K_LEFT] == 1:  # Left key pressed
            x2 -= 5
            if x2 < 0:
                x2 = 0
        if pressed_keys2[pygame.K_RIGHT] == 1:  # Right key pressed
            x2 += 5
            if x2 > 1920-50:
                x2 = 1920-50
        # moving blocks
        rx1, moR1 = mov_blocks(rx1, moR1, 0, 640-100, 5, p2)
        rx2, moR2 = mov_blocks(rx2, moR2, 642, 1280-100, 8, p2)
        rx3, moR3 = mov_blocks(rx3, moR3, 1282, 1920-100, 3, p2)
        rx4, moR4 = mov_blocks(rx4, moR4, 0, 960-100, 6, p2)
        rx5, moR5 = mov_blocks(rx5, moR5, 960, 1920-100, 10, p2)
        rx6, moR6 = mov_blocks(rx6, moR6, 0, 640-100, 8, p2)
        rx7, moR7 = mov_blocks(rx7, moR7, 642, 1280-100, 4, p2)
        rx8, moR8 = mov_blocks(rx8, moR8, 1282, 1920-100, 7, p2)
        rx9, moR9 = mov_blocks(rx9, moR9, 0, 960-100, 4, p2)
        rx10, moR10 = mov_blocks(rx10, moR10, 960, 1920-100, 5, p2)
        rx11, moR11 = mov_blocks(rx11, moR11, 0, 640-100, 3, p2)
        rx12, moR12 = mov_blocks(rx12, moR12, 642, 1280-100, 8, p2)
        rx13, moR13 = mov_blocks(rx13, moR13, 1282, 1920-100, 5, p2)

        # time_score

        thisFrameTicks = pygame.time.get_ticks()
        ticksSinceLastFrame = thisFrameTicks - lastFrameTicks
        lastFrameTicks = thisFrameTicks
        scoreIncrementTimer = scoreIncrementTimer + ticksSinceLastFrame

        if scoreIncrementTimer > 100:
            time_score = time_score + 1
            scoreIncrementTimer = 0
        clock = "Clock : " + str(time_score)
        text_time_score = font.render(clock, True, (255, 255, 0))

        # pass score
        ob_score_p2 = check_score(x2, y2, ob_score_p2, player1)
        text_pass_score = font.render(str(ob_score_p2), True, (255, 255, 0))
        if time_score > 0:
            final_score = 10000//time_score + ob_score_p2
        else:
            time_score = 0
        # checking collisions
        player2_collide = checkCollision(x2, y2, rx1, 130)
        player2_collide = player2_collide or checkCollision(x2, y2, rx2, 130)
        player2_collide = player2_collide or checkCollision(x2, y2, rx3, 130)
        player2_collide = player2_collide or checkCollision(x2, y2, rx4, 290)
        player2_collide = player2_collide or checkCollision(x2, y2, rx5, 290)
        player2_collide = player2_collide or checkCollision(x2, y2, rx6, 450)
        player2_collide = player2_collide or checkCollision(x2, y2, rx7, 450)
        player2_collide = player2_collide or checkCollision(x2, y2, rx8, 450)
        player2_collide = player2_collide or checkCollision(x2, y2, rx9, 610)
        player2_collide = player2_collide or checkCollision(x2, y2, rx10, 610)
        player2_collide = player2_collide or checkCollision(x2, y2, rx11, 770)
        player2_collide = player2_collide or checkCollision(x2, y2, rx12, 770)
        player2_collide = player2_collide or checkCollision(x2, y2, rx13, 770)

        player2_collide = player2_collide or checkCollision(x2, y2, 0, 210)
        player2_collide = player2_collide or checkCollision(x2, y2, 910, 210)
        player2_collide = player2_collide or checkCollision(x2, y2, 1820, 210)
        player2_collide = player2_collide or checkCollision(x2, y2, 455, 370)
        player2_collide = player2_collide or checkCollision(x2, y2, 1365, 370)
        player2_collide = player2_collide or checkCollision(x2, y2, 0, 530)
        player2_collide = player2_collide or checkCollision(x2, y2, 910, 530)
        player2_collide = player2_collide or checkCollision(x2, y2, 1820, 530)
        player2_collide = player2_collide or checkCollision(x2, y2, 455, 690)
        player2_collide = player2_collide or checkCollision(x2, y2, 1365, 690)

        if player2_collide is True:  # player2 collides
            x2 = 1920-50
            y2 = 930
            player1 = False
            player2 = False
            player2_died = True
            player2_reached = False
            if time_score > 0:
                final_score_p2 = 10000//time_score + ob_score_p2
            ob_score_p2 = 0

        if y2 <= 50:  # player2 completes
            x2 = 1920-50
            y2 = 930
            player1 = False
            player2 = False
            player2_reached = True
            player2_died = False
            if time_score > 0:
                final_score_p2 = 10000//time_score + ob_score_p2
            ob_score_p2 = 0

    if player1 is False and player2 is False:
        if player1_died is True:
            if player2_died is True:  # no player won  no change
                msg = font.render("Draw", True, (255, 255, 0))
                a = 1
            else:  # player2 won
                msg = font.render("Player 2 won", True, (255, 255, 0))
                p2 = p2 + 3
                a = 1

        elif player2_died is True:
            if player1_died is True:  # no player won  no change
                a = 1
            else:  # player1 won
                msg = font.render("Player 1 won", True, (255, 255, 0))
                p1 = p1 + 3
                a = 1
        else:
            if final_score_p1 > final_score_p2:
                msg = font.render("Player 1 won", True, (255, 255, 0))
                p1 = p1 + 3
                a = 1
            elif final_score_p2 > final_score_p1:
                msg = font.render("Player 2 won", True, (255, 255, 0))
                p2 = p2 + 3
                a = 1
            else:  # no changescore
                a = 1
                msg = font.render("Draw", True, (255, 255, 0))

        IncrementTimer = 0
        lastFrameTicks = pygame.time.get_ticks()
        time_score = 0

        player1 = True
        player2 = False

        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        flag5 = False
        flag6 = False
        flag7 = False
        flag8 = False
        flag9 = False

    screen.blit(bg, (0, 0))  # bg image blitted

    screen.blit(par1, (0, 100))  # partitions blitted
    screen.blit(par1, (0, 260))
    screen.blit(par1, (0, 420))
    screen.blit(par1, (0, 580))
    screen.blit(par1, (0, 740))

    screen.blit(planet1, (0, 210))  # static obstacles blitted
    screen.blit(planet1, (910, 210))
    screen.blit(planet1, (1820, 210))
    screen.blit(planet1, (455, 370))
    screen.blit(planet1, (1365, 370))
    screen.blit(planet1, (0, 530))
    screen.blit(planet1, (910, 530))
    screen.blit(planet1, (1820, 530))
    screen.blit(planet1, (455, 690))
    screen.blit(planet1, (1365, 690))

    screen.blit(ufo1, (rx1, 130))  # moving obstacles blitted
    screen.blit(ufo1, (rx2, 130))
    screen.blit(ufo1, (rx3, 130))
    screen.blit(ufo1, (rx4, 290))
    screen.blit(ufo1, (rx5, 290))
    screen.blit(ufo1, (rx6, 450))
    screen.blit(ufo1, (rx7, 450))
    screen.blit(ufo1, (rx8, 450))
    screen.blit(ufo1, (rx9, 610))
    screen.blit(ufo1, (rx10, 610))
    screen.blit(ufo1, (rx11, 770))
    screen.blit(ufo1, (rx12, 770))
    screen.blit(ufo1, (rx13, 770))

    screen.blit(player1Image, (x1, y1))  # player1 blitted
    screen.blit(player2Image, (x2, y2))  # player2 blitted

    screen.blit(text_time_score, (50, 50))  # score blitted
    screen.blit(text_pass_score, (500, 50))

    frame.tick(60)  # clock speed slowed
    if a == 1:
        screen.blit(msg, (800, 500))  # result declared
        x1 = 0
        x2 = 1920 - 50
        y1 = 0
        y2 = 980 - 50
        pygame.display.flip()
        pygame.time.delay(1000)  # delay to give the user time

        a = 0
    else:
        scr = "Score :" + " " + str(final_score)
        pr = font.render(scr, True, (255, 255, 0))
        screen.blit(pr, (1600, 50))
        pygame.display.flip()  # flipped
        if temp == 1:
            pygame.time.delay(1000)
            temp = 0
