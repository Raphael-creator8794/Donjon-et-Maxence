#Maxence FERTRE

from json import *
from TexturePack import *

whiteTexture = [
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], 
    ['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF']
]

with open("DefaultTexture.json","r") as dataBase :
    dicTexture = load(dataBase)

dicTexture["stairsTexture"] = [
    ["#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C"],
    ["#3E2A1C", "#D8A76F", "#D8A76F", "#D8A76F", "#D8A76F", "#D8A76F", "#D8A76F", "#3E2A1C"],
    ["#3E2A1C", "#D8A76F", "#3E2A1C", "#D8A76F", "#D8A76F", "#D8A76F", "#D8A76F", "#3E2A1C"],
    ["#3E2A1C", "#D8A76F", "#3E2A1C", "#E6B980", "#E6B980", "#E6B980", "#E6B980", "#3E2A1C"],
    ["#3E2A1C", "#D8A76F", "#3E2A1C", "#E6B980", "#3E2A1C", "#E6B980", "#E6B980", "#3E2A1C"],
    ["#3E2A1C", "#D8A76F", "#3E2A1C", "#E6B980", "#3E2A1C", "#F2C995", "#F2C995", "#3E2A1C"],
    ["#3E2A1C", "#D8A76F", "#3E2A1C", "#E6B980", "#3E2A1C", "#F2C995", "#3E2A1C", "#3E2A1C"],
    ["#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C", "#3E2A1C"]
]


with open("DefaultTexture.json","w") as dataBase :
    dump(dicTexture,dataBase,indent = 4)

with open("PlayersTextures.json","w") as dataBase :
    dump(dicTexture,dataBase,indent = 4)