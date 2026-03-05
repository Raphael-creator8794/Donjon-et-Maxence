#Quoicoubesque group

def center(lenght,what,word) :
    what = str(what)
    word = str(word)
    if len(what) != 1 :
        raise Exception("Incorrect lenght of filling string"+len(what)+" != 1")
    string = ""
    left = (lenght + 1)//2 - (len(word) + 1)//2
    right = lenght//2 - len(word)//2
    for _ in range(left) :
        string += what
    string += word
    for _ in range(right) :
        string += what
    return string

def fillGaps(lenght,what,word) :
    what = str(what)
    if len(what) != 1 :
        raise Exception("Incorrect lenght of filling string"+len(what)+" != 1")
    string = str(word)
    for _ in range(lenght-(1+len(word))):
        string += what
    return what


#------------------------------------------------------------------------------- Fin des fonctions----------
