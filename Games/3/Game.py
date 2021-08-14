# This Game is outside
import os
try:
    import pygame
except:
    try:
        os.system("pip install pygame")
    except:
        print("You dont have pip for install pygame. please install pip.")
        quit()
import sqlite3
import time

def charecter():
    conn = sqlite3.connect('../../files/Game_info.db') #connect to database
    cur = conn.cursor()
    cur.execute("SELECT * FROM info_setting WHERE rowid=1") #for sql codes : SELECT user 's level 
    setting = cur.fetchall()
    ret_s = [setting[0][0],setting[0][1]]
    if setting[0][2] == 1:
        ret_s.append("../../icons/boy_anim_")
    elif setting[0][2] == 2:
        ret_s.append("../../icons/boy2_anim_")
    elif setting[0][2] == 3:
        ret_s.append("../../icons/boy3_anim_")
    return ret_s

pygame.init() # init
gamedisplay = pygame.display.set_mode((263,450)) # width and height
pygame.display.set_caption('Code Jungle') # Title

#for icon
icon = pygame.image.load('../../icons/programming.png')
pygame.display.set_icon(icon)

#maps & character
#maps
game_map = pygame.image.load('map.png') # map 1

atorpot_1 = pygame.image.load(charecter()[2] + '1.png').convert_alpha()
atorpot_2 = pygame.image.load(charecter()[2] + '2.png').convert_alpha() # stand
atorpot_3 = pygame.image.load(charecter()[2] + '3.png').convert_alpha()

#clock
clock = pygame.time.Clock()

#colors:
white = (255,255,255)

#sound
pygame.mixer.init()
foot = pygame.mixer.Sound("../../Sounds/inside.ogg")
foot.set_volume(charecter()[1] / 100)

#musics
#pygame.mixer.music.load("../../Sounds/jungle.wav")
#pygame.mixer.music.set_volume(charecter()[0] / 10000)
#pygame.mixer.music.play(-1)

#images
lock_1 = pygame.image.load('map3.png')
lock_2 = pygame.image.load('map3.png')

x_c = 80
y_c = 155
map_ar = ([100,1,0],
          [0,0,0],
          [1,1,1],
          [1,0,1],
          [1,0,1],
          [1,0,0])
player_ar = "[2][1]"
#About may_ar
#This is array of map for functions ( example : right or left )
#0 = wall
#1 = way
#100 = end

#vars:
out1_answer = 52
out2_answer = 36


def left():
    time.sleep(2)
    #check map:
    global player_ar
    global atorpot_1
    global atorpot_2
    global atorpot_3
    global x_c
    global y_c
    row = int(player_ar[1])
    if int(player_ar[4]) == 0:
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()
    column = int(player_ar[4]) - 1
    if map_ar[row][column] == 0:   
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()
    atorpot_1 = pygame.transform.rotate(atorpot_1, 90)
    atorpot_2 = pygame.transform.rotate(atorpot_2, 90)
    atorpot_3 = pygame.transform.rotate(atorpot_3, 90)
    
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()
    
    player_ar = "[" + str(row) + "]" + "[" + str(column) + "]"
    time.sleep(0.5)

    
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_1,(x_c - 35,y_c))
    pygame.display.update()
    x_c = x_c - 35
    pygame.mixer.Sound.play(foot)
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_3,(x_c - 35,y_c))
    pygame.display.update()
    x_c = x_c - 35
    
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()

    #reset
    atorpot_1 = pygame.transform.rotate(atorpot_1, 270)
    atorpot_2 = pygame.transform.rotate(atorpot_2, 270)
    atorpot_3 = pygame.transform.rotate(atorpot_3, 270)

    #time.sleep(0.25)
    #gamedisplay.blit(game_map,(0,0))
    #gamedisplay.blit(atorpot_2,(x_c,y_c))
    #pygame.display.update()

    if player_ar == "[5][0]":
       out_1 = pygame.image.load("out1.png")
       gamedisplay.blit(out_1,(10,140))
       pygame.display.update()
       time.sleep(3)
    if player_ar == "[4][2]":
       out_2 = pygame.image.load("out2.png")
       gamedisplay.blit(out_2,(10,140))
       pygame.display.update()
       time.sleep(3)


