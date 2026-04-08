"""definingMovement = True
if definingMovement :
    definingMovement = False"""
import json
from Donjon import maxX,maxY,divisionSize
#from Donjon import Xposition,Yposition
from Visuel.PrintThings import *
from Visuel.Transition import *
from time import time

level = 0

if level == 0 or level == 1:
    Xposition = (maxX-13)//2
    Yposition = (maxY)//2
elif level == 2:
    Xposition = (maxX-15)//2
    Yposition = (maxY)//2
elif level == 3:
    Xposition = (maxX-15)//2
    Yposition = (maxY)//2
elif level == 4:
    Xposition = (maxX-15)//2
    Yposition = (maxY)//2


with open("Levels.json","r") as datas :
    levelDatas = load(datas)[level]
actualRoom = 0
actualArea = levelDatas[actualRoom]["area"]
objects = levelDatas[actualRoom]["objects"]
lastTimeMovement = 0
delayMovement = 0.1

isMovable = ["crateTexture","torchTexture","chestTexture","stoneTexture","blueJewelTexture","greenJewelTexture","redJewelTexture"]
isInteractible = []

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

def movable(niveau,direction):
    global Xposition
    global Yposition
    with open("Jeu.json","r",encoding="utf-8") as fichier:
        dict = json.load(fichier)
        le_niveau = dict[str(niveau)]
        match direction :
            case "down" :
                for valeur in le_niveau[Yposition-1][Xposition].values():
                    return (valeur is True)
            case "up" :
                for valeur in le_niveau[Yposition+1][Xposition].values():
                    return (valeur is True)
            case "left" :
                for valeur in le_niveau[Yposition][Xposition-1].values():
                    return (valeur is True)
            case "right" :
                for valeur in le_niveau[Yposition][Xposition+1].values():
                    return (valeur is True)

def modifierjson(Json,X,Y,data,niveau):
    with open(Json,"r",encoding="utf-8") as fichier:
        dict = json.load(fichier)
        listex2 = dict[niveau]
        listex2[X][Y] = data
        dict[niveau] = listex2
    with open(Json,"w",encoding="utf-8") as fichier:
        json.dump(dict,fichier,indent = 2)

def movePlayer(screen,direction,Xposition,Yposition,area) :
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

