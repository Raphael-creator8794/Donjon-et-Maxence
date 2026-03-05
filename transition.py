#Quoicoubesque group
from printThings import printThings
from texturePack import *
from time import time
from tkinter import *
"""from donjon import screen
from donjon import screenWidth
from donjon import screenHeight
from donjon import backgroundColor"""

delay = 0.01
nbPoint = 20
black = "#000000"
backgroundColor = "#D2DF89"

def transDown(screen,screenWidth,screenHeight) :
    token = 0
    lastCall = time()
    amplitude = screenHeight // nbPoint
    wideness = screenWidth // nbPoint
    while token < 20 :
        now = time()
        if now - lastCall > delay :
            lastCall = now
            for i in range(nbPoint) :
                screen.create_rectangle(wideness*i,token*amplitude,wideness*(i+1),(token+1)*amplitude,fill = black)
                screen.create_rectangle(wideness*(i+0.15),(token+1.15)*amplitude,wideness*(i+0.85),(token+1.85)*amplitude,fill = black)
                screen.create_rectangle(wideness*(i+0.25),(token+2.25)*amplitude,wideness*(i+0.75),(token+2.75)*amplitude,fill = black)
            screen.update_idletasks()
            token += 1

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

def printArea(screen,areaBlocks,maxX,maxY,divisionSize) :
    delay = 0
    for i in range(maxY) :
        Jrange = list(range(maxX))
        if ((-1)**i) == -1 :
            Jrange = Jrange[::-1]
        for j in Jrange :
            lastCall = time()
            while (time() - lastCall < delay) :
                continue
            printThings(screen,matchTexture[areaBlocks[i][j]],divisionSize,j,i)
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