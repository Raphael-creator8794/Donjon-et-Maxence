#Quoicoubesque group
#modif test
from tkinter import *
from transition import *
from printThings import *
from texturePack import *

# Global variable
screenWidth = 800
screenHeight = 600
divisionSize = 50
maxX = screenWidth//divisionSize
maxY = screenHeight//divisionSize
backgroundColor = "#D2DF89"
state = "menu"

# Test variable
testPlayer = [
    [None,None,None,None,None,None,None,None],
    [None,None,black,black,black,black,None,None],
    [None,black,black,orange,orange,black,black,None],
    [None,black,orange,orange,orange,orange,black,None],
    [None,None,purple,purple,purple,purple,None,None],
    [None,purple,None,purple,purple,None,purple,None],
    [None,None,None,purple,purple,None,None,None],
    [None,None,purple,None,None,purple,None,None]
]

def transDownLink() :
    transDown(screen,screenWidth,screenHeight)

def transUpLink() :
    transUp(screen,screenWidth,screenHeight)

def transLeftLink() :
    transLeft(screen,screenWidth,screenHeight)

def transRightLink() :
    transRight(screen,screenWidth,screenHeight)

def move(direction,Xposition,Yposition) :
    printThings(screen,grassTexture,divisionSize,Xposition,Yposition)
    match direction :
        case "up" :
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition-1)
        case "down" :
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition+1)
        case "left" :
            printThings(screen,playerTexture,divisionSize,Xposition-1,Yposition)
        case "right" :
            printThings(screen,playerTexture,divisionSize,Xposition+1,Yposition)

def printStart() :
    startArea = [["grass" for _ in range(maxX)] for _ in range(maxY)]
    printArea(screen,startArea,maxX,maxY,divisionSize)
    printThings(screen,playerTexture,divisionSize,(maxX-1)//2,(maxY-1)//2)
    #printThings(screen,crateTexture,divisionSize,1,1)


def printSettings() :
    screen.delete("all")
    screen.create_rectangle(0,0,screenWidth,screenHeight//4,fill="#D36221")

def clickSituation(event) :
    Xaxe = event.x
    Yaxe = event.y
    global state
    global Xposition
    global Yposition
    match state :
        case "menu" :
            if Xaxe > screenWidth//4 and Xaxe < 3*screenWidth//4 :
                positionIndex = int(((Yaxe / screenHeight)*nbIndex)//1)
                match positionIndex :
                    case 8 :
                        state = "play"
                        transUpLink()
                        printStart()
                        Xposition = (maxX-1)//2
                        Yposition = (maxY-1)//2
                    case 10 :
                        state = "settings"
                    case 12 :
                        window.destroy()
                        state = "exit"
        case "play" :
            Xindex = Xaxe//divisionSize
            Yindex = Yaxe//divisionSize
            #print(Yindex," - ",Yposition)
            if Xindex == Xposition :
                if Yindex > Yposition :
                    move("down",Xposition,Yposition)
                    Yposition += 1
                elif Yindex < Yposition : 
                    move("up",Xposition,Yposition)
                    Yposition -= 1
            elif Yindex == Yposition :
                if Xindex > Xposition :
                    move("right",Xposition,Yposition)
                    Xposition += 1
                else :
                    move("left",Xposition,Yposition)
                    Xposition -= 1

def arrowMove(event) :
    print(repr(event.char))

def printHey() :
    print("Hey !")

window = Tk()
window.title("Donjon")
window.geometry("1200x700")
window.config(bg = "#888888")

screen = Canvas(window,height = screenHeight,width = screenWidth,bg = backgroundColor)
screen.place(x = 0,y = 0)
screen.delete("all")
printMenu()
screen.bind("<Button-1>", clickSituation )
screen.bind("<Button-2>", printHey)
window.bind("<Key>", arrowMove )
window.mainloop()
