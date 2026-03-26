#Quoicoubesque group
#modif test
notDefined = True
if notDefined :
    notDefined = False
    from tkinter import *
    from Visuel.Transition import *
    from Visuel.PrintThings import *
    from Visuel.TexturePack import *
    from Inventory import *
    from Visuel.TextureEditor import *
    from Mouvement import *
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
level = 1
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

    def printStart() :
        global startArea
        global level
        startArea = [[grassTexture for _ in range(maxX)] for _ in range(maxY)]
        #createCarpet(startArea, 8, 8, 10, 11, darkBlue)
        #modifierjson("Jeu.json",3,2,{"squarePotionTexture":True},str(level))
        printArea(screen,startArea,maxX,maxY,divisionSize)
        with open("Jeu.json","r",encoding="utf-8") as fichier:
            dict = json.load(fichier)
            le_niveaux = dict[str(level)]
            for ligne in range(len(le_niveaux)):
                for dico in range(len(le_niveaux[ligne])):
                    for texture in le_niveaux[ligne][dico]:
                        if texture != "grassTexture":
                            printThings(screen,matchTexture[texture],divisionSize,dico,ligne)
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
                            transDownLink()
                            printEditor(screen,screenWidth,screenHeight)
                        case 12 :
                            window.destroy()
                            state = "exit"
            case "play" :
                pass #arrowMove(event)
            case "settings" :
                if clickedEditor(screen,Xaxe,Yaxe,screenWidth,screenHeight) == "Resume" :
                    printMenu(screen,screenWidth,screenHeight)
                    state = "menu"

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
                            modifierjson("Jeu.json",Yposition-2,Xposition,{list(le_niveau[Yposition-1][Xposition])[0] : True},str(level))
                            modifierjson("Jeu.json",Yposition-1,Xposition,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
                            printThings(screen,squarePotionTexture,divisionSize,Xposition,Yposition-2)
                            printThings(screen,grassTexture,divisionSize,Xposition,Yposition-1)
                        move("up",Xposition,Yposition, startArea)
                        Yposition -= 1
                if dir == "'q'":
                    if Xposition > 0 and colision(level)[1] is True:
                        if deplacable(level)[1]:
                            modifierjson("Jeu.json",Yposition,Xposition-2,{list(le_niveau[Yposition][Xposition-1])[0]: True},str(level))
                            modifierjson("Jeu.json",Yposition,Xposition-1,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
                            printThings(screen,squarePotionTexture,divisionSize,Xposition-2,Yposition)
                            printThings(screen,grassTexture,divisionSize,Xposition-1,Yposition)
                        move("left",Xposition,Yposition, startArea)
                        Xposition -= 1
                if dir == "'s'":
                    if Yposition < maxY-1 and colision(level)[2] is True:
                        if deplacable(level)[2] is True:
                            modifierjson("Jeu.json",Yposition+2,Xposition,{list(le_niveau[Yposition+1][Xposition])[0]: True},str(level))
                            modifierjson("Jeu.json",Yposition+1,Xposition,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
                            printThings(screen,squarePotionTexture,divisionSize,Xposition,Yposition+2)
                            printThings(screen,grassTexture,divisionSize,Xposition,Yposition+1)
                        move("down",Xposition,Yposition, startArea)
                        Yposition += 1
                if dir == "'d'":
                    if Xposition < maxX-1 and colision(level)[0] is True:
                        if deplacable(level)[0] is True:
                            for cle in le_niveau[Yposition][Xposition+2].keys():
                                modifierjson("Jeu.json",Yposition,Xposition+2,{list(le_niveau[Yposition][Xposition+1])[0]: True},str(level))
                            modifierjson("Jeu.json",Yposition,Xposition+1,{list(le_niveau[Yposition][Xposition])[0]: False},str(level))
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
