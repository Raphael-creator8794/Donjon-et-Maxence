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
    from CreateComments import *

# Global variable
screenWidth = 800
screenHeight = 600
bannerWidth = int((screenWidth*0.3)//1)
divisionSize = 50
maxX = screenWidth//divisionSize
maxY = screenHeight//divisionSize
state = "menu"
iClicked = False

"""def refresh() :
    window.update_idletasks()"""

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
        
        if level == 0:
            createCarpet(actualArea,10,4,13,7,darkBlue)
            createCarpet(actualArea,11,5,12,6,red)
            printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
            printThings(screen,playerTexture,divisionSize,(maxX-13)//2,(maxY)//2)
        elif level == 1:
            printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
            printThings(screen,playerTexture,divisionSize,(maxX-13)//2,(maxY)//2)
        elif level == 2:
            printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
            printThings(screen,playerTexture,divisionSize,(maxX-15)//2,(maxY)//2)
        elif level == 3:
            printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
            printThings(screen,playerTexture,divisionSize,(maxX-15)//2,(maxY)//2)
        elif level == 4:
            printArea(screen,actualArea,objects,maxX,maxY,divisionSize)
            printThings(screen,playerTexture,divisionSize,(maxX-15)//2,(maxY)//2)

    def printSettings() :
        screen.delete("all")
        screen.create_rectangle(0,0,screenWidth,screenHeight//4,fill=orange)

    def clickSituation(event) :
        Xaxe = event.x
        Yaxe = event.y
        global state
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
                return
                if Xaxe < screenWidth/10 and Yaxe < screenHeight/10 :
                    printMap(screen,screenWidth,screenHeight,roomsToMap(levelDatas))
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
                moveDir(screen,pressedKey,screenWidth,screenHeight)

    def printHey(event = None) :
        print("Hey !")

    def addAie(event) :
        addComment(commentBanner,"Aïe")

    window = Tk()
    window.title("Donjon")
    window.geometry(str(screenWidth+bannerWidth)+"x"+str(screenHeight))
    window.config(bg = "#888888")

    screen = Canvas(window,height = screenHeight,width = screenWidth,bg = black)
    screen.place(x = 0,y = 0)
    printMenu(screen,screenWidth,screenHeight)
    screen.bind("<Button-1>", clickSituation )
    screen.bind("<a>", printHey)
    commentBanner = Canvas(window,height = screenHeight,width = bannerWidth,bg = black)
    commentBanner.place(x = screenWidth,y = 0)
    initParametres(screenHeight,bannerWidth,20)
    commentBanner.bind("<Button-1>", addAie )
    window.bind("<Key>", keySituation )
    window.mainloop()
