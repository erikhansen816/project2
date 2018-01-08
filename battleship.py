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

def buildBoard(): #creates an matrix that is 5x5 and empty
    return [[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5,[EMPTY]*5]



buildBoard()
    
def reDrawAll(): #a function that creates the board and sprites the different color squares depending on where the ships and hits are
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
    Sprite(TextAsset("USER", fill = black, style = "Bold 24pt Times"),(10,SQUARESIZE*5))
    Sprite(TextAsset("COMPUTER", fill = black, style = "Bold 24pt Times"),(310,SQUARESIZE*5))
            

def mouseClick(event): 
    if data['shipcount'] < 3: #part of function that places the players ships depending on where the click is
        if event.x <= SQUARESIZE*5 and event.y <= SQUARESIZE*5:
            pickcolumn = event.x//SQUARESIZE
            pickrow = event.y//SQUARESIZE
            if data['playerboard'][pickcolumn][pickrow] != SHIP:
                data['playerboard'][pickcolumn][pickrow] = SHIP
                data['shipcount']+=1
                reDrawAll()
    else:
        if data['gameover'] == False: #part of function that will determine if you hit a ship based on the click
            if event.x >= 300 and event.x<=300+SQUARESIZE*5:
                choosecolumn = (event.x-300)//SQUARESIZE
                chooserow = event.y//SQUARESIZE
                if data['computerboard'][choosecolumn][chooserow] == EMPTY:
                    data['computerboard'][choosecolumn][chooserow] = MISS
                    reDrawAll()
                    computer = True
                
                elif data['computerboard'][choosecolumn][chooserow] == SHIP:
                    data['computerboard'][choosecolumn][chooserow] = HIT
                    data['chits'] +=1
                    reDrawAll()
                    computer = True
                
                elif data['computerboard'][choosecolumn][chooserow] == MISS:
                    data['computerboard'][choosecolumn][chooserow] = MISS
                    reDrawAll()
                    computer = False
                
                elif data['computerboard'][choosecolumn][chooserow] == HIT:
                    data['computerboard'][choosecolumn][chooserow] = HIT
                    reDrawAll()
                    computer = False
                if computer == True:
                    computerTurn()
        #part of function that displays who won            
        if data['phits'] == 3 and data['chits']<3:
            data['gameover'] = True
            Sprite(TextAsset("Computer wins!!!!", fill = black, style = "Bold 40pt Times"),(320,22))
        if data['chits'] == 3 and data['phits']<3:
            data['gameover'] = True
            Sprite(TextAsset("Player wins!!!!", fill = black, style = "Bold 40pt Times"),(20,22))        

def pickComputerShips(): #randomly chooses three ships for the computer
    pick = False
    if pick == False:
        cships = 0
        while cships<3:
            row = randint(0,4)
            col = randint(0,4)
            if data['computerboard'][row][col] != SHIP:
                data['computerboard'][row][col] = SHIP
                cships += 1
        pick = True

def computerTurn(): #randomly guesses where the ships are on player board
    row = randint(0,4)
    col = randint(0,4)
    if data['playerboard'][row][col] == SHIP:
        data['playerboard'][row][col] = HIT
        reDrawAll()
        data['phits']+=1
    elif data['playerboard'][row][col] == MISS:
        computerTurn()
    elif data['playerboard'][row][col] == HIT:
        computerTurn()
    elif data['playerboard'][row][col] == EMPTY:
        data['playerboard'][row][col] = MISS
        reDrawAll()
       

if __name__ == '__main__': #runs the game
    
    #dictionary
    data = {}
    data['gameover'] = False
    data['shipcount'] = 0
    data['chits'] = 0
    data['phits'] = 0
    data['computerboard'] = buildBoard()
    data['playerboard'] = buildBoard()
    
    #colors
    gray = Color(0xD3D3D3, 1)
    white = Color(0xFFFFFF, 1)
    blue = Color(0x0000FF, 1)
    red = Color(0xFF0000, 1)
    black = Color(0x000000, 1)
    blackOutline = LineStyle(1,black)
    
    #squares
    square_empty = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,white)
    square_miss = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,gray)
    square_hit = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,red)
    square_ship = RectangleAsset(SQUARESIZE,SQUARESIZE,blackOutline,blue)
    
    reDrawAll()
    pickComputerShips()
    
    App().listenMouseEvent("click", mouseClick)
    App().run()