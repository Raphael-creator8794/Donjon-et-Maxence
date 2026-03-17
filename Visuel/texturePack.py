#Quoicoubesque group

glass = "#D4F6FC"
white = "#FFFFFF"
grey = "#474646"
black = "#000000"
brown = "#2E2106"
lightBrown = "#694703"
darkGreen = "#003D0F"
green = "#008132"
lightGreen = "#00BE49"
neonGreen = "#00FF00"
backgroundColor = "#D2DF89"
gold = "#F8DC0B"
orange = "#F78012"
darkRed = "#8C3113"
purple = "#440439"
darkBlue = "#2B0D71"
neonBlue = "#006EFF"
neonPurple = "#AE00FF"
neonPink = "#FF00FF"

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
    [lightGreen,lightGreen,lightGreen,green,lightGreen,lightGreen,green,lightGreen],
    [lightGreen,green,lightGreen,lightGreen,lightGreen,green,lightGreen,lightGreen],
    [lightGreen,lightGreen,green,green,lightGreen,lightGreen,lightGreen,green],
    [green,lightGreen,lightGreen,lightGreen,lightGreen,green,lightGreen,lightGreen],
    [lightGreen,lightGreen,green,lightGreen,lightGreen,lightGreen,lightGreen,lightGreen],
    [lightGreen,lightGreen,lightGreen,green,lightGreen,green,lightGreen,lightGreen],
    [lightGreen,lightGreen,lightGreen,lightGreen,lightGreen,lightGreen,green,lightGreen],
    [lightGreen,green,lightGreen,lightGreen,lightGreen,green,lightGreen,green],
]
verifTexture(grassTexture)

chestTexture =  [
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,brown,brown,brown,brown,brown,brown,None],
    [None,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,None],
    [None,gold,gold,gold,gold,gold,gold,None],
    [None,lightBrown,lightBrown,gold,gold,lightBrown,lightBrown,None],
    [None,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,lightBrown,None],
    [None,None,None,None,None,None,None,None]
]
verifTexture(chestTexture)

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
    [None,None,None,glass,glass,None,None,None],
    [None,None,glass,glass,glass,glass,None,None],
    [None,glass,neonBlue,neonBlue,neonBlue,neonBlue,glass,None],
    [None,glass,neonBlue,neonBlue,neonBlue,neonBlue,glass,None],
    [None,None,glass,neonBlue,neonBlue,glass,None,None],
    [None,None,None,glass,glass,None,None,None]
]
verifTexture(roundPotionTexture)

squarePotionTexture =  [
    [None,None,None,None,None,None,None,None],
    [None,None,None,brown,brown,None,None,None],
    [None,None,None,glass,glass,None,None,None],
    [None,glass,glass,glass,glass,glass,glass,None],
    [None,glass,neonPink,neonPink,neonPink,neonPink,glass,None],
    [None,glass,neonPink,neonPink,neonPink,neonPink,glass,None],
    [None,glass,neonPink,neonPink,neonPink,neonPink,glass,None],
    [None,glass,glass,glass,glass,glass,glass,None]
]
verifTexture(squarePotionTexture)

trianglePotionTexture =  [
    [None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None],
    [None,None,None,brown,brown,None,None,None],
    [None,None,None,glass,glass,None,None,None],
    [None,None,glass,glass,glass,glass,None,None],
    [None,glass,neonGreen,neonGreen,neonGreen,neonGreen,glass,None],
    [glass,neonGreen,neonGreen,neonGreen,neonGreen,neonGreen,neonGreen,glass],
    [glass,glass,glass,glass,glass,glass,glass,glass]
]
verifTexture(trianglePotionTexture)

upsideDownTrianglePotionTexture =  [
    [None,None,None,None,None,None,None,None],
    [None,None,None,brown,brown,None,None,None],
    [None,None,None,glass,glass,None,None,None],
    [glass,glass,glass,glass,glass,glass,glass,glass],
    [glass,neonPurple,neonPurple,neonPurple,neonPurple,neonPurple,neonPurple,glass],
    [None,glass,neonPurple,neonPurple,neonPurple,neonPurple,glass,None],
    [None,None,glass,neonPurple,neonPurple,glass,None,None],
    [None,None,None,glass,glass,None,None,None]
]
verifTexture(upsideDownTrianglePotionTexture)

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
