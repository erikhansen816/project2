#Erik Hansen
#12/18/17
#battleship.py

from ggame import *

#Constants
EMPTY = 0
MISS = 1
HIT = 2
SQUARESIZE = 50

def buildBoard():
    return [['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]

buildBoard()
    
def reDrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            Sprite(square_empty,(row*SQUARESIZE,col*SQUARESIZE))
    for row in range(0,5):
        for col in range(0,5):
            Sprite(square_empty,(row*SQUARESIZE+300,col*SQUARESIZE))

def mouseClick(event):
    if data['shipcount'] < 3:
        if event.x

def pickComputerShips():
    pick = false
    if pick == false:
        cships = 0
        while cships<3:
            row = randint(0,4)
            col = randint(0,4)
            if data['computerboard'][row][col] != SHIP:
                data['computerboard'][row][col] = SHIP
                cships += 1
            
    

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
    square_miss = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,blue)
    square_hit = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,red)
    square_ship = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,white)
    reDrawAll()
    App().run()