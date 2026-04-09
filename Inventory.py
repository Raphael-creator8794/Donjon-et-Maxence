#Quoicoubesque group
from tkinter import *
from Visuel.PrintThings import *
inventory = []
def seeInventory(window, iClicked):
    global inventory
    global popup
    if iClicked:
        popup = Toplevel(window)
        popup.title("Inventaire")
        popup.geometry("250x600")
        popup.config(bg = "#D6B36D")
        canvas = Canvas(popup, height = 580, width = 100, bg = "#D6B36D")
        canvas.place(x = 10, y = 10)
        yIndex = 0
        yPos = 60
        for i in inventory :
            printThings(canvas,i[0],100,0,yIndex)
            nom = Label(popup, text = i[1], font = "Verdana, 13", bg = "#D6B36D", fg = brown)
            nom.place(x = 175, y = yPos)
            yIndex += 1
            yPos += 100
    else:
        popup.destroy()

def findObjectIndex(objectTexture):
    global inventory
    for i in inventory:
        if i[0]==objectTexture:
            return i
    return None

def addObject(objectTexture):
    global inventory
    index = findObjectIndex(objectTexture)
    if index == None:
        inventory.append([objectTexture, 1])
    else : 
        index[1] += 1

def removeObject(objectTexture):
    global inventory
    index = findObjectIndex(objectTexture)
    if index == None:
        print("You can't remove something that's not here")
    else : 
        index[1] -= 1
        if index[1] == 0:
            inventory.pop(inventory.index(index))
