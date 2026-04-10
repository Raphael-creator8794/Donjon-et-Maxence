

# Importations
notDefined = True
if notDefined :
    notDefined = False
    from tkinter import *
    from Visuel.Transition import *
    from Visuel.PrintThings import *
    from Visuel.TexturePack import *
    from Visuel.TextureEditor import *
    from Inventory import *
    from Movement import *


# Variables globales
screenWidth = 800
screenHeight = 600
divisionSize = 50
maxX = screenWidth//divisionSize
maxY = screenHeight//divisionSize
state = "menu"
iClicked = False

if __name__ == "__main__" :

# Fonction de tranistions visuels
    def transDownLink() :
        transDown(screen,screenWidth,screenHeight)

    def transUpLink() :
        transUp(screen,screenWidth,screenHeight)

    def transLeftLink() :
        transLeft(screen,screenWidth,screenHeight)

    def transRightLink() :
        transRight(screen,screenWidth,screenHeight)


    def printStart() :        
        """
        Cette fonction permet d'afficher le niveau voulu sur l'écran
        On distingue l'area, la zone au sols, les objets qui constitus tout ce qui va être intéractif, et les tapis qui sont des éléments de décors
        """
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


    def clickSituation(event) :
        """
        Cette fonction est une machine d'état qui permet la gestion du menu
        """
        Xaxe = event.x
        Yaxe = event.y
        global state
        global startArea
        global objects
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
                            state = "editor"
                            transDownLink()
                            printEditor(screen,screenWidth,screenHeight)
                        case 12 :
                            window.destroy()
                            state = "exit"
            case "play" :
                Yindex = int(((Yaxe/screenHeight)*maxY)//1)
                Xindex = int(((Xaxe/screenWidth)*maxX)//1)
                if objects[Yindex][Xindex] == "treeTexture" :
                    for i in [2,9] :
                        for j in range(8,16) :
                            objects[i][j] = None
                            printThings(screen,actualArea[i][j],divisionSize,j,i)
                    objects[2][9] = "torchOffTexture"
                    objects[9][9] = "torchOffTexture"
                    printThings(screen,"torchOffTexture",divisionSize,9,2)
                    printThings(screen,"torchOffTexture",divisionSize,9,9)
            case "editor" :
                if clickedEditor(screen,Xaxe,Yaxe,screenWidth,screenHeight) == "Resume" :
                    state = "menu"
                    printMenu(screen,screenWidth,screenHeight)


    def keySituation(event) :
        """
        Cette fonction permet de lancer le jeu et d'initialiser les fonctions liés au gameplay
        """
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
        """
        Cette fonction, dont la complexité est d'une rare violence, affiche "Hey" dans le terminal 
        (Très utile pour faire des print espions)
        """
        print("Hey !")


# Initialisations des fenêtres Tkinter
    window = Tk()
    window.title("Donjon")
    window.geometry(str(screenWidth)+"x"+str(screenHeight))
    window.config(bg = "#888888")

    screen = Canvas(window,height = screenHeight,width = screenWidth,bg = black)
    screen.place(x = 0,y = 0)
    printMenu(screen,screenWidth,screenHeight)
    screen.bind("<Button-1>", clickSituation )
    screen.bind("<a>", printHey)
    window.bind("<Key>", keySituation )
    window.mainloop()
