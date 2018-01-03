#Erik Hansen
#12/18/17
#battleship.py

from ggame import *
from random import randint

#Constants
EMPTY = 0
MISS = 1
HIT = 2
SHIP = 3
SQUARESIZE = 50

def buildBoard():
    return [[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5]

buildBoard()
    
def reDrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            if data['playerboard'][row][col] == EMPTY:
                Sprite(square_empty,(row*SQUARESIZE,col*SQUARESIZE))
            if data['playerboard'][row][col] == SHIP:
                Sprite(square_ship,(row*SQUARESIZE,col*SQUARESIZE))
            if data['playerboard'][row][col] == MISS:
                Sprite(square_miss,(row*SQUARESIZE,col*SQUARESIZE))
            if data['playerboard'][row][col] == HIT:
                Sprite(square_hit,(row*SQUARESIZE,col*SQUARESIZE))
    for row in range(0,5):
        for col in range(0,5):
            if data['computerboard'][row][col] == EMPTY:
                Sprite(square_empty,(row*SQUARESIZE+300,col*SQUARESIZE))
            if data['computerboard'][row][col] == SHIP:
                Sprite(square_empty,(row*SQUARESIZE+300,col*SQUARESIZE))
            if data['computerboard'][row][col] == MISS:
                Sprite(square_miss,(row*SQUARESIZE+300,col*SQUARESIZE))
            if data['computerboard'][row][col] == HIT:
                Sprite(square_hit,(row*SQUARESIZE+300,col*SQUARESIZE))
            

def mouseClick(event):
    if data['shipcount'] < 3:
        if event.x <= SQUARESIZE*5 and event.y <= SQUARESIZE*5:
            pickcolumn = event.x//SQUARESIZE
            pickrow = event.y//SQUARESIZE
            if data['playerboard'][pickcolumn][pickrow] != SHIP:
                data['playerboard'][pickcolumn][pickrow] = SHIP
                data['shipcount']+=1
                reDrawAll()
    else:
        if event.x >= 300 and event.x<=300+SQUARESIZE*5:
            choosecolumn = (event.x-300)//SQUARESIZE
            chooserow = event.y//SQUARESIZE
            if data['computerboard'][choosecolumn][chooserow] == EMPTY:
                data['computerboard'][choosecolumn][chooserow] = MISS
                reDrawAll()
            elif data['computerboard'][choosecolumn][chooserow] == SHIP:
                data['computerboard'][choosecolumn][chooserow] = HIT
                reDrawAll()
            elif data['computerboard'][choosecolumn][chooserow] == MISS:
                data['computerboard'][choosecolumn][chooserow] = MISS
                reDrawAll()
            elif data['computerboard'][choosecolumn][chooserow] == HIT:
                data['computerboard'][choosecolumn][chooserow] = HIT
                reDrawAll()

def pickComputerShips():
    pick = False
    if pick == False:
        cships = 0
        while cships<3:
            row = randint(0,4)
            col = randint(0,4)
            if data['computerboard'][row][col] != SHIP:
                data['computerboard'][row][col] = SHIP
                cships += 1

def computerTurn():
    pick = False
    if pick == False:
        pships = 0
        while pships<3:
            row = randint(0,4)
            col = randint(0,4)
            if data['playerboard'][row][col] == SHIP:
                data['playerboard'][row][col] = HIT
                cships += 1
            else:
                data['playerboard'][row][col] = MISS

if __name__ == '__main__':
    
    data = {}
    data['shipcount'] = 0
    data['chits'] = 0
    data['phits'] = 0
    data['computerboard'] = buildBoard()
    data['playerboard'] = buildBoard()
    
    gray = Color(0xD3D3D3, 1)
    white = Color(0xFFFFFF, 1)
    blue = Color(0x0000FF, 1)
    red = Color(0xFF0000, 1)
    black = Color(0x000000, 1)
    blackOutline = LineStyle(1,black)
    
    square_empty = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,white)
    square_miss = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,gray)
    square_hit = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,red)
    square_ship = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,blue)
    reDrawAll()
    pickComputerShips()
    App().listenMouseEvent("click", mouseClick)
    App().run()