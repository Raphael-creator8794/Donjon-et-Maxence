#Quoicoubesque group

backgroundColor = "#D2DF89"
black = "#000000"
white = "#FFFFFF"
purple = "#440439"
orange = "#F78012"
lightGreen = "#00BE49"
green = "#008132"
darkGreen = "#003D0F"
brown = "#2E2106"
lightBrown = "#694703"
grey = "#474646"
gold = "#F8DC0B"
darkRed = "#8C3113"
darkBlue = "#2B0D71"
lightBlue = "#ABF2FF"
neonGreen = "#00FF00"
neonBlue = "#0000FF"

'''----- verifTexture -----------
> -- Objectif -- :
    Cette fonction na pas de but utile. Elle ne fais que lever une interuption dans le cas où le format ne correspond pas aux attentes.
    Est utile pour les développeur.
> -- Paramètre -- :
    texture : /list/ La grille a vérifier
> -- Retourne -- :
    Rien
'''
def verifTexture(texture) :
    if type(texture) != list :
        raise Exception("Is not a list")
    elif len(texture) != 8 :
        raise Exception("Doesn't have 8 rows")
    else :
        for i in range(8) :
            if type(texture[i]) != list : 
                raise Exception("Row " + str(i) + " isn't a list")
            elif len(texture[i]) != 8 :
                raise Exception("Doesn't have 8 squares at row " + str(i))
            else :
                for j in range(8) :
                    if texture[i][j] == None :
                        continue
                    else :
                        if type(texture[i][j]) != str :
                            raise TypeError("Unvalid type for square "+str(j)+" at row "+str(i))
                        """else :
                            if texture[i][j][0] != "#" or not(texture[i][j][1:].isdigit()) :
                                raise ValueError("Unvalid value for the square "+str(j)+" at row "+str(i)+" : "+texture[i][j])
                        """ # Ne fonctionne pas car est codé en hexadécimal

playerTexture = [
    [None,None,None,None,None,None,None,None],
    [None,None,black,black,black,black,None,None],
    [None,black,black,orange,orange,black,black,None],
    [None,black,orange,orange,orange,orange,black,None],
    [None,None,purple,purple,purple,purple,None,None],
    [None,purple,None,purple,purple,None,purple,None],
    [None,None,None,purple,purple,None,None,None],
    [None,None,purple,None,None,purple,None,None]
]
verifTexture(playerTexture)

grassTexture = [
    [lightGreen,lightGreen,lightGreen,lightGreen,lightGreen,lightGreen,green,lightGreen],
    [lightGreen,green,lightGreen,lightGreen,lightGreen,green,lightGreen,lightGreen],
    [lightGreen,lightGreen,green,lightGreen,lightGreen,lightGreen,lightGreen,green],
    [lightGreen,lightGreen,lightGreen,lightGreen,lightGreen,green,lightGreen,lightGreen],
    [brown,lightGreen,lightGreen,brown,lightGreen,lightGreen,brown,lightGreen],
    [brown,lightGreen,brown,brown,lightGreen,lightGreen,brown,brown],
    [brown,brown,brown,brown,brown,lightGreen,brown,brown],
    [brown,brown,brown,brown,brown,brown,brown,brown]
]
verifTexture(grassTexture)

crateTexture =  [
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,brown,brown,brown,brown,brown,brown,None],
    [None,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,None],
    [None,gold,gold,gold,gold,gold,gold,None],
    [None,lightBrown,lightBrown,gold,gold,lightBrown,lightBrown,None],
    [None,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,None],
    [None,None,None,None,None,None,None,None]
]
verifTexture(crateTexture)

torchTexture =  [
    [None,darkRed,None,orange,orange,None,None,darkRed],
    [None,None,orange,gold,orange,orange,None,None],
    [darkRed,None,orange,gold,gold,orange,None,None],
    [None,None,grey,grey,grey,grey,None,darkRed],
    [None,None,None,grey,grey,None,None,None],
    [None,None,None,grey,grey,None,None,None],
    [None,None,None,grey,grey,None,None,None],
    [None,None,grey,grey,grey,grey,None,None]
]
verifTexture(torchTexture)

roundPotionTexture =  [
    [None,None,None,None,None,None,None,None],
    [None,None,None,brown,brown,None,None,None],
    [None,None,None,lightBlue,lightBlue,None,None,None],
    [None,None,lightBlue,lightBlue,lightBlue,lightBlue,None,None],
    [None,lightBlue,neonGreen,neonGreen,neonGreen,neonGreen,lightBlue,None],
    [None,lightBlue,neonGreen,neonGreen,neonGreen,neonGreen,lightBlue,None],
    [None,None,lightBlue,neonGreen,neonGreen,lightBlue,None,None],
    [None,None,None,lightBlue,lightBlue,None,None,None]
]
verifTexture(roundPotionTexture)

def singleCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,gold,color],
    [gold,color,gold,gold,gold,gold,color,gold],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [gold,color,gold,gold,gold,gold,color,gold],
    [color,gold,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def leftCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,color,color],
    [gold,color,gold,gold,gold,gold,gold,gold],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [gold,color,gold,gold,gold,gold,gold,gold],
    [color,gold,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def rightCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,gold,color],
    [gold,gold,gold,gold,gold,gold,color,gold],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [gold,gold,gold,gold,gold,gold,color,gold],
    [color,color,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def topCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,gold,color],
    [gold,color,gold,gold,gold,gold,color,gold],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def bottomCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [gold,color,gold,gold,gold,gold,color,gold],
    [color,gold,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def horizontalCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,color,color],
    [gold,gold,gold,gold,gold,gold,gold,gold],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [gold,gold,gold,gold,gold,gold,gold,gold],
    [color,color,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def verticalCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color],
    [color,gold,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def middleCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def leftSideCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def rightSideCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def topSideCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,color,color],
    [gold,gold,gold,gold,gold,gold,gold,gold],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def bottomSideCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [color,color,color,color,color,color,color,color],
    [gold,gold,gold,gold,gold,gold,gold,gold],
    [color,color,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def topLeftCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,color,color],
    [gold,color,gold,gold,gold,gold,gold,gold],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def topRightCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,gold,color],
    [gold,gold,gold,gold,gold,gold,color,gold],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def bottomRightCarpet(color):
    carpetTexture =  [
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [color,color,color,color,color,color,gold,color],
    [gold,gold,gold,gold,gold,gold,color,gold],
    [color,color,color,color,color,color,gold,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture

def bottomLeftCarpet(color):
    carpetTexture =  [
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [color,gold,color,color,color,color,color,color],
    [gold,color,gold,gold,gold,gold,gold,gold],
    [color,gold,color,color,color,color,color,color]
    ]
    verifTexture(carpetTexture)
    return carpetTexture


matchTexture = {
    "grass" : grassTexture

}
