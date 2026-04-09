
import json
from Donjon import maxX,maxY,divisionSize
from Visuel.PrintThings import *
from Visuel.Transition import *
from time import time
from Inventory import *
from File import*

matchPosition = [((maxX-13)//2,(maxY)//2),((maxX-13)//2,(maxY)//2),((maxX-15)//2,(maxY)//2),((maxX-15)//2,(maxY)//2)]
level = 0
nbMove = 0
lastMaxX = 7
bridge = True
traps = True
torcheoff1 = False
torcheoff2 = False
color_file = File(3)
Xposition,Yposition = matchPosition[level]

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

isMovable = ["crateTexture","torchTexture","chestTexture","stoneTexture","blueJewelTexture","greenJewelTexture","redJewelTexture","torchOffTexture"]

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
    global blueBridge
    global greenBridge
    global redBridge
    global bridge
    global lastMaxX
    
    blueBridge = True
    greenBridge = True
    redBridge = True
    bridge = True
    nbMove = 0
    nbCall = 0
    lastMaxX = 7
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

def passRoom(screen) :
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
    level += 1
    Xposition,Yposition = matchPosition[level]
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
    global lastMaxX
    global traps
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
            traps = True

    match level:
        case 0:
            global torcheoff1
            global torcheoff2
            if Xposition == 6 and Yposition == 2:
                printThings(screen,"StoneGroundTexture",divisionSize,7,5)
                printThings(screen,"StoneGroundTexture",divisionSize,7,6)
                objects[5][7] = None
                objects[6][7] = None
            if objects[9][15] == "torchOffTexture" and torcheoff1 == False:
                torcheoff1 = True
                printThings(screen,"torchTexture",divisionSize,15,9)
            if objects[2][15] == "torchOffTexture" and torcheoff2 == False:
                torcheoff2 = True
                printThings(screen,"torchTexture",divisionSize,15,2)
            if objects[9][15] == "torchOffTexture" and objects[2][15] == "torchOffTexture":
                actualArea[5][15] = "HoleUp"
                actualArea[6][15] = "Holedown"
                printThings(screen,"HoleUp",divisionSize,15,5)
                printThings(screen,"Holedown",divisionSize,15,6)
            if Xposition == 15 and (Yposition == 5 or Yposition == 6) and actualArea[5][15] == "HoleUp"and actualArea[6][15] == "Holedown":
                transDown(screen,screenWidth,screenHeight)
                passRoom(screen)
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
        case 1 :
            if actualArea[Yposition][Xposition] == "smallTorchTexture":
                addObject("smallTorchTexture")
                actualArea[Yposition][Xposition] = "StoneGroundTexture"
                
            if actualArea[Yposition][Xposition] == "greyBaseTexture":
                if findObjectIndex("smallTorchTexture"):
                    removeObject("smallTorchTexture")
                    actualArea[Yposition][Xposition] = "greyBaseFireTexture"

            if actualArea[1][6] == "greyBaseFireTexture" and actualArea[10][6] == "greyBaseFireTexture":
                if bridge:
                    for i in range (8, 15):
                        for j in range (5, 7):
                            actualArea[j][i] = "roofTexture"
                            objects[j][i] = None
                            printThings(screen, "roofTexture", divisionSize, i, j)
                            screen.update_idletasks()
                bridge = False
            if Xposition > lastMaxX :
                lastMaxX = Xposition
                lauchVerticaleSpear(screen,divisionSize,actualArea,Xposition)
            if (Xposition,Yposition) in [(8,6),(9,6),(11,5),(12,5),(14,6)] :
                respawn(screen, screenWidth, screenHeight)
            if Xposition == 15 and (Yposition == 5 or Yposition == 6):
                transDown(screen,screenWidth,screenHeight)
                passRoom(screen)
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
        case 2 :
            global nbMove
            global blueBridge
            global greenBridge
            global redBridge
            
            if Xposition == 12 and (Yposition == 6 or Yposition == 5):
                traps = False
            if traps:
                nbMove += 1
                if nbMove > 5 :
                    nbMove = 1
                if nbMove == 4 :
                    printThings(screen,"brickWallHoleArrowleft",divisionSize,15,5)
                    printThings(screen,"brickWallHoleArrowleft",divisionSize,15,6)
                if nbMove == 5:
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
                passRoom(screen)
                printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
                printThings(screen,"playerTexture",divisionSize,Xposition,Yposition)
        case 3:

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
            if Xposition == 3 and Yposition == 1 and findObjectIndex("keyTexture"):
                addObject("upsideDownTrianglePotionTexture")
                removeObject("keyTexture")
                actualArea[1][3] = "OpenchestTexture" 
            if Xposition == 12 and Yposition == 1 and findObjectIndex("upsideDownTrianglePotionTexture"):
    
                removeObject("upsideDownTrianglePotionTexture")
                actualArea[1][12] = "BreakorbTexture"
                objects[1][8] = "DragonHeadUpright"
                objects[1][7] = "DragonHeadUpleft"
                objects[2][7] = "DragonHeadDownleft"
                objects[2][8] = "DragonHeadDownright"
                objects[0][7] = "DragonHornLeft"
                objects[0][8] = "DragonHornRight"
                printThings(screen,"DragonHeadUpright",divisionSize,8,1)
                printThings(screen,"DragonHeadUpleft",divisionSize,7,1)
                printThings(screen,"DragonHeadDownleft",divisionSize,7,2)
                printThings(screen,"DragonHeadDownright",divisionSize,8,2)
                printThings(screen,"DragonHornLeft",divisionSize,7,0)
                printThings(screen,"DragonHornRight",divisionSize,8,0)
 