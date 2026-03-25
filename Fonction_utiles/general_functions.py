#Quoicoubesque group
'''----- center -----------
> -- Objectif -- :
    Centrer un str sur une taille donnée
> -- Paramètre -- :
    lenght : /int/ La taille finale du str
    what : /str/ Avec quoi vont être rempli les trous. Doit n'être qu'un caractère !
    word : /str/ Ce que vous voulez centrer
> -- Retourne -- :
    /str/ Le str centré
'''
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

'''----- fillGaps -----------
> -- Objectif -- :
    Remplir un str pour qu'il fasse une taille donnée
> -- Paramètre -- :
    lenght : /int/ La taille finale du str
    what : /str/ Avec quoi vont être rempli les trous. Doit n'être qu'un caractère !
    word : /str/ Le str que vous voulez ensuite compléter
> -- Retourne -- :
    /str/ Le str remplit
'''
def fillGaps(lenght,what,word) :
    what = str(what)
    if len(what) != 1 :
        raise Exception("Incorrect lenght of filling string"+len(what)+" != 1")
    string = str(word)
    for _ in range(lenght-(1+len(word))):
        string += what
    return what

#------------------------------------------------------------------------------- Fin des fonctions----------
