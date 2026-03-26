#Maxence, Raphaël, Maëva

# Variables de paramètre
page = floatLoop(0,0,0)

def actionSettings(screen,Xaxe,Yaxe,screenWidth,screenHeight) :
  if Yaxe < screenHeight*0.15 : #Si l'utilisateur clique sur les 15% supérieur de l'écran il clique dans le vide
    if Xaxe > (screenWidth - screenHeight*0.15) :
      return "resume"
  elif Yaxe < screenHeight*0.25 :
    if Xaxe > screenWidth//2 :
      page = page + 1
    else :
      page = page - 1
