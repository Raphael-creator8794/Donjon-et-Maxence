#
from foatLoop import *
page = floatLoop(0,0,0)
topColor = "#CCA077"
middleColor = "#D8BF9F" #+94
dictPage = {
  0 : [
}

def printEditor(screen,screenWidth,screenHeight) :
  screen.delete("all")
  screen.create_rectangle(0,0,screenWidth,screenHeight//10,width = 0,fill = topColor)
  screen.create_rectangle(0,screenHeight//10,screenWidth,screenHeught//4,width = 0,fill = middleColor)
      

def click(Xaxe,Yaxe,screenWidth,screenHeight) :
  if Yaxe < screenHeight//10 :
    return "resume"
  elif Yaxe < screenHeight//4 :
    global page
    if Xaxe < screenWidth/2 :
      page = page - 1
    else :
      page = page + 1
  else :
    clikedFrame = (Xaxe - screenHeight//4) // 