def passRoom() :
    global actualArea
    global objects
    global actualMap
    global actualRoom
    global Xposition
    global Yposition
    global levelDatas
    global level
    for i in levelDatas[actualRoom]["door"] :
        if i[0] == Xposition and i[1] == Yposition :
            break
    Xposition = i[3]
    Yposition = i[4]
    level += 1
    print(level)
    with open("Levels.json","r") as datas :
        levelDatas = load(datas)[level]
        actualRoom = 0
        actualArea = levelDatas[actualRoom]["area"]
        objects = levelDatas[actualRoom]["objects"]
    '''
    actualRoom = i[2]
    actualMap = levelDatas[actualRoom]
    actualArea = actualMap["area"]
    objects = actualMap["objects"]

def moveDir(screen,dir,screenWidth,screenHeight) : #,area,objects
    global Xposition
    global Yposition
    global lastTimeMovement

    if lastTimeMovement + delayMovement > time() :
        return
    else :
        lastTimeMovement = time()

    if dir == "'z'":
        try :
            theObject = objects[Yposition-1][Xposition] 
            if theObject == None :
                movePlayer(screen,"up",Xposition,Yposition, actualArea)
                Yposition -= 1
            elif theObject  == "Holedown" :
                Yposition -= 1
                transUp(screen,screenWidth,screenHeight)
                passRoom()
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
            elif theObject in isMovable :
                if objects[Yposition-2][Xposition] == None :
                    printThings(screen,actualArea[Yposition-1][Xposition],divisionSize,Xposition,Yposition-1)
                    printThings(screen,objects[Yposition-1][Xposition],divisionSize,Xposition,Yposition-2)
                    movePlayer(screen,"up",Xposition,Yposition, actualArea)
                    objects[Yposition-2][Xposition] = objects[Yposition-1][Xposition]
                    objects[Yposition-1][Xposition] = None
                    Yposition -= 1
        except IndexError :
            return
    
    if dir == "'q'":
        try :
            theObject = objects[Yposition][Xposition-1] 
            if theObject == None :
                movePlayer(screen,"left",Xposition,Yposition, actualArea)
                Xposition -= 1
            elif theObject == "Holedown" or theObject == "HoleUp" :
                Xposition -= 1
                transLeft(screen,screenWidth,screenHeight)
                passRoom()
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
            elif theObject in isMovable :
                if objects[Yposition][Xposition-2] == None :
                    printThings(screen,actualArea[Yposition][Xposition-1],divisionSize,Xposition-1,Yposition)
                    printThings(screen,objects[Yposition][Xposition-1],divisionSize,Xposition-2,Yposition)
                    movePlayer(screen,"left",Xposition,Yposition, actualArea)
                    objects[Yposition][Xposition-2] = objects[Yposition][Xposition-1]
                    objects[Yposition][Xposition-1] = None
                    Xposition -= 1
        except IndexError :
            return
    
    if dir == "'s'":
        try :
            theObject = objects[Yposition+1][Xposition] 
            if theObject == None :
                movePlayer(screen,"down",Xposition,Yposition, actualArea)
                Yposition += 1
            elif theObject == "HoleUp" :
                Yposition += 1
                transDown(screen,screenWidth,screenHeight)
                passRoom()
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
            elif theObject in isMovable :
                if objects[Yposition+2][Xposition] == None :
                    printThings(screen,actualArea[Yposition+1][Xposition],divisionSize,Xposition,Yposition+1)
                    printThings(screen,objects[Yposition+1][Xposition],divisionSize,Xposition,Yposition+2)
                    movePlayer(screen,"down",Xposition,Yposition, actualArea)
                    objects[Yposition+2][Xposition] = objects[Yposition+1][Xposition]
                    objects[Yposition+1][Xposition] = None
                    Yposition += 1
        except IndexError :
            return
    
    if dir == "'d'":
        try :
            theObject = objects[Yposition][Xposition+1] 
            if theObject == None :
                movePlayer(screen,"right",Xposition,Yposition, actualArea)
                Xposition += 1
            elif theObject == "Holedown" or theObject == "HoleUp" :
                Xposition += 1
                transRight(screen,screenWidth,screenHeight)
                passRoom()
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
            elif theObject in isMovable :
                if objects[Yposition][Xposition+2] == None :
                    printThings(screen,actualArea[Yposition][Xposition+1],divisionSize,Xposition+1,Yposition)
                    printThings(screen,objects[Yposition][Xposition+1],divisionSize,Xposition+2,Yposition)
                    movePlayer(screen,"right",Xposition,Yposition, actualArea)
                    objects[Yposition][Xposition+2] = objects[Yposition][Xposition+1]
                    objects[Yposition][Xposition+1] = None
                    Xposition += 1
        except IndexError :
            return
    
    interact(screen)
    """if actualArea[Yposition][Xposition] in isInteractible :
        pass"""

def interact(screen) :
    match actualArea[Yposition][Xposition] :
        case "redPressurePlateTextureOff" :
            actualArea[Yposition][Xposition] = "redPressurePlateTextureOn"
            printThings(screen,"redPressurePlateTextureOn",divisionSize,Xposition,Yposition)
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition)
        case "redPressurePlateTextureOn" :
            actualArea[Yposition][Xposition] = "redPressurePlateTextureOff"
            printThings(screen,"redPressurePlateTextureOff",divisionSize,Xposition,Yposition)
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition)
        case "bluePressurePlateTextureOff" :
            actualArea[Yposition][Xposition] = "bluePressurePlateTextureOn"
            printThings(screen,"bluePressurePlateTextureOn",divisionSize,Xposition,Yposition)
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition)
        case "bluePressurePlateTextureOn" :
            actualArea[Yposition][Xposition] = "bluePressurePlateTextureOff"
            printThings(screen,"bluePressurePlateTextureOff",divisionSize,Xposition,Yposition)
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition)
        case "stairsTexture" :
            pass
        case _ :
            return


'''
def moveDirOld(screen,dir,area,le_niveau,level) :
    return
    global Xposition
    global Yposition
    if dir == "'z'":
        if Yposition > 0 and colision(level)[3] is True:
            if movable(level,"up") :
                modifierjson("Jeu.json",Yposition-2,Xposition,{list(le_niveau[Yposition-1][Xposition])[0] : True},str(level))
                modifierjson("Jeu.json",Yposition-1,Xposition,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
                printThings(screen,squarePotionTexture,divisionSize,Xposition,Yposition-2)
                printThings(screen,grassTexture,divisionSize,Xposition,Yposition-1)
            movePlayer(screen,"up",Xposition,Yposition, area)
            Yposition -= 1
    if dir == "'q'":
        if Xposition > 0 and colision(level)[1] is True:
            if movable(level,"left") :
                modifierjson("Jeu.json",Yposition,Xposition-2,{list(le_niveau[Yposition][Xposition-1])[0]: True},str(level))
                modifierjson("Jeu.json",Yposition,Xposition-1,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
                printThings(screen,squarePotionTexture,divisionSize,Xposition-2,Yposition)
                printThings(screen,grassTexture,divisionSize,Xposition-1,Yposition)
            movePlayer(screen,"left",Xposition,Yposition, area)
            Xposition -= 1
    if dir == "'s'":
        if Yposition < maxY-1 and colision(level)[2] is True:
            if movable(level,"down") :
                modifierjson("Jeu.json",Yposition+2,Xposition,{list(le_niveau[Yposition+1][Xposition])[0]: True},str(level))
                modifierjson("Jeu.json",Yposition+1,Xposition,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
                printThings(screen,squarePotionTexture,divisionSize,Xposition,Yposition+2)
                printThings(screen,grassTexture,divisionSize,Xposition,Yposition+1)
            movePlayer(screen,"down",Xposition,Yposition, area)
            Yposition += 1
    if dir == "'d'":
        if Xposition < maxX-1 and colision(level)[0] is True:
            if movable(level,"right") :
                for cle in le_niveau[Yposition][Xposition+2].keys():
                    modifierjson("Jeu.json",Yposition,Xposition+2,{list(le_niveau[Yposition][Xposition+1])[0]: True},str(level))
                modifierjson("Jeu.json",Yposition,Xposition+1,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
                printThings(screen,squarePotionTexture,divisionSize,Xposition+2,Yposition)
                printThings(screen,grassTexture,divisionSize,Xposition+1,Yposition)
            movePlayer(screen,"right",Xposition,Yposition, area)
            Xposition += 1 
'''