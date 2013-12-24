import pygame
import random
black=(0,0,0)
white=(255,255,255)
green=(1,255,0)
yellow=(15,100,0)
red=(255,0,0)
blue=(19,37,173)
orange=(240,69,12)
pygame.init()
size=[375,300]
screen=pygame.display.set_mode(size)
pygame.display.set_caption('MONSTER SWEEP')
done=False
smile=pygame.image.load("smiley.jpeg").convert()
index=pygame.image.load("index.jpeg").convert()

clock=pygame.time.Clock()
screen.fill(white)
#play_count=0
r1=[]
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
def make():
	cord_y=0+50
	cord_x=0
	screen.fill(white)
	for i in range(5):
		for j in range(5):
			pygame.draw.rect(screen,black,[cord_x,cord_y,75,50],2)
			cord_x=cord_x+75
		cord_x=0
		cord_y=cord_y+50
	#screen.blit(smile,[170,7])
	#font=pygame.font.Font(None,25)
	#text=font.render("monster count",True,black)
	#screen.blit(text,[20,17])
	
	pygame.display.flip()
	assign(grid)
	
def assign(grid):
	global minecount
	global remaining_no
	for i in range(5):
	        for j in range(5):
        	        grid[i].append(random.randrange(0,5))

	for b in range(10):
		temp1=random.randrange(0,5)
		temp2=random.randrange(0,4)
		grid[temp1][temp2]='bomb'
	for i in range(5):
        	for j in range(5):
                	if grid[i][j]=='bomb':
                        	minecount=minecount+1
	remaining_no=25-minecount
	font=pygame.font.Font(None,25)
        text=font.render("monster count:"+str(minecount),True,black)
        screen.blit(text,[20,17])
	pygame.display.flip()

#temp_remaining_nos=remaining_no
def checkbomb(x,y):
	global grid
	global open_count
	global temp_remaining_nos
	#temp_remaining_nos=remaining_nos

	pygame.draw.rect(screen,white,[273,17,20,20])
	font=pygame.font.Font(None,25)
	open_count=open_count+1
	block_no=0
	selected_no=0
	flag=0
	lcord_x=0
	ucord_y=50
	dcord_y=100
	rcord_x=75
	for i in range(5):
		for j in range(5):
			block_no=block_no+1
			if(x>lcord_x and x<rcord_x and y>ucord_y and y<dcord_y ):
				selected_no=block_no
				flag=1
#				pygame.draw.rect(screen,white,[273,17,20,20])
#			        font=pygame.font.Font(None,25)
#			        remaining_nos-=1
# 			        text=font.render("Remaining:"+str(remaining_nos),True,black)
#		 		screen.blit(text,[175,17])
#   				pygame.display.flip()
				break
			
			lcord_x=lcord_x+75
			rcord_x=rcord_x+75
		
		if(flag==1):
			break
		lcord_x=0
		rcord_x=75
		ucord_y=ucord_y+50
		dcord_y=dcord_y+50
	#print selected_no
	find_grid_pos(selected_no)
	grid_display(x,y,lcord_x,rcord_x,ucord_y,dcord_y)
def find_grid_pos(selected_no):
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

	
	

def grid_display(x,y,lcord_x,rcord_x,ucord_y,dcord_y):
	global GI
	global GJ
	global grid
	#print grid
	#print grid[GI][GJ]
	font=pygame.font.Font(None,25)
	if(str(grid[GI][GJ])=='bomb'and open_count>=1):
		showgrid_gameover()
	else:
		text=font.render(str(grid[GI][GJ]),True,black)
		screen.blit(text,[lcord_x+30,ucord_y+15])
		if (open_count==remaining_no+1):
			showgrid_win()
	pygame.display.flip()
def showgrid_gameover():
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
	#font=pygame.font.Font(None,50)
	pygame.draw.rect(screen,white,[0,0,375,50])

	screen.blit(smile,[170,7])
        font=pygame.font.Font(None,25)
        text=font.render("press me--->",True,black)
        screen.blit(text,[55,17])
	font=pygame.font.Font(None,55)
	text=font.render("GAME OVER!!!",True,blue)
	screen.blit(text,[80,150])
        pygame.display.flip()
			
def showgrid_win():
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
        text=font.render("press me--->",True,black)
        screen.blit(text,[55,17])
	font=pygame.font.Font(None,50)
        text=font.render("BRAVO YOU WIN!!!",True,blue)
        screen.blit(text,[60,150])

def check_reset(x,y):
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
	global temp_remaining_nos
	if(x>=170 and x<=210 and y>=7 and y<=47):
		#print 'hello'
		r1=[]
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
		make()



make()
while done==False:
	clock.tick(20)
	for event in pygame.event.get():
		
		if event.type==pygame.QUIT:
			done=True
		elif(event.type==pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]):
			x,y=pygame.mouse.get_pos()
			check_reset(x,y)
			checkbomb(x,y)		
		
	pygame.display.flip()
pygame.quit()
	
















































