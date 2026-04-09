"""definingMovement = True
if definingMovement :
    definingMovement = False"""
import json
from Donjon import maxX,maxY,divisionSize
#from Donjon import Xposition,Yposition
from Visuel.PrintThings import *
from Visuel.Transition import *
from time import time
from Inventory import *
from File import*
matchPosition = [((maxX-13)//2,(maxY)//2),((maxX-13)//2,(maxY)//2),((maxX-15)//2,(maxY)//2),((maxX-15)//2,(maxX-15)//2),((maxX-15)//2,(maxX-15)//2)]
bridge = True
level = 3
nbMove = 0
color_file = File(3)



with open("Levels.json","r") as datas :
    levelDatas = load(datas)[level]
actualRoom = 0
actualArea = levelDatas[actualRoom]["area"]
objects = levelDatas[actualRoom]["objects"]
blueBridge = True
greenBridge = True
redBridge = True
lastTimeMovement = 0
delayMovement = 0.1

isMovable = ["crateTexture","torchTexture","chestTexture","stoneTexture","blueJewelTexture","greenJewelTexture","redJewelTexture"]

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

def respawn(screen,screenWidth,screenHeight) :
    global Xposition
    global Yposition
    global levelDatas
    global actualArea
    global objects
    global nbMove
    global bridge

    bridge = True
    nbMove = 0
    nbCall = 0
    writtedPlayer = True
    blinkDelay = 0.1
    lastCall = time()
    while nbCall < 6 :
        now = time()
        if now > lastCall + blinkDelay :
            lastCall = now
            writtedPlayer = not(writtedPlayer)
            nbCall += 1
            if writtedPlayer :
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
            else :
                printThings(screen,actualArea[Yposition][Xposition],divisionSize,Xposition,Yposition)
            screen.update_idletasks()
    
    with open("Levels.json","r") as datas :
        levelDatas = load(datas)[level]
    actualArea = levelDatas[actualRoom]["area"]
    objects = levelDatas[actualRoom]["objects"]
    
    Xposition,Yposition = matchPosition[level]
    transDown(screen,screenWidth,screenHeight)
    printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
    printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)

def passRoom() :
    global actualArea
    global objects
    global actualMap
    global Xposition
    global Yposition
    global levelDatas
    global level
    for i in levelDatas[0]["door"] :
        if i[0] == Xposition and i[1] == Yposition :
            break
    Xposition = i[3]
    Yposition = i[4]
    level += 1
    with open("Levels.json","r") as datas :
        levelDatas = load(datas)[level]
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

    interact(screen,screenWidth,screenHeight)

def interact(screen,screenWidth,screenHeight) :
    global level
    global objects
    global color_file
    global bridge
    global Xposition
    global Yposition
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
        case "greyPressurePlateTextureOff" :
            actualArea[Yposition][Xposition] = "greyPressurePlateTextureOn"
            printThings(screen,"greyPressurePlateTextureOn",divisionSize,Xposition,Yposition)
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition)
        case "greyPressurePlateTextureOn" :
            actualArea[Yposition][Xposition] = "greyPressurePlateTextureOff"
            printThings(screen,"greyPressurePlateTextureOff",divisionSize,Xposition,Yposition)
            printThings(screen,playerTexture,divisionSize,Xposition,Yposition)
        case "lavaTexture" :
            respawn(screen,screenWidth,screenHeight)

    match level:
        case 0:
            if Xposition == 6 and Yposition == 2:
                printThings(screen,"StoneGroundTexture",divisionSize,7,5)
                printThings(screen,"StoneGroundTexture",divisionSize,7,6)
                objects[5][7] = None
                objects[6][7] = None
            if objects[9][15] == "torchTexture" and objects[2][15] == "torchTexture":
                actualArea[5][15] = "HoleUp"
                actualArea[6][15] = "Holedown"
                printThings(screen,"HoleUp",divisionSize,15,5)
                printThings(screen,"Holedown",divisionSize,15,6)
            if Xposition == 15 and (Yposition == 5 or Yposition == 6):
                transDown(screen,screenWidth,screenHeight)
                passRoom()
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
        case 1 :
            if actualArea[Yposition][Xposition] == "smallTorchTexture":
                addObject("smallTorchTexture")
                actualArea[Yposition][Xposition] = "StoneGroundTexture"
                
            if actualArea[Yposition][Xposition] == "greyBaseTexture":
                if findObjectIndex("smallTorchTexture"):
                    removeObject("smallTorchTexture")
                    actualArea[Yposition][Xposition] = "smallTorchTexture"

            if actualArea[1][6] == "smallTorchTexture" and actualArea[10][6] == "smallTorchTexture":
                if bridge:
                    for i in range (8, 15):
                        for j in range (5, 7):
                            actualArea[j][i] = "roofTexture"
                            objects[j][i] = None
                            printThings(screen, "roofTexture", divisionSize, i, j)
                bridge = False

            if Xposition == 8 and (Yposition == 5 or Yposition == 6):
                if not(bridge):
                    for i in range (8,10):
                        objects[11][i] = "brickWallHoleSpearUp"
                        printThings(screen, "brickWallHoleSpearUp", divisionSize, i, 11)
                        for j in range (7, 11):
                            objects[j][i] = "spearTexture"
                            printThings(screen, "spearTexture", divisionSize, i, j)
                        actualArea[6][i] = "spearPointTexture"
                        printThings(screen, "spearPointTexture", divisionSize, i, 6)
                    for i in range (11, 13):
                        objects[0][i] = "brickWallHoleSpearDown"
                        printThings(screen, "brickWallHoleSpearDown", divisionSize, i, 0)
                        for j in range (1, 5):
                            objects[j][i] = "spearTexture"
                            printThings(screen, "spearTexture", divisionSize, i, j)
                        actualArea[5][i] = "spearPointDownTexture"
                        printThings(screen, "spearPointDownTexture", divisionSize, i, 5)
                    objects[11][14] = "brickWallHoleSpearUp"
                    printThings(screen, "brickWallHoleSpearUp", divisionSize, 14, 11)
                    for j in range (7, 11):
                        objects[j][14] = "spearTexture"
                        printThings(screen, "spearTexture", divisionSize, 14, j)
                    actualArea[6][14] = "spearPointTexture"
                    printThings(screen, "spearPointTexture", divisionSize, 14, 6)

            if actualArea[Yposition][Xposition] == "spearPointTexture" or actualArea[Yposition][Xposition] == "spearPointDownTexture" or actualArea[Yposition][Xposition] == "lavaTexture":
                respawn(screen, screenWidth, screenHeight)
            if Xposition == 15 and (Yposition == 5 or Yposition == 6):
                transDown(screen,screenWidth,screenHeight)
                passRoom()
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
        case 2 :
            global nbMove
            global blueBridge
            global greenBridge
            global redBridge

            nbMove += 1
            if nbMove > 5 :
                nbMove = 1
            if nbMove == 4 and actualArea[10][14] == "redPressurePlateTextureOn" :
                printThings(screen,"brickWallHoleArrowleft",divisionSize,15,5)
                printThings(screen,"brickWallHoleArrowleft",divisionSize,15,6)
            if nbMove == 5 and actualArea[10][14] == "redPressurePlateTextureOn" :
                launchLeftSpears(screen,divisionSize,actualArea)
                if (Yposition == 5 or Yposition == 6) :
                    respawn(screen,screenWidth,screenHeight)
                else :
                    retractLeftSpears(screen,divisionSize,actualArea)
                    screen.delete("all")
                    printArea(screen,actualArea,objects,maxX,maxY,divisionSize,False)
                    printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
            if blueBridge :
                if objects[1][2] == "blueJewelTexture" :
                    blueBridge = False
                    printBridge(screen,divisionSize,actualArea,0)
            if greenBridge :
                if objects[1][5] == "greenJewelTexture" :
                    greenBridge = False
                    printBridge(screen,divisionSize,actualArea,1)
            if redBridge :
                if objects[1][8] == "redJewelTexture" :
                    redBridge = False
                    printBridge(screen,divisionSize,actualArea,2)
            if Xposition == 0 and (Yposition == 9 or Yposition == 10):
                transDown(screen,screenWidth,screenHeight)
                passRoom()
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
        case 3:
            print("Xposition : ",Xposition)
            print("Yposition : ",Yposition)

            color_file_model = File(3)
            color_file_model.push("redPressurePlateTextureOn")
            color_file_model.push("bluePressurePlateTextureOn")
            color_file_model.push("greyPressurePlateTextureOn")

            if  actualArea[10][8] == "redPressurePlateTextureOn" or actualArea[10][4] == "bluePressurePlateTextureOn" or actualArea[10][12] == "greyPressurePlateTextureOn":
                if actualArea[Yposition][Xposition] == "redPressurePlateTextureOn" or actualArea[Yposition][Xposition] == "bluePressurePlateTextureOn" or actualArea[Yposition][Xposition] == "greyPressurePlateTextureOn":
                    color_file.push(actualArea[Yposition][Xposition])
                    if color_file == color_file_model:
                        objects[9][2] = None
                        printThings(screen,"StoneGroundTexture",divisionSize,2,9)
            if Xposition == 1 and Yposition == 9:
                addObject("keyTexture")
                actualArea[9][1] = "StoneGroundTexture"
            if Xposition == 3 and Yposition == 1:
                addObject("upsideDownTrianglePotionTexture")
                removeObject("keyTexture")
                actualArea[1][3] = "OpenchestTexture"

 
if level == 0:
    Xposition = (maxX-13)//2
    Yposition = (maxY)//2
elif level == 1:
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
