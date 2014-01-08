#**********************************************************************************************************************************#
#        Author: Chaythanya SK                                                                                                     #
#        Name of project: MONSTER SWEEP GAME                                                                                       #
#        RULES: open the boxes containing numbers only if you open the monster containing box.. you die!! GAME OVER!               #
#            mere luck based game                                                                                                  #
#***********************************************************************************************************************************


import pygame
import random
# declaring colours
black=(0,0,0)
white=(255,255,255)
green=(1,255,0)
yellow=(15,100,0)
red=(255,0,0)
blue=(19,37,173)
orange=(240,69,12)
pygame.init()
size=[375,300]                  # size of the game window
screen=pygame.display.set_mode(size)    
pygame.display.set_caption('MONSTER SWEEP')    # title of the game window
done=False
smile=pygame.image.load("smiley.jpeg").convert()    #getting images
index=pygame.image.load("index.jpeg").convert()        #getting images

clock=pygame.time.Clock()
screen.fill(white)        
r1=[]
r2=[]
r3=[]
r4=[]
r5=[]
grid=[r1,r2,r3,r4,r5]        # game array
minecount=0    
remaining_no=0
GI=-1                # row to be selected initialised as -1
GJ=-1                # col to be selected initialised as -1
open_count=0            # no of boxes opened
def make():            #making the first look
    cord_y=0+50
    cord_x=0
    screen.fill(white)    
    for i in range(5):
        for j in range(5):
            pygame.draw.rect(screen,black,[cord_x,cord_y,75,50],2)        # draw the grid
            cord_x=cord_x+75
        cord_x=0
        cord_y=cord_y+50
    pygame.display.flip()            #update the screen
    assign(grid)
    
def assign(grid):        # assign monsters and numbers in the grid
    global minecount
    global remaining_no
    for i in range(5):                #fill the grid with random nos
        for j in range(5):
            grid[i].append(random.randrange(0,5))

    for b in range(10):                # put "bomb"(monsters) in some random places
        temp1=random.randrange(0,5)
        temp2=random.randrange(0,4)
        grid[temp1][temp2]='bomb'
    for i in range(5):
        for j in range(5):
            if grid[i][j]=='bomb':
                minecount=minecount+1        #count the no: of monsters
    remaining_no=25-minecount                #count the remaining boxes
    font=pygame.font.Font(None,25)
    text=font.render("monster count:"+str(minecount),True,black)    #blit the monster count in the screen
    screen.blit(text,[20,17])
    pygame.display.flip()            # update the screen

def checkbomb(x,y):                #identify the selected box.. x,y are the coordinates of mouse click
    global grid
    global open_count
    global temp_remaining_nos
    open_count=open_count+1            #box opened
    block_no=0
    selected_no=0
    flag=0
    lcord_x=0                # left x coordinate
    ucord_y=50                # up y coordinate
    dcord_y=100                # down y coordinate
    rcord_x=75                # right x coordinate
    for i in range(5):            
        for j in range(5):
            block_no=block_no+1
            if(x>lcord_x and x<rcord_x and y>ucord_y and y<dcord_y ):# find the selected box no (1-25)
                selected_no=block_no
                flag=1
                break
            
            lcord_x=lcord_x+75
            rcord_x=rcord_x+75
        
        if(flag==1):
            break
        lcord_x=0
        rcord_x=75
        ucord_y=ucord_y+50
        dcord_y=dcord_y+50
    find_grid_pos(selected_no)         # find row and col of the selected block no (1-25)
    grid_display(x,y,lcord_x,rcord_x,ucord_y,dcord_y)
def find_grid_pos(selected_no):        #find the row and col of the selected block no (1-25)
    global GI
    global GJ
    if selected_no==1:
        GI=0
        GJ=0
    if selected_no==2:
        GI=0
        GJ=1
    if selected_no==3:
        GI=0
        GJ=2
    if selected_no==4:
        GI=0
        GJ=3
    if selected_no==5:
        GI=0
        GJ=4
    if selected_no==6:
        GI=1
        GJ=0
    if selected_no==7:
        GI=1
        GJ=1
    if selected_no==8:
        GI=1
        GJ=2
    if selected_no==9:
        GI=1
        GJ=3
    if selected_no==10:
        GI=1
        GJ=4
    if selected_no==11:
        GI=2
        GJ=0
    if selected_no==12:
        GI=2
        GJ=1
    if selected_no==13:
        GI=2
        GJ=2
    if selected_no==14:
        GI=2
        GJ=3
    if selected_no==15:
        GI=2
        GJ=4
    if selected_no==16:
        GI=3
        GJ=0
    if selected_no==17:
        GI=3
        GJ=1
    if selected_no==18:
        GI=3
        GJ=2
    if selected_no==19:
        GI=3
        GJ=3
    if selected_no==20:
        GI=3
        GJ=4
    if selected_no==21:
        GI=4
        GJ=0
    if selected_no==22:
        GI=4
        GJ=1
    if selected_no==23:
        GI=4
        GJ=2
    if selected_no==24:
        GI=4
        GJ=3
    if selected_no==25:
        GI=4
        GJ=4

    
    

def grid_display(x,y,lcord_x,rcord_x,ucord_y,dcord_y): # display the content of the opened box
    global GI
    global GJ
    global grid
    #print grid
    font=pygame.font.Font(None,25)
    if(str(grid[GI][GJ])=='bomb'and open_count>=1): # if the opened box contains bomb show game over
        showgrid_gameover()            # diaply whole grid
    else:                        # else display the no:    
        text=font.render(str(grid[GI][GJ]),True,black)
        screen.blit(text,[lcord_x+30,ucord_y+15])
        if (open_count==remaining_no+1):        #if open count equals remining no you win!
            showgrid_win()            #display whole grid
    pygame.display.flip()                # update screen to show no:
def showgrid_gameover():                # show game over screen
    global grid
    x_cord=0
    y_cord=50
    for i in range(5):
        for j in range(5):
            if (grid[i][j]=='bomb'):
                screen.blit(index,[x_cord+20,y_cord+5])
            else:
                font=pygame.font.Font(None,25)
                text=font.render(str(grid[i][j]),True,black)
                screen.blit(text,[x_cord+30,y_cord+15])
            
            x_cord=x_cord+75
        x_cord=0
        y_cord=y_cord+50
    pygame.draw.rect(screen,white,[0,0,375,50])

    screen.blit(smile,[170,7])
    font=pygame.font.Font(None,25)
    text=font.render("press me--->",True,black)    # show press me smiley to restart game
    screen.blit(text,[55,17])
    font=pygame.font.Font(None,55)
    text=font.render("GAME OVER!!!",True,blue)
    screen.blit(text,[80,150])
    pygame.display.flip()
            
def showgrid_win():            # show "you won" screen
    global grid
    x_cord=0
    y_cord=50
    for i in range(5):
        for j in range(5):
            if (grid[i][j]=='bomb'):
                screen.blit(index,[x_cord+20,y_cord+5])
            else:
                font=pygame.font.Font(None,25)
                text=font.render(str(grid[i][j]),True,black)
                screen.blit(text,[x_cord+30,y_cord+15])

            x_cord=x_cord+75
        x_cord=0
        y_cord=y_cord+50
    pygame.draw.rect(screen,white,[0,0,375,50])
    screen.blit(smile,[170,7])
    font=pygame.font.Font(None,25)
    text=font.render("press me--->",True,black)        # show press me smiley to restart the game
    screen.blit(text,[55,17])
    font=pygame.font.Font(None,50)
    text=font.render("BRAVO YOU WIN!!!",True,blue)
    screen.blit(text,[60,150])

def check_reset(x,y):            # check if the press me smiley is pressed
    global r1
    global r2
    global r3
    global r4
    global r5
    global grid
    global minecount
    global remaining_no
    global GI
    global GJ
    global open_count
    if(x>=170 and x<=210 and y>=7 and y<=47):    # trace the coordinates
        r1=[]                    # reinitialise everything
        r2=[]
        r3=[]
        r4=[]
        r5=[]
        grid=[r1,r2,r3,r4,r5]
        minecount=0
        remaining_no=0
        GI=-1
        GJ=-1
        open_count=0
        temp_remaining_nos=0
        screen.fill(white)
        make()                # make the screen again



make()
while done==False:
    clock.tick(20)
    for event in pygame.event.get():    # for each thing you do in the screen
        
        if event.type==pygame.QUIT:    # if it is quit exit the loop
            done=True
        elif(event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]): # if the mouse is pressed
            x,y=pygame.mouse.get_pos()        # get the position
            check_reset(x,y)            # check if the reset button is pressed
            checkbomb(x,y)                # check for the bomb
        
    pygame.display.flip()                    # update the screen
pygame.quit()                            # quit the game
    
















































