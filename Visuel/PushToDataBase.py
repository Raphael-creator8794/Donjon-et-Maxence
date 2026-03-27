#Maxence FERTRE

from json import *
from TexturePack import *
forestTexture = [[white for _ in range(8)] for _ in range(8)]


dicTexture = {
    "grassTexture" : grassTexture ,
    "playerTexture" : playerTexture ,
    "torchTexture" : torchTexture ,
    "chestTexture" : chestTexture ,
    "roundPotionTexture" : roundPotionTexture ,
    "squarePotionTexture" : squarePotionTexture ,
    "crateTexture" : crateTexture ,
    "trianglePotionTexture" : trianglePotionTexture ,
    "upsideDownTrianglePotionTexture" : upsideDownTrianglePotionTexture ,
    "forestTexture" : forestTexture ,
    "void" : [[white for _ in range(8)] for _ in range(8)]
}

with open("DefaultTexture.json","w") as dataBase :
    dump(dicTexture,dataBase,indent = 4)

with open("PlayersTextures.json","w") as dataBase :
    dump(dicTexture,dataBase,indent = 4)