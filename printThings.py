#Quoicoubesque group
from tkinter import *
from random import randint

backgroundColor = "#D2DF89"
black = "#000000"
white = "#FFFFFF"
purple = "#440439"
orange = "#F78012"
lightGreen = "#00BE49"
green = "#008132"
darkGreen = "#003D0F"
brown = "#2E2106"

#--- Main Function ----------------------------------------------------------------------
def printThings(screen,pixelGrid,divisionSize,Xindex,Yindex) :
    pixelSize = divisionSize//8
    for i in range(8) :
        for j in range(8) :
            if pixelGrid[i][j] == None :
                continue
            else :
                screen.create_rectangle(Xindex*divisionSize+j*pixelSize,Yindex*divisionSize+i*pixelSize,Xindex*divisionSize+(j+1)*pixelSize,Yindex*divisionSize+(i+1)*pixelSize,width = 0,fill = pixelGrid[i][j])

if __name__ == "__main__" :

    def testPrintThings() :
        printThings(testCanva,testPlayer,50,randint(0,7),randint(0,7))

    testPlayer = [
        [None,None,None,None,None,None,None,None],
        [None,None,black,black,black,black,None,None],
        [None,black,black,orange,orange,black,black,None],
        [None,black,orange,orange,orange,orange,black,None],
        [None,None,purple,purple,purple,purple,None,None],
        [None,purple,None,purple,purple,None,purple,None],
        [None,None,None,purple,purple,None,None,None],
        [None,None,purple,None,None,purple,None,None]
    ]
    testWindow = Tk()
    testWindow.title("Test Donjon")
    testWindow.geometry("500x500")
    testWindow.config(bg = "#888888")
    canvaHeight = 400
    canvaWidth = 400
    testCanva = Canvas(testWindow,height = canvaHeight,width = canvaWidth,bg = backgroundColor)
    testCanva.place(x = 0,y = 0)
    testButton = Button(testWindow,text = "switch",command = testPrintThings)
    testButton.place(x = 400,y = 0)
    testWindow.mainloop()