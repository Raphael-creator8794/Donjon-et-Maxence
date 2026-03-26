import json
from Donjon import Xposition,Yposition



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