#front
def front():
    time.sleep(2)
    #check map:
    global player_ar
    global atorpot_1
    global atorpot_2
    global atorpot_3
    global x_c
    global y_c
    column = int(player_ar[4])
    if int(player_ar[1]) == 0:
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()
    row = int(player_ar[1]) - 1
    
    if map_ar[row][column] == 0:   
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()
       
    player_ar = "[" + str(row) + "]" + "[" + str(column) + "]"
    
    time.sleep(0.5)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_1,(x_c,y_c - 35))
    pygame.display.update()
    y_c = y_c - 35
    pygame.mixer.Sound.play(foot)
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_3,(x_c,y_c - 35))
    pygame.display.update()
    y_c = y_c - 35
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()

    if player_ar == "[5][0]":
       out_1 = pygame.image.load("out1.png")
       gamedisplay.blit(out_1,(10,140))
       pygame.display.update()
       time.sleep(3)
    if player_ar == "[4][2]":
       out_2 = pygame.image.load("out2.png")
       gamedisplay.blit(out_2,(10,140))
       pygame.display.update()
       time.sleep(3)












def behind():
    time.sleep(2)
    #check map:
    global player_ar
    global atorpot_1
    global atorpot_2
    global atorpot_3
    global x_c
    global y_c
    column = int(player_ar[4])
    if int(player_ar[1]) == 5:
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()
    row = int(player_ar[1]) + 1
    
    if map_ar[row][column] == 0:   
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()

    atorpot_1 = pygame.transform.rotate(atorpot_1, 180)
    atorpot_2 = pygame.transform.rotate(atorpot_2, 180)
    atorpot_3 = pygame.transform.rotate(atorpot_3, 180)
       
    player_ar = "[" + str(row) + "]" + "[" + str(column) + "]"
    
    time.sleep(0.5)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_1,(x_c,y_c + 35))
    pygame.display.update()
    y_c = y_c + 35
    pygame.mixer.Sound.play(foot)
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_3,(x_c,y_c + 35))
    pygame.display.update()
    y_c = y_c + 35
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()


    #reset
    atorpot_1 = pygame.transform.rotate(atorpot_1, 180)
    atorpot_2 = pygame.transform.rotate(atorpot_2, 180)
    atorpot_3 = pygame.transform.rotate(atorpot_3, 180)

    #time.sleep(0.25)
    #gamedisplay.blit(game_map,(0,0))
    #gamedisplay.blit(atorpot_2,(x_c,y_c))
    #pygame.display.update()

    if player_ar == "[5][0]":
       out_1 = pygame.image.load("out1.png")
       gamedisplay.blit(out_1,(10,140))
       pygame.display.update()
       time.sleep(3)
    if player_ar == "[4][2]":
       out_2 = pygame.image.load("out2.png")
       gamedisplay.blit(out_2,(10,140))
       pygame.display.update()
       time.sleep(3)



    
def main():
    #main
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gamedisplay.fill(white)
    gamedisplay.blit(game_map,(0,0)) # create map
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    
        
    #update 
    pygame.display.update()
    #tick clock
    clock.tick(90)
    time.sleep(2)

















def right():
    time.sleep(2)
    #check map:
    global player_ar
    global atorpot_1
    global atorpot_2
    global atorpot_3
    global x_c
    global y_c
    row = int(player_ar[1])
    if int(player_ar[4]) == 2:
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()
    column = int(player_ar[4]) + 1
    if map_ar[row][column] == 0:   
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()
    atorpot_1 = pygame.transform.rotate(atorpot_1, 270)
    atorpot_2 = pygame.transform.rotate(atorpot_2, 270)
    atorpot_3 = pygame.transform.rotate(atorpot_3, 270)
    
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()
    
    player_ar = "[" + str(row) + "]" + "[" + str(column) + "]"
    time.sleep(0.5)

    
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_1,(x_c + 37,y_c))
    pygame.display.update()
    x_c = x_c + 37
    pygame.mixer.Sound.play(foot)
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_3,(x_c + 37,y_c))
    pygame.display.update()
    x_c = x_c + 37
    
    
    time.sleep(0.25)
    gamedisplay.blit(game_map,(0,0))
    gamedisplay.blit(atorpot_2,(x_c,y_c))
    pygame.display.update()

    #reset
    atorpot_1 = pygame.transform.rotate(atorpot_1, 90)
    atorpot_2 = pygame.transform.rotate(atorpot_2, 90)
    atorpot_3 = pygame.transform.rotate(atorpot_3, 90)

    #time.sleep(0.25)
    #gamedisplay.blit(game_map,(0,0))
    #gamedisplay.blit(atorpot_2,(x_c,y_c))
    #pygame.display.update()
    if player_ar == "[5][0]":
       out_1 = pygame.image.load("out1.png")
       gamedisplay.blit(out_1,(10,140))
       pygame.display.update()
       time.sleep(3)

    if player_ar == "[4][2]":
       out_2 = pygame.image.load("out2.png")
       gamedisplay.blit(out_2,(10,140))
       pygame.display.update()
       time.sleep(3)















