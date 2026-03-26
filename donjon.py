#Quoicoubesque group
#modif test
from tkinter import *
from Visuel.transition import *
from Visuel.printThings import *
from Visuel.texturePack import *
from Inventory import *
import json
# Global variable
screenWidth = 800
screenHeight = 600
divisionSize = 50
maxX = screenWidth//divisionSize
maxY = screenHeight//divisionSize
nbIndex = 20
backgroundColor = "#D2DF89"
borderColor = "#FFFFFF"
writtingStyle = "Verdana"
labelStyle = (writtingStyle,"13")
state = "menu"
Xposition = (maxX-1)//2
Yposition = (maxY-1)//2
iClicked = False
level = 1
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

def move(direction,Xposition,Yposition,area) :
    printThings(screen,area[Yposition][Xposition],divisionSize,Xposition,Yposition)
    match direction :
        case "up" :
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition-1)
        case "down" :
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition+1)
        case "left" :
            printThings(screen,playerTexture,divisionSize,Xposition-1,Yposition)
        case "right" :
            printThings(screen,playerTexture,divisionSize,Xposition+1,Yposition)

def menu() :
    screen.delete("all")
    screen.create_rectangle(0,0,screenWidth,screenHeight//4,fill="#D36221")
    indexThickness = screenHeight//nbIndex
    screen.create_rectangle(screenWidth//4,8*indexThickness,screenWidth*3//4,9*indexThickness,outline = borderColor,width = 3,fill="#D36221")
    screen.create_text(screenWidth//2,(8.5*indexThickness)//1,text = "Jouer",font = labelStyle)
    screen.create_rectangle(screenWidth//4,10*indexThickness,screenWidth*3//4,11*indexThickness,outline = borderColor,width = 3,fill="#994514")
    screen.create_text(screenWidth//2,(10.5*indexThickness)//1,text = "Paramètres",font = labelStyle)
    screen.create_rectangle(screenWidth//4,12*indexThickness,screenWidth*3//4,13*indexThickness,outline = borderColor,width = 3,fill="#57270B")
    screen.create_text(screenWidth//2,(12.5*indexThickness)//1,text = "Sortir",font = labelStyle)

def printStart() :
    global startArea
    startArea = [[grassTexture for _ in range(maxX)] for _ in range(maxY)]
    #createCarpet(startArea, 8, 8, 10, 11, darkBlue)
    printArea(screen,startArea,maxX,maxY,divisionSize)
    printThings(screen,squarePotionTexture,divisionSize,2,3)
    printThings(screen,playerTexture,divisionSize,(maxX-1)//2,(maxY-1)//2)
    '''printThings(screen,chestTexture,divisionSize,1,1)
    printThings(screen,torchTexture,divisionSize,1,2)
    printThings(screen,roundPotionTexture,divisionSize,1,3)
    printThings(screen,squarePotionTexture,divisionSize,1,4)
    printThings(screen,trianglePotionTexture,divisionSize,1,5)
    printThings(screen,upsideDownTrianglePotionTexture,divisionSize,1,6)'''


def printSettings() :
    screen.delete("all")
    screen.create_rectangle(0,0,screenWidth,screenHeight//4,fill="#D36221")

def clickSituation(event) :
    Xaxe = event.x
    Yaxe = event.y
    global state
    global Xposition
    global Yposition
    global startArea
    match state :
        case "menu" :
            if Xaxe > screenWidth//4 and Xaxe < 3*screenWidth//4 :
                positionIndex = int(((Yaxe / screenHeight)*nbIndex)//1)
                match positionIndex :
                    case 8 :
                        state = "play"
                        transUpLink()
                        printStart()
                    case 10 :
                        state = "settings"
                    case 12 :
                        window.destroy()
                        state = "exit"
        case "play" :
            pass #arrowMove(event)

def keySituation(event) :
    global Xposition
    global Yposition
    global startArea
    global iClicked
    global level
    with open("Jeu.json","r",encoding="utf-8") as fichier:
        dict = json.load(fichier)
        le_niveau = dict[str(level)]
        if state == "play":
            dir = str(repr(event.char)).lower()
            if dir == "'z'":
                if Yposition > 0 and colision(level)[3] is True:
                    if deplacable(level)[3] is True:
                        for cle in le_niveau[Yposition-1][Xposition].keys():
                            modifierjson("Jeu.json",Yposition-2,Xposition,{str(cle): True},str(level))
                        modifierjson("Jeu.json",Yposition-1,Xposition,{"grassTexture": False},str(level))
                        printThings(screen,squarePotionTexture,divisionSize,Xposition,Yposition-2)
                        printThings(screen,grassTexture,divisionSize,Xposition,Yposition-1)
                    move("up",Xposition,Yposition, startArea)
                    Yposition -= 1
            if dir == "'q'":
                if Xposition > 0 and colision(level)[1] is True:
                    if deplacable(level)[1]:
                        for cle in le_niveau[Yposition][Xposition-1].keys():
                            modifierjson("Jeu.json",Yposition,Xposition-2,{str(cle): True},str(level))
                        modifierjson("Jeu.json",Yposition,Xposition-1,{"grassTexture": False},str(level))
                        printThings(screen,squarePotionTexture,divisionSize,Xposition-2,Yposition)
                        printThings(screen,grassTexture,divisionSize,Xposition-1,Yposition)
                    move("left",Xposition,Yposition, startArea)
                    Xposition -= 1
            if dir == "'s'":
                if Yposition < maxY-1 and colision(level)[2] is True:
                    if deplacable(level)[2] is True:
                        for cle in le_niveau[Yposition+1][Xposition].keys():
                            modifierjson("Jeu.json",Yposition+2,Xposition,{str(cle): True},str(level))
                        modifierjson("Jeu.json",Yposition+1,Xposition,{"grassTexture": False},str(level))
                        printThings(screen,squarePotionTexture,divisionSize,Xposition,Yposition+2)
                        printThings(screen,grassTexture,divisionSize,Xposition,Yposition+1)
                    move("down",Xposition,Yposition, startArea)
                    Yposition += 1
            if dir == "'d'":
                if Xposition < maxX-1 and colision(level)[0] is True:
                    if deplacable(level)[0] is True:
                        for cle in le_niveau[Yposition][Xposition+2].keys():
                            modifierjson("Jeu.json",Yposition,Xposition+2,{str(cle): True},str(level))
                        modifierjson("Jeu.json",Yposition,Xposition+1,{"grassTexture": False},str(level))
                        printThings(screen,squarePotionTexture,divisionSize,Xposition+2,Yposition)
                        printThings(screen,grassTexture,divisionSize,Xposition+1,Yposition)
                    move("right",Xposition,Yposition, startArea)
                    Xposition += 1
            if dir == "'i'" :
                iClicked = not(iClicked)
                seeInventory(window, iClicked)

def modifierjson(Json,X,Y,data,niveau):
    with open(Json,"r",encoding="utf-8") as fichier:
        dict = json.load(fichier)
        listex2 = dict[niveau]
        listex2[X][Y] = data
        dict[niveau] = listex2
    with open(Json,"w",encoding="utf-8") as fichier:
        json.dump(dict,fichier,indent = 2)


def printHey() :
    print("Hey !")

def colision(niveau):
    global Xposition
    global Yposition
    with open("Jeu.json","r",encoding="utf-8") as fichier:
        dict = json.load(fichier)
        le_niveau = dict[str(niveau)]

        for valeur in le_niveau[Yposition-1][Xposition].values():
            if valeur is None:
                
                YmoveDown = False
            else:
                YmoveDown = True

        for valeur in le_niveau[Yposition+1][Xposition].values():
            if valeur is None:
                YmoveUp = False
            else:
                YmoveUp = True
        for valeur in le_niveau[Yposition][Xposition-1].values():
            if valeur is None:
                Xmoveleft = False
            else:
                Xmoveleft = True
        for valeur in le_niveau[Yposition][Xposition+1].values():
            if valeur is None:
                Xmoveright = False
            else:
                Xmoveright = True
    return Xmoveright,Xmoveleft,YmoveUp,YmoveDown

def deplacable(niveau):
    global Xposition
    global Yposition
    with open("Jeu.json","r",encoding="utf-8") as fichier:
        dict = json.load(fichier)
        le_niveau = dict[str(niveau)]

        for valeur in le_niveau[Yposition-1][Xposition].values():
            if valeur is True:
                deplacdown = True
            else:
                deplacdown = False

        for valeur in le_niveau[Yposition+1][Xposition].values():
            if  valeur is True:
                deplacup = True
            else:
                deplacup = False

        for valeur in le_niveau[Yposition][Xposition-1].values():
            if valeur is True:
                deplacleft = True
            else:
                deplacleft = False

        for valeur in le_niveau[Yposition][Xposition+1].values():
            if valeur is True:
                deplaceright = True
            else:
                deplaceright = False

    return deplaceright,deplacleft,deplacup,deplacdown
window = Tk()
window.title("Donjon")
window.geometry("1200x700")
window.config(bg = "#888888")

screen = Canvas(window,height = screenHeight,width = screenWidth,bg = backgroundColor)
screen.place(x = 0,y = 0)
"""upButton = Button(window,text = "up",command = transUpLink)
upButton.place(x = 430,y = 0)
downButton = Button(window,text = "down",command = transDownLink)
downButton.place(x = 430,y = 60)
leftButton = Button(window,text = "left",command = transLeftLink)
leftButton.place(x = 400,y = 30)
rightButton = Button(window,text = "right",command = transRightLink)
rightButton.place(x = 460,y = 30)"""
screen.delete("all")
menu()
screen.bind("<Button-1>", clickSituation )
screen.bind("<Button-2>", printHey)
window.bind("<Key>", keySituation )
window.mainloop()
