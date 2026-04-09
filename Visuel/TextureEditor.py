
from Visuel.FloatLoop import *
from tkinter import *
from json import *
from Visuel.PrintThings import *
from File import *
#from texturePack import *

isOpen = False
actualColor = black
isAdmin = True
tool = "Pinceau"

listTexture = [[]]
for nameTexture in matchTexture.keys() :
  if len(listTexture[-1]) < 3 :
    listTexture[-1].append(nameTexture)
  else :
    listTexture.append([nameTexture])
for _ in range(3-len(listTexture[-1])) :
  listTexture[-1].append("void")
page = floatLoop(0,0,len(listTexture)-1)

preSetColors = [topColor,middlecolor,bottomColor,black,white,red,purple,gold]
pastColors = File(7)

def printEditor(screen,screenWidth,screenHeight) :
  # Bandeau supérieur
  crossWidth = screenHeight//10
  screen.create_rectangle(0,0,screenWidth,crossWidth,width = 0,fill = topColor)
  screen.create_rectangle(0,screenHeight//4,screenWidth,screenHeight,width = 0,fill = bottomColor)
  screen.create_rectangle(0,screenHeight//10,screenWidth,screenHeight//4,width = 3,fill = middlecolor)
  screen.create_line(screenWidth//2,screenHeight//10,screenWidth//2,screenHeight//4,fill = black,width = 3)
  quartWidth = screenWidth//4
  wideness = screenWidth//10
  beforLine,afterLine = quartWidth - wideness,quartWidth + wideness
  #screen.create_line(screenWidth//4-wideness,screenWidth//4+wideness)
  #Croix pour retourner
  screen.create_rectangle(screenWidth - crossWidth,0,screenWidth,crossWidth,width = 1,fill = red)
  screen.create_line(screenWidth - crossWidth*0.9,crossWidth*0.1,screenWidth - crossWidth*0.1,crossWidth*0.9,fill = white,width = 3)
  screen.create_line(screenWidth - crossWidth*0.1,crossWidth*0.1,screenWidth - crossWidth*0.9,crossWidth*0.9,fill = white,width = 3)

  # Textures à éditer
  quartScreen = screenHeight//4
  for indexTexture in [0,1,2] :
    printThings(screen,matchTexture[listTexture[page.getValue()][indexTexture]],quartScreen//2,1,(indexTexture+1.25)*2)#(0.1+indexTexture)*quartScreen)
  
  # Les Boutons pour éditer
  listText = ["Editer","Restaurer"]
  for i in [0,1] :
    for j in [1,2,3] :
      screen.create_rectangle((0.45+0.3*i)*screenWidth,(0.2+j)*quartScreen,(0.65+0.3*i)*screenWidth,(0.8+j)*quartScreen,fill = middlecolor,width = 0)
      screen.create_text(screenWidth*(i*0.3+0.55),(0.5+j)*quartScreen,text = listText[i],font = ("Verdana",15))

def clickedEditor(screen,Xaxe,Yaxe,screenWidth,screenHeight) :
  quartScreen = screenHeight//4
  if Yaxe < screenHeight//10 :
    if screenWidth-Xaxe < screenHeight//10 :
      return "Resume"
  else :
    if Yaxe < quartScreen :
      global page
      if Xaxe < screenWidth/2 :
        page = page - 1
      else :
        page = page + 1
      printEditor(screen,screenWidth,screenHeight)
    else :
      Yindex = Yaxe//quartScreen
      match (Yindex) :
        case 1 :
          Yposition = Yaxe - quartScreen
        case 2 :
          Yposition = Yaxe - quartScreen*2
        case 3 :
          Yposition = Yaxe - quartScreen*3
      if Yposition > quartScreen*0.2 and Yposition < quartScreen*0.8 :
        Xratio = Xaxe/screenWidth
        if Xratio > 0.45 :
          if Xratio > 0.65 :
            if Xratio > 0.75 and Xratio < 0.95 :
              textureName = listTexture[page.getValue()][Yindex-1]
              if textureName != "void" :
                restoreOldTexture(textureName)
          else :
            textureName = listTexture[page.getValue()][Yindex-1]
            if textureName != "void" :
              printEditTexture(screen,screenHeight,textureName,matchTexture[textureName])
 
def printEditTexture(window,screenHeight,textureName,texture) :
  global popup
  def editTextureLink(event) :
    editTexture(event,editCanva,popupSize,textureName,texture)

  popupSize = (screenHeight*4)//5
  quartPopupSize = popupSize//4
  popup = Toplevel(window)
  popup.geometry(str(popupSize)+"x"+str(popupSize))
  editCanva = Canvas(popup,width = popupSize,height = popupSize,bg = "#D1C97B")
  editCanva.create_rectangle(0,0,popupSize,popupSize//4,width = 0,fill = middlecolor)
  printEditColors(editCanva,popupSize)
  printProjectedTexture(editCanva,quartPopupSize,texture)
  editCanva.place(x = 0,y = 0)
  editCanva.bind("<Button-1>",editTextureLink)
  printTools(editCanva,quartPopupSize)
  
def printTools(canva,quartPopupSize) :
  listButton = ["Pinceau","Pipette","Gomme","Sauvegarder"]
  for i in range(4) :
    fillColor = topColor
    if tool == listButton[i] :
      fillColor = middlecolor
    canva.create_rectangle(3*quartPopupSize,(1.25+i*0.7)*quartPopupSize,3.5*quartPopupSize,(1.65+i*0.7)*quartPopupSize,fill = fillColor,width = 0)
    canva.create_text(3.25*quartPopupSize,(1.45+i*0.7)*quartPopupSize,text = listButton[i])

def printEditColors(canva,canvaSize) :
  pixelColorSize = canvaSize/20
  canva.create_rectangle(pixelColorSize,pixelColorSize,pixelColorSize*4,pixelColorSize*4,width = 3,fill = actualColor)
  for i in range(7) :
    canva.create_rectangle(pixelColorSize*(2*i+5),pixelColorSize,pixelColorSize*(2*i+6),pixelColorSize*2,width = 2,fill = preSetColors[i])
  listPastColors = pastColors.getValues()
  for j in range(len(listPastColors)) :
    canva.create_rectangle(pixelColorSize*(2*j+5),pixelColorSize*3,pixelColorSize*(2*j+6),pixelColorSize*4,width = 2,fill = listPastColors[j])
  searchTexture = [
    [None,None,None,None,None,None,None,None,None],
    [None,None,None,None,black,black,None,None,None],
    [None,None,None,black,None,None,black,None,None],
    [None,None,None,black,None,None,black,None,None],
    [None,None,black,black,black,black,None,None,None],
    [None,black,black,black,None,None,None,None,None],
    [None,black,black,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None]
  ]
  printThings(canva,searchTexture,pixelColorSize,17,3)

def editTexture(event,canva,screenSize,textureName,texture) :
  Xposition = event.x
  Yposition = event.y
  quartSize = screenSize//4
  global actualColor
  global tool
  if Yposition < quartSize : #Quart supérieur de la popup
    pixelColorSize = quartSize/5
    if Yposition//pixelColorSize == 1 :
      colorList = preSetColors
    elif Yposition//pixelColorSize == 3 :
      colorList = pastColors.getValues()
    else :
      return
    try :
      match Xposition//pixelColorSize :
        case 5 :
          actualColor = colorList[0]
        case 7 :
          actualColor = colorList[1]
        case 9 :
          actualColor = colorList[2]
        case 11 :
          actualColor = colorList[3]
        case 13 :
          actualColor = colorList[4]
        case 15 :
          actualColor = colorList[5]
        case 17 :
          def changeColor() :
            global actualColor
            actualColor = "#" + askColor.get()
            popupAskColor.destroy()
          popupAskColor = Toplevel(popup)
          askColor = Entry(popupAskColor)
          sendButton = Button(popupAskColor,text = "send",command = changeColor )
          askColor.pack()
          sendButton.pack()
          #actualColor = colorList[6]
    except IndexError :
      pass
    if not(actualColor in pastColors.getValues()) :
      pastColors.push(actualColor)
    printEditColors(canva,screenSize)
  else :
    Yposition -= quartSize
    if (Xposition > 0.5*quartSize and Xposition < 2.5*quartSize) and (Yposition > 0.5*quartSize and Yposition < 2.5*quartSize):
      pixelSize = (2*quartSize)/8
      Xindex = int((Xposition - 0.5*quartSize)//pixelSize)
      Yindex = int((Yposition - 0.5*quartSize)//pixelSize)
      match tool :
        case "Pinceau" :
          texture[Yindex][Xindex] = actualColor
          printProjectedTexture(canva,quartSize,texture)
        case "Pipette" :
          if texture[Yindex][Xindex] == None :
            return
          actualColor = texture[Yindex][Xindex]
          if not(actualColor in pastColors.getValues()) :
            pastColors.push(actualColor)
          tool = "Pinceau"
          printTools(canva,quartSize)
          printEditColors(canva,screenSize)
        case "Gomme" :
          texture[Yindex][Xindex] = None
          printProjectedTexture(canva,quartSize,texture)
    elif (Xposition > 3*quartSize and Xposition < 3.5*quartSize) :
      if Yposition > 0.25*quartSize and Yposition < 0.65*quartSize :
        tool = "Pinceau"
        printTools(canva,quartSize)
      elif Yposition > 0.95*quartSize and Yposition < 1.35*quartSize :
        tool = "Pipette"
        printTools(canva,quartSize)
      elif Yposition > 1.65*quartSize and Yposition < 2.05*quartSize :
        tool = "Gomme"
        printTools(canva,quartSize)
      elif Yposition > 2.35*quartSize and Yposition < 2.75*quartSize :
        saveTexture(textureName,texture)
        popup.destroy()

def printProjectedTexture(canva,quartSize,texture) :
  canva.create_rectangle(0.25*quartSize,1.25*quartSize,2.75*quartSize,3.75*quartSize,width = 3,fill = lightGrey)
  printThings(canva,texture,2*quartSize,0.25,0.75)

def saveTexture(textureName,texture) :
  with open("PlayersTextures.json","r") as textureBase :
    dicTexture = load(textureBase)
  dicTexture[textureName] = texture
  with open("PlayersTextures.json","w") as textureBase :
    dump(dicTexture,textureBase,indent = 4)
  if isAdmin :
    with open("DefaultTexture.json","w") as textureBase :
      dump(dicTexture,textureBase,indent = 4)

def restoreOldTexture(textureName) :
  with open("DefaultTexture.json","r") as textureBase :
    dicTexture = load(textureBase)
  global matchTexture
  matchTexture[textureName] = dicTexture[textureName]
  with open("PlayersTextures.json","w") as textureBase :
    dump(matchTexture,textureBase,indent = 4)

if __name__ == "__main__" :

  def clickedEditorLink(event) :
    if clickedEditor(testCanva,event.x,event.y,canvaWidth,canvaHeight) == "Resume" :
      testWindow.destroy()

  testWindow = Tk()
  testWindow.title("Test Donjon")
  canvaHeight = 500
  canvaWidth = 500
  testWindow.geometry(str(canvaWidth)+"x"+str(canvaHeight))
  testWindow.config(bg = "#888888")
  testCanva = Canvas(testWindow,height = canvaHeight,width = canvaWidth,bg = "#D1C97B")
  testCanva.place(x = 0,y = 0)
  printEditor(testCanva,canvaWidth,canvaHeight)
  testCanva.bind("<Button-1>", clickedEditorLink )

  testWindow.mainloop()