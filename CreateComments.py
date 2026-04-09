#
notDefined = True
if notDefined :
    from tkinter import *
    from File import *
    #from Donjon import refresh
    notDefined = False

nbLine =  0
textStyle = 0
pastComment = 0
lineThickness = 0
bannerWidth = 0

def initParametres(bannerHeight,width,lineHeight) :
    global nbLine
    global textStyle
    global pastComment
    global lineThickness
    global bannerWidth
    bannerWidth = width
    lineThickness = lineHeight
    nbLine = bannerHeight//lineHeight
    textStyle = ("Verdana",str(lineHeight//2))
    pastComment = File(nbLine)

def addComment(canva , comment) :
    global pastComment
    pastComment.push(comment)
    canva.delete("all")
    listComment = pastComment.getValues()[::-1]
    bannerCenter = bannerWidth/2
    for i in range(len(listComment)) :
        canva.create_text(bannerCenter,(i+0.5)*lineThickness,text = listComment[i],fill = "#FFFFFF",font = textStyle)
    refresh()