#Quoicoubesque group
from printThings import printThings
from texturePack import *
from time import time
from tkinter import *

delay = 0.01
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
def printArea(screen,areaBlocks,maxX,maxY,divisionSize) :
    delay = 0
    for i in range(maxY) :
        Jrange = list(range(maxX))
        if ((-1)**i) == -1 :
            Jrange = Jrange[::-1]
        for j in Jrange :
            lastCall = time()
            while (time() - lastCall < delay) :
                # On attend d'avoir attendu assez longtemps
                continue
            printThings(screen,areaBlocks[i][j],divisionSize,j,i)
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

