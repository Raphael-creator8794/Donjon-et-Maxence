#Quoicoubesque group
from Visuel.PrintThings import *
from Visuel.TexturePack import *
from time import time
from tkinter import *

delay = 0.001
nbPoint = 20
black = "#000000"
backgroundColor = "#D2DF89"

'''----- transDown -----------
> -- Objectif -- :
    Afficher une animation sur un canva, celle ci est orienté vers le bas
> -- Paramètre -- :
    screen : /Canvas/ Le canva sur lequel on affiche l'animation
    screenWidth : /int/ Largeur du canva
    screenHeight : /int/ Hauteur du canva
> -- Retourne -- :
    Rien
'''
def transDown(screen,screenWidth,screenHeight) :
    token = 0 # Initialisation de la ligne de transition à 0
    lastCall = time()
    # nbPoint est une contante définit au début du programme pour désigner le nombre de carrées utiliser pour la transition
    amplitude = screenHeight // nbPoint # Représente la hauteur des carrés
    wideness = screenWidth // nbPoint # Représente la largeurs des carrés
    while token < 20 :
        now = time()
        # On attend le moment venu pour afficher les carrées
        if now - lastCall > delay :
            lastCall = now
            for i in range(nbPoint) :
                # On créer une ligne de carré plein (un gros trait quoi)
                screen.create_rectangle(wideness*i,token*amplitude,wideness*(i+1),(token+1)*amplitude,fill = black)
                # Puis une ligne en avance on creer des carrées avec 30% (2*15%) en moins de taille
                screen.create_rectangle(wideness*(i+0.15),(token+1.15)*amplitude,wideness*(i+0.85),(token+1.85)*amplitude,fill = black)
                # Et enfin une dernière ligne avec 2 lignes d'avance avec 50% (2*25%) en moins de taille
                screen.create_rectangle(wideness*(i+0.25),(token+2.25)*amplitude,wideness*(i+0.75),(token+2.75)*amplitude,fill = black)
            screen.update_idletasks() # On réactualise le fenetre pour afficher les carrées créé
            token += 1 # Prochaine ligne
    screen.delete("all")

'''----- transUp -----------
> -- Objectif -- :
    Afficher une animation sur un canva, celle ci est orienté vers le haut
> -- Paramètre -- :
    screen : /Canvas/ Le canva sur lequel on affiche l'animation
    screenWidth : /int/ Largeur du canva
    screenHeight : /int/ Hauteur du canva
> -- Retourne -- :
    Rien
'''
def transUp(screen,screenWidth,screenHeight) :
    token = 20
    lastCall = time()
    amplitude = screenHeight // nbPoint
    wideness = screenWidth // nbPoint
    while token >= 0 :
        now = time()
        if now - lastCall > delay :
            lastCall = now
            for i in range(nbPoint) :
                screen.create_rectangle(wideness*i,token*amplitude,wideness*(i+1),(token+1)*amplitude,fill = black)
                screen.create_rectangle(wideness*(i+0.15),(token-1.15)*amplitude,wideness*(i+0.85),(token-1.85)*amplitude,fill = black)
                screen.create_rectangle(wideness*(i+0.25),(token-2.25)*amplitude,wideness*(i+0.75),(token-2.75)*amplitude,fill = black)
            screen.update_idletasks()
            token -= 1
    screen.delete("all")

'''----- transLeft -----------
> -- Objectif -- :
    Afficher une animation sur un canva, celle ci est orienté vers la gauche
> -- Paramètre -- :
    screen : /Canvas/ Le canva sur lequel on affiche l'animation
    screenWidth : /int/ Largeur du canva
    screenHeight : /int/ Hauteur du canva
> -- Retourne -- :
    Rien
'''
def transLeft(screen,screenWidth,screenHeight) :
    token = 20
    lastCall = time()
    amplitude = screenHeight // nbPoint
    wideness = screenWidth // nbPoint
    while token >= 0 :
        now = time()
        if now - lastCall > delay :
            lastCall = now
            for i in range(nbPoint) :
                screen.create_rectangle(wideness*token,amplitude*i,wideness*(token+1),amplitude*(i+1),fill = black)
                screen.create_rectangle(wideness*(token-1.15),amplitude*(i+0.15),wideness*(token-1.85),amplitude*(i+0.85),fill = black)
                screen.create_rectangle(wideness*(token-2.25),amplitude*(i+0.25),wideness*(token-2.75),amplitude*(i+0.75),fill = black)
            screen.update_idletasks()
            token -= 1
    screen.delete("all")

'''----- transRight -----------
> -- Objectif -- :
    Afficher une animation sur un canva, celle ci est orienté vers la droite
> -- Paramètre -- :
    screen : /Canvas/ Le canva sur lequel on affiche l'animation
    screenWidth : /int/ Largeur du canva
    screenHeight : /int/ Hauteur du canva
> -- Retourne -- :
    Rien
'''
def transRight(screen,screenWidth,screenHeight) :
    token = 0
    lastCall = time()
    amplitude = screenHeight // nbPoint
    wideness = screenWidth // nbPoint
    while token < 20 :
        now = time()
        if now - lastCall > delay :
            lastCall = now
            for i in range(nbPoint) :
                screen.create_rectangle(wideness*token,amplitude*i,wideness*(token+1),amplitude*(i+1),fill = black)
                screen.create_rectangle(wideness*(token+1.15),amplitude*(i+0.15),wideness*(token+1.85),amplitude*(i+0.85),fill = black)
                screen.create_rectangle(wideness*(token+2.25),amplitude*(i+0.25),wideness*(token+2.75),amplitude*(i+0.75),fill = black)
            screen.update_idletasks()
            token += 1
    screen.delete("all")

'''----- printArea -----------
> -- Objectif -- :
    Afficher la zone de façon progressive
> -- Paramètre -- :
    screen : /Canvas/ Le canva sur lequel on affiche la zone
    areaBlocks : /list/ La liste des blocks dans la zone
    maxX : /int/ Le nombre de block dans la largeur
    maxY : /int/ Le nombre de block dans la hauteur
    divisionSize : /int/ La taille du block
> -- Retourne -- :
    Rien
'''
def printArea(screen,areaBlocks,objects,maxX,maxY,divisionSize,animation = True) :
    delay = 0.000
    for i in range(maxY) :
        Jrange = list(range(maxX))
        if ((-1)**i) == -1 :
            Jrange = Jrange[::-1]
        lastCall = time()
        for j in Jrange :
            while (time() - lastCall < delay) :
                # On attend d'avoir attendu assez longtemps
                continue
            printThings(screen,areaBlocks[i][j],divisionSize,j,i)
            if objects[i][j] != None :
                printThings(screen,objects[i][j],divisionSize,j,i)
            lastCall = time()
            if animation :
                screen.update_idletasks()

def launchLeftSpears(screen,divisionSize,area) :
    printThings(screen,"brickWallHoleSpearleft",divisionSize,15,5)
    printThings(screen,"brickWallHoleSpearleft",divisionSize,15,6)
    for i in range(13) :
        lastCall = time()
        while time() < lastCall + 0.01 :
            pass
        printThings(screen,area[5][14-i],divisionSize,14-i,5)
        printThings(screen,area[6][14-i],divisionSize,14-i,6)
        printThings(screen,"spearHorizontalTexture",divisionSize,14-i,5)
        printThings(screen,"spearHorizontalTexture",divisionSize,14-i,6)
        printThings(screen,"spearPointLeftTexture",divisionSize,13-i,5)
        printThings(screen,"spearPointLeftTexture",divisionSize,13-i,6)
        screen.update_idletasks()

def retractLeftSpears(screen,divisionSize,area) :
    for i in range(14) :
        lastCall = time()
        while time() < lastCall + 0.1 :
            pass
        printThings(screen,"spearPointLeftTexture",divisionSize,1+i,5)
        printThings(screen,"spearPointLeftTexture",divisionSize,1+i,6)
        printThings(screen,area[5][i],divisionSize,i,5)
        printThings(screen,area[6][i],divisionSize,i,6)
        screen.update_idletasks()

def printBridge(screen,divisionSize,actualArea,indexBridge) :
    Xorigin = indexBridge*4 + 1
    for i in range(3) :
        for j in range(2) :
            lastCall = time()
            while time() < lastCall + 0.1 :
                pass
            actualArea[9+j][Xorigin+i] = "roofTexture"
            printThings(screen,"roofTexture",divisionSize,Xorigin+i,9+j)
            screen.update_idletasks()

if __name__ == "__main__" :

    def transDownTest() :
        transDown(testCanva,canvaWidth,canvaHeight)
        #testCanva.delete("all")

    testWindow = Tk()
    testWindow.title("Test Donjon")
    testWindow.geometry("500x500")
    testWindow.config(bg = "#888888")
    canvaHeight = 400
    canvaWidth = 400
    testCanva = Canvas(testWindow,height = canvaHeight,width = canvaWidth,bg = backgroundColor)
    testCanva.place(x = 0,y = 0)
    testButton = Button(testWindow,text = "switch",command = transDownTest)
    testButton.place(x = 400,y = 0)

    testWindow.mainloop()

