#Quoicoubesque group
from printThings import *

def verifTexture(texture) :
    if type(texture) != list :
        raise Exception("Is not a list")
    elif len(texture) != 8 :
        raise Exception("Havn't 8 row")
    else :
        for i in range(8) :
            if type(texture[i]) != list : 
                raise Exception("Row " + str(i) + " isn't a list")
            elif len(texture[i]) != 8 :
                raise Exception("Havn't 8 square at row " + str(i))
            else :
                for j in range(8) :
                    if texture[i][j] == None :
                        continue
                    else :
                        if type(texture[i][j]) != str :
                            raise TypeError("Unvalid type of the square "+str(j)+" at row "+str(i))
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

crateTexture =  [
    [None,None,None,None,None,None,None,None],
    [None,None,green,green,green,green,green,None],
    [None,green,brown,brown,brown,green,green,None],
    [green,green,green,green,green,brown,green,None],
    [green,green,brown,green,green,brown,green,None],
    [green,brown,green,brown,green,brown,green,None],
    [green,green,brown,green,green,green,None,None],
    [green,green,green,green,green,None,None,None]
]
verifTexture(crateTexture)

matchTexture = {
    "grass" : grassTexture
}