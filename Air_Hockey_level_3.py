import pygame
import math
import random
import text
import time
pygame.init()
#####<< colors >>####
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
#####<<< variable >>>#####
wall_crash=pygame.mixer.Sound("wall_crash.wav")
score_up=pygame.mixer.Sound("score_up.wav")
score_down=pygame.mixer.Sound("score_down.wav")
level_up=pygame.mixer.Sound("level_up.wav")
game_over=pygame.mixer.Sound("game_over.wav")
move_speed=1
sheet_w=500
sheet_h=700
clock=pygame.time.Clock()
sheet=pygame.display.set_mode((sheet_w,sheet_h))
pygame.display.set_caption('Air Hockey')
#####<<< def >>>###
def dist_poin_to_point(x_1,y_1,x_2,y_2):
    dist=math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)
    return dist
###########################
def game_level_3():
    move_angle=random.randrange(45,315)
    ball_x=int(sheet_w/2)
    ball_x_change=0
    ball_y=int(sheet_h/2)
    ball_y_change=0
    line_angle=0
    line_lenght=70
    other_line_lenght=80
    my_door_lenght=100
    other_door_lenght=80
    score=0
    intro=True
    i=0
    start_other_line_x=0
    start_other_line_y=30
    end_other_line_x=other_line_lenght
    end_other_line_y=30
    other_line_change=0
    while intro:
        if i==0:
            text.message_display("Level 3",sheet_w/2,sheet_h/2,white,50)
            time.sleep(2)
        ball_x_change=math.cos(move_angle*math.pi/180)*move_speed
        ball_y_change=math.sin(move_angle*math.pi/180)*move_speed
        ball_x=ball_x_change+ball_x
        ball_y=ball_y+ball_y_change
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        start_line_x=mouse[0]-line_lenght/2
        end_line_x=mouse[0]+line_lenght/2
        start_line_y=sheet_h-40
        end_line_y=sheet_h-40
        if end_other_line_x<=290:
            other_line_change+=0.0005
            start_other_line_x+=other_line_change
            end_other_line_x+=other_line_change
        elif start_other_line_x>=100:
            other_line_change-=0.0005
            start_other_line_x+=other_line_change
            end_other_line_x+=other_line_change
        if int(ball_y)-15==0:
            move_angle=move_angle*(-1)
        if int(ball_y)+15==sheet_h:
            move_angle=move_angle*(-1)
        if int(ball_x)-15==0:
            move_angle=180-move_angle
        if int(ball_x)+15==sheet_w:
            move_angle=180-move_angle
        if click[0]==1:
            line_angle+=0.2
            start_line_x=mouse[0]-(line_lenght/2)*math.cos(line_angle*math.pi/180)
            end_line_x=mouse[0]+(line_lenght/2)*math.cos(line_angle*math.pi/180)
            start_line_y=sheet_h-40-(line_lenght/2)*math.sin(line_angle*math.pi/180)
            end_line_y=sheet_h-40+(line_lenght/2)*math.sin(line_angle*math.pi/180)
        elif click[2]==1:
            line_angle-=0.2
            start_line_x=mouse[0]-(line_lenght/2)*math.cos(line_angle*math.pi/180)
            end_line_x=mouse[0]+(line_lenght/2)*math.cos(line_angle*math.pi/180)
            start_line_y=sheet_h-40-(line_lenght/2)*math.sin(line_angle*math.pi/180)
            end_line_y=sheet_h-40+(line_lenght/2)*math.sin(line_angle*math.pi/180)
        else:
            start_line_x=mouse[0]-(line_lenght/2)
            start_line_y=sheet_h-40
            line_angle=0
        if start_line_x<=int(ball_x)<=end_line_x and start_line_y<=int(ball_y)+15<=end_line_y or end_line_x<=int(ball_x)<=start_line_x and end_line_y<=int(ball_y)+15<=start_line_y or start_line_x<=int(ball_x)<=end_line_x and end_line_y<=int(ball_y)+15<=start_line_y or end_line_x<=int(ball_x)<=start_line_x and start_line_y<=int(ball_y)+15<=end_line_y:
            move_angle=2*line_angle-move_angle
            pygame.mixer.Sound.play(wall_crash)
        if start_other_line_x<=int(ball_x)<=end_other_line_x and start_other_line_y>=int(ball_y)-15:
            move_angle=move_angle*(-1)
        if sheet_w/2-my_door_lenght/2-15<=int(ball_x)<=sheet_w/2+my_door_lenght/2+15 and sheet_h==int(ball_y)+15:
            score-=1
            pygame.mixer.Sound.play(score_down)
            print(score)
        if sheet_w/2-other_door_lenght/2-15<=int(ball_x)<=sheet_w/2+other_door_lenght/2+15 and 0==int(ball_y)-15:
            score+=1
            pygame.mixer.Sound.play(score_up)
            print(score)
        if score<-5:
            text.message_display("Game Over",sheet_w/2,sheet_h/2,red,50)
            pygame.mixer.Sound.play(game_over)
            time.sleep(2)
            intro=False
            import Air_Hockey_level_1
        elif score>5: 
            text.message_display("Level Up",sheet_w/2,sheet_h/2,red,50)
            pygame.mixer.Sound.play(level_up)
            time.sleep(2)
            import Air_Hockey_level_4
            break  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        sheet.fill(black)
        pygame.draw.circle(sheet,red,(int(ball_x),int(ball_y)),15)
        pygame.draw.circle(sheet,green,(int(ball_x),int(ball_y)),5)
        pygame.draw.line(sheet,white,(start_line_x,start_line_y),(end_line_x,end_line_y),5)
        pygame.draw.line(sheet,white,(start_other_line_x,start_other_line_y),(end_other_line_x,end_other_line_y),5)
        pygame.draw.rect(sheet,green,(sheet_w/2-my_door_lenght/2,sheet_h-20,my_door_lenght,20))
        pygame.draw.rect(sheet,green,(sheet_w/2-other_door_lenght/2,0,other_door_lenght,20))
        pygame.draw.rect(sheet,blue,(20,520,20,20))
        pygame.draw.line(sheet,white,(30,40),(30,520),2)
        if score>=0:
            pygame.draw.line(sheet,green,(30,270),(30,270-score*50),8)
        elif score<0:
            pygame.draw.line(sheet,red,(30,270),(30,270-score*50),8)
        pygame.draw.rect(sheet,blue,(20,20,20,20))
        pygame.display.update()
        i+=1 
game_level_3()