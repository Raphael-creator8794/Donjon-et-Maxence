#Quoicoubesque group
#modif test
notDefined = True
if notDefined :
    notDefined = False
    from tkinter import *
    from Visuel.Transition import *
    from Visuel.PrintThings import *
    from Visuel.TexturePack import *
    from Visuel.TextureEditor import *
    from Visuel.PrintMap import *
    from Inventory import *
    from Movement import *
    import json

# Global variable
screenWidth = 800
screenHeight = 600
divisionSize = 50
maxX = screenWidth//divisionSize
maxY = screenHeight//divisionSize
backgroundColor = "#D2DF89"
state = "menu"
Xposition = (maxX-1)//2
Yposition = (maxY-1)//2
iClicked = False
level = 0
actualRoom = 4

if __name__ == "__main__" :

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

    def printStart() :
        global actualArea
        global objects
        global level
        global actualMap
        global actualRoom
        with open("Levels.json","r") as datas :
            levelDatas = load(datas)[level]
        actualArea = levelDatas[actualRoom]["area"]
        objects = levelDatas[actualRoom]["objects"]
        objects[3][3] = "crateTexture"
        actualMap = levelDatas[actualRoom]
        printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
        printThings(screen,playerTexture,divisionSize,(maxX-1)//2,(maxY-1)//2)

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
                            transDownLink()
                            printEditor(screen,screenWidth,screenHeight)
                        case 12 :
                            window.destroy()
                            state = "exit"
            case "play" :
                if Xaxe < screenWidth/10 and Yaxe < screenHeight/10 :
                    printMap(screen,screenWidth,screenHeight,roomsToMap(actualMap))
            case "settings" :
                if clickedEditor(screen,Xaxe,Yaxe,screenWidth,screenHeight) == "Resume" :
                    printMenu(screen,screenWidth,screenHeight)
                    state = "menu"

    def keySituation(event) :
        global Xposition
        global Yposition
        global actualArea
        global objects
        global iClicked
        global level
        if state == "play":
            pressedKey = str(repr(event.char)).lower()
            if pressedKey == "'i'" :
                iClicked = not(iClicked)
                seeInventory(window, iClicked)
            else :
                moveDir(screen,pressedKey,actualArea,objects)

    def printHey() :
        print("Hey !")

    window = Tk()
    window.title("Donjon")
    window.geometry(str(screenWidth)+"x"+str(screenHeight))
    window.config(bg = "#888888")

    screen = Canvas(window,height = screenHeight,width = screenWidth,bg = backgroundColor)
    screen.place(x = 0,y = 0)
    screen.delete("all")
    printMenu(screen,screenWidth,screenHeight)
    screen.bind("<Button-1>", clickSituation )
    screen.bind("<Button-2>", printHey)
    window.bind("<Key>", keySituation )
    window.mainloop()
