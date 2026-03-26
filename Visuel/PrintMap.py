#

from tkinter import *
from PrintThings import *
from TexturePack import *

def roomsToMap(rooms) :
    map = [[None for _ in range(20)] for _ in range(20)]
    for i in range(len(rooms)) :
        if rooms[i]["seen"] :
            Xpos , Ypos = rooms[i]["Xpos"] , rooms[i]["Ypos"]
            for j in range(rooms[i]["height"]) :
                for y in range(rooms[i]["width"]) :
                    map[j+Ypos][y+Xpos] = i
    return map

def printMap(screen,screenWidth,screenHeight,map) :
    screen.create_rectangle(0,0,screenWidth,screenHeight,fill = black)
    minLenght = min(screenHeight,screenWidth)
    partRoomSize = minLenght/20
    for i in range(20) :
        for j in range(20) :
            if map[i][j] == None :
                continue
                #screen.create_rectangle(partRoomSize*j,partRoomSize*i,partRoomSize*(1+j),partRoomSize*(1+i),fill = black)
            else :
                partRoomTexture = [[ neonBlue for _ in range(8)] for _ in range(8)]
                actualRoom = map[i][j]
                if map[i+1][j] != actualRoom :
                    for y in range(1,7) :
                        partRoomTexture[6][y] = darkBlue
                if map[i-1][j] != actualRoom :
                    for y in range(1,7) :
                        partRoomTexture[1][y] = darkBlue
                if map[i][j+1] != actualRoom :
                    for y in range(1,7) :
                        partRoomTexture[y][6] = darkBlue
                if map[i][j-1] != actualRoom :
                    for y in range(1,7) :
                        partRoomTexture[y][1] = darkBlue
                printThings(screen,partRoomTexture,partRoomSize,j,i)

if __name__ == "__main__" :
    testLevel = [
        {
            "height" : 2 ,
            "width" : 3 ,
            "Xpos" : 1 ,
            "Ypos" : 1 ,
            "seen" : True
        } ,
        {
            "height" : 3 ,
            "width" : 1 ,
            "Xpos" : 4 ,
            "Ypos" : 1 ,
            "seen" : True
        } ,
        {
            "height" : 3 ,
            "width" : 3 ,
            "Xpos" : 1 ,
            "Ypos" : 3 ,
            "seen" : False
        } ,
        {
            "height" : 7 ,
            "width" : 7 ,
            "Xpos" : 2 ,
            "Ypos" : 4 ,
            "seen" : True
        }
    ]
    corner = False
    def switchSize(event) :
        global corner
        corner = not(corner)
        testCanva.delete("all")
        if corner :
            printMap(testCanva,canvaWidth/10,canvaHeight/10,testMap)
        else :
            printMap(testCanva,canvaWidth,canvaHeight,testMap)
    
    testMap = roomsToMap(testLevel)
    testWindow = Tk()
    testWindow.title("Test map")
    canvaHeight = 500
    canvaWidth = 500
    testWindow.geometry(str(canvaWidth)+"x"+str(canvaHeight))
    testWindow.config(bg = "#888888")
    testCanva = Canvas(testWindow,height = canvaHeight,width = canvaWidth,bg = "#D1C97B")
    testCanva.place(x = 0,y = 0)

    printMap(testCanva,canvaWidth,canvaHeight,testMap)
    testCanva.bind("<Button-1>", switchSize)
    testWindow.mainloop()