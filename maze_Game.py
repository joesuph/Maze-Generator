import pygame, math, time, random, copy


#SHOW PROGRESS???
show_progress = True

screen_height = 400
screen_width = 400
box_height = 20
box_width = 20

screen = pygame.display.set_mode([screen_height, screen_width])


xwalls = []
ywalls = []
point = [box_width, box_height]
visitedSquares = [copy.copy(point)]
count = 0

for xnum in range(1, int(screen_width / box_width)):
    for ynum in range(0,int(screen_height / box_height)):
        x = box_width * xnum
        y = box_height * ynum
        ywalls.append([[x,y],[x, y + box_height]])

for ynum in range(1, int(screen_height / box_height)):
    for xnum in range(0,int(screen_width / box_width)):
        x = box_width * xnum
        y = box_height * ynum
        xwalls.append([[x,y],[x + box_width, y]])

def updateWalls():
    screen.fill([0,0,0])

    if show_progress:
        for i in xwalls:
            pygame.draw.lines(screen,[0,255,255],True,i,1)
        for i in ywalls:
            pygame.draw.lines(screen,[255,0,255],True,i,1)
        pygame.display.flip()



def moveLeft():
    ywalls.remove([point,[point[0], point[1] + box_height]])
    point[0] -= box_width
    visitedSquares.append(copy.copy(point))
def moveRight():
    ywalls.remove([[point[0] + box_width,point[1]] ,[point[0] + box_width, point[1] + box_height]])             
    point[0] += box_width

    visitedSquares.append(copy.copy(point))
def moveUp():
    xwalls.remove([point,[point[0] + box_width, point[1]]])              
    point[1] -= box_height

    visitedSquares.append(copy.copy(point))
def moveDown():
    xwalls.remove([[point[0],point[1] + box_height],[point[0] + box_width, point[1] + box_height]]) 
    point[1] += box_height

    visitedSquares.append(copy.copy(point))
    

for i in visitedSquares:
    point = copy.copy(i)
    left = True
    right = True
    up = True
    down = True
    while left or right or up or down:
        r = random.randint(1,5)
        if r == 1:
            if (not [point[0] - box_width,point[1]] in visitedSquares) and point[0] != 0:
                moveLeft()
                left = True
                right = True
                up = True
                down = True
                updateWalls()
            else:
                left = False
        if r == 2:
            if (not [point[0] + box_width,point[1]] in visitedSquares) and point[0] != (screen_width - box_width):
                moveRight()
                left = True
                right = True
                up = True
                down = True
                updateWalls()
            else:
                right = False
        if r == 3:
            if (not [point[0],point[1] + box_height] in visitedSquares) and point[1] != (screen_height - box_height):
                moveDown()
                left = True
                right = True
                up = True
                down = True
                updateWalls()
            else:
                down = False
        if r == 4:
            if (not [point[0],point[1] - box_height] in visitedSquares) and point[1] != 0:
                moveUp()
                left = True
                right = True
                up = True
                down = True
                updateWalls()
            else:
                up = False
                
for i in xwalls:
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    pygame.draw.lines(screen,[r,g,b],True,i,1)
for i in ywalls:
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    pygame.draw.lines(screen,[r,g,b],True,i,1)

pygame.display.flip()
raw_input()
pygame.quit()