def check():
    global player_ar
    if player_ar == "[0][0]":
        conn = sqlite3.connect('../../files/Game_info.db') #connect to database
        cur = conn.cursor()
        #check level:
        cur.execute("SELECT * FROM info_play WHERE rowid=1")
        level = cur.fetchall()
        if level[0][0] == 7:
            cur.execute("SELECT * FROM info_cc WHERE rowid=1") #for sql codes : SELECT user 's level
            coin = cur.fetchall()
            cur.execute("UPDATE info_cc SET Coin=" + str(coin[0][0] + 3) + " WHERE rowid=1;")
            cur.execute("UPDATE info_play SET level = 8 WHERE rowid=1;")
            level_up = pygame.mixer.Sound("../../Sounds/level_up.ogg")
            level_up.set_volume(charecter()[1] / 100)
            pygame.mixer.Sound.play(level_up)
            time.sleep(5)
            conn.commit()
            conn.close()
        else:
            time.sleep(3)
            quit()
        
        

    else:
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(game_map,(0,0))
       gamedisplay.blit(atorpot_2,(x_c,y_c))
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       time.sleep(2)
       quit()


def output(out):
    global player_ar
    global out1_answer
    global out2_answer
    global map_ar
    global game_map
    #if
    
    if player_ar == "[5][0]":
        if out1_answer != False:
            if out1_answer == out:
                out1_answer = False
                true_ans = pygame.mixer.Sound("../../Sounds/True.ogg")
                true_ans.set_volume(charecter()[1] / 100)
                pygame.mixer.Sound.play(true_ans)
            else:
                time.sleep(3)
                gamedisplay.blit(game_map,(0,0))
                gamedisplay.blit(atorpot_2,(x_c,y_c))
                gamedisplay.blit(lost,(35,130))
                pygame.display.update()
                false_ans = pygame.mixer.Sound("../../Sounds/False.ogg")
                false_ans.set_volume(charecter()[1] / 100)
                pygame.mixer.Sound.play(false_ans)
                time.sleep(2)
                quit()
       
    elif player_ar == "[4][2]":
        if out2_answer != False:
            if out2_answer == out:
                out2_answer = False
                true_ans = pygame.mixer.Sound("../../Sounds/True.ogg")
                true_ans.set_volume(charecter()[1] / 100)
                pygame.mixer.Sound.play(true_ans)
            else:
                time.sleep(3)
                lost = pygame.image.load("lost.png")
                gamedisplay.blit(game_map,(0,0))
                gamedisplay.blit(atorpot_2,(x_c,y_c))
                gamedisplay.blit(lost,(35,130))
                pygame.display.update()
                false_ans = pygame.mixer.Sound("../../Sounds/False.ogg")
                false_ans.set_volume(charecter()[1] / 100)
                pygame.mixer.Sound.play(false_ans)
                time.sleep(2)
                quit()
    else:
       time.sleep(3)
       lost = pygame.image.load("lost.png")
       gamedisplay.blit(lost,(35,130))
       pygame.display.update()
       false_ans = pygame.mixer.Sound("../../Sounds/False.ogg")
       false_ans.set_volume(charecter()[1] / 100)
       pygame.mixer.Sound.play(false_ans)
       time.sleep(2)
       quit()
       
    if out2_answer == False and out1_answer == False:
        time.sleep(1)
        game_map = pygame.image.load("map2.png")
        gamedisplay.blit(game_map,(0,0))
        gamedisplay.blit(atorpot_2,(x_c,y_c))
        pygame.display.update()

        time.sleep(0.1)
        game_map = pygame.image.load("map3.png")
        gamedisplay.blit(game_map,(0,0))
        gamedisplay.blit(atorpot_2,(x_c,y_c))
        pygame.display.update()

        time.sleep(0.1)
        game_map = pygame.image.load("map4.png")
        gamedisplay.blit(game_map,(0,0))
        gamedisplay.blit(atorpot_2,(x_c,y_c))
        pygame.display.update()

        time.sleep(0.1)
        game_map = pygame.image.load("map5.png")
        gamedisplay.blit(game_map,(0,0))
        gamedisplay.blit(atorpot_2,(x_c,y_c))
        pygame.display.update()
        map_ar[1][1] = 1
    

    
