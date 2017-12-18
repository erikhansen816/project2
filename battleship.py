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
    return
    
def reDrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for row in range(0,5):
        for col in range(0,5):
            Sprite(square,(10+row*SQUARESIZE,10+col*SQUARESIZE))

if __name__ == '__main__':
    black = Color(0x000000,1)
    white = Color(0xFFFFFF,1)
    blackOutline = LineStyle(1,black)
    square = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,white)
    reDrawAll()
    App().run()