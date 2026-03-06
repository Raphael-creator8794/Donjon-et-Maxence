#Maxence FERTRE
from Graphe import *
from json import *

isSimplePath = True
listLettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
tools = ["S", "E", ".", "#", "STOP"]

def center(lenght,what,word) :
    what = str(what)
    word = str(word)
    if len(what) != 1 :
        raise Exception("What must be a single string")
    string = ""
    left = (lenght + 1)//2 - (len(word) + 1)//2
    right = lenght//2 - len(word)//2
    for _ in range(left) :
        string += what
    string += word
    for _ in range(right) :
        string += what
    return string

def getDics(board) :
    size = len(board)
    coord_to_num = {}
    num_to_coord = {}
    lastNum = 0
    for i in range(size) :
        for j in range(size) :
            if board[i][j] != "#" :
                coord_to_num[(i,j)] = lastNum
                num_to_coord[lastNum] = (i,j)
                lastNum += 1
    return coord_to_num ,num_to_coord

def statePath(board,x,y) :
    size = len(board)
    if (x < 0) or (y < 0) or (x >= size) or (y >= size) :
        return False
    else :
        return board[x][y] == "." or board[x][y] == "S" or board[x][y] == "E"

def createGraph(board ,coord_to_num ,num_to_coord) :
    sizeBoard = len(board)
    sizeGraph = len(coord_to_num)
    futureGraph = [[ 0 for _ in range(sizeGraph) ] for _ in range(sizeGraph) ]
    for x,y in num_to_coord.values() :
        if statePath(board,x-1,y) :
            futureGraph[coord_to_num[(x,y)]][coord_to_num[(x-1,y)]] = 1
        if statePath(board,x+1,y) :
            futureGraph[coord_to_num[(x,y)]][coord_to_num[(x+1,y)]] = 1
        if statePath(board,x,y-1) :
            futureGraph[coord_to_num[(x,y)]][coord_to_num[(x,y-1)]] = 1
        if statePath(board,x,y+1) :
            futureGraph[coord_to_num[(x,y)]][coord_to_num[(x,y+1)]] = 1
    return Graphe(sizeGraph,False,futureGraph)

def printLabyrinth(labyrinth, isPrinting = True) :
    string = ""
    for i in labyrinth :
        line = "[ "
        for j in i :
            line += str(j) + " "
        string += line + "]\n"
    if isPrinting :
        print(string)
    return string

def printAllLabyrinths(dicLabyrinth) :
    pass

def creatCriticalPath(labyrinth,start,end) :
    listPaths = labyrinth.listeParcours(start)
    if type(listPaths[0]) == int :
        return listPaths[:listPaths.index(end)+1]
    else :
        pathsToEnd = []
        for i in listPaths :
            if end in i :
                pathsToEnd.append(i[:i.index(end)+1])
        listSizes = []
        for i in pathsToEnd :
            listSizes.append(len(i))
        return pathsToEnd[listSizes.index(min(listSizes))]

def showCriticalPath(labyrinth, criticalPath, num_to_coord) :
    newLabyrinth = labyrinth[:]
    for i in range(1,len(criticalPath)-1) :
        x,y = num_to_coord[criticalPath[i]]
        if isSimplePath :
            nextX, nextY = num_to_coord[criticalPath[i+1]]
            if nextX - x == 1 :
                newLabyrinth[x][y] = "v"
            elif nextX - x == -1 :
                newLabyrinth[x][y] = "^"
            elif nextY - y == 1 :
                newLabyrinth[x][y] = ">"
            elif nextY - y == -1 :
                newLabyrinth[x][y] = "<"
        else :
            newLabyrinth[x][y] = "*"
    return newLabyrinth

def askSize() :
    print("De quel taille voulez vous votre labyrinthe ?")
    x = None
    while True :
        try :
            if x == None :
                x = int(input("\t Largeur : "))
                if x < 2 or x > 20 :
                    x = None
                    raise ValueError
            y = int(input("\t Hauteur : "))
            if y < 2 or y > 20 :
                raise ValueError
        except TypeError :
            print("Les coordonnées doivent être des entiers")
        except ValueError :
            print("Les coordonnées doivent être d'une valeur entre 2 et 20")
        else :
            return x,y

def isCoordinate(string) :
    if type(string) != str :
        return False
    elif len(string) == 1 or len(string) > 3 :
        return False
    elif string[0:1].isalpha() :
        if string[1:].isdigit() :
            return True
        else :
            return False
    else :
        return False

def replaceFromGrid(grid, oldValue, newValue) :
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            if grid[i][j] == oldValue :
                grid[i][j] = newValue

def printHUD(labyrinth,actualTool) :
    size = len(labyrinth)
    string = "\n\t["
    for i in [0,1,2,3] :
        if i == actualTool :
            string += " >" + tools[i] + "< |"
        else :
            string += " " + tools[i] + " |"
    string = string[:-1] + "]\n\n"
    
    string += "         "
    for i in range(len(labyrinth[0])) :
        string += " " + listLettre[i]
    string += "\n"
    
    for i in range(size) :
        if i < 10 :
            string += "   " + str(i) + "  : " + printLabyrinth([labyrinth[i]],False)[:-1] + " : " + str(i) + "\n"
        else : 
            string += "   " + str(i) + " : " + printLabyrinth([labyrinth[i]],False)[:-1] + " : " + str(i) + "\n"
    
    string += "         "
    for i in range(len(labyrinth[0])) :
        string += " " + listLettre[i]
    string += "\n"
    
    print(string)

def createLabyrinth() :
    width,hight = askSize()
    createdLabyrinth = [ ["." for _ in range(width)] for _ in range(hight) ]
    createdLabyrinth[0][0] = "S"
    createdLabyrinth[-1][-1] = "E"
    actualTool = 2
    action = None
    while action != "STOP" :
        printHUD(createdLabyrinth,actualTool)
        action = input("\t-> ")
        if action == None :
            continue
        action = action.upper()
        if action in tools :
            actualTool = tools.index(action)
        elif isCoordinate(action) :
            x = int(action[1:])
            y = listLettre.index(action[0])
            if x >= hight  or y >= width :
                continue
            match (actualTool) :
                case 0 :
                    if createdLabyrinth[x][y] != "E" :
                        replaceFromGrid(createdLabyrinth,"S",".")
                    else :
                        replaceFromGrid(createdLabyrinth,"S","E")
                    createdLabyrinth[x][y] = "S"
                case 1 :
                    if createdLabyrinth[x][y] != "S" :
                        replaceFromGrid(createdLabyrinth,"E",".")
                    else :
                        replaceFromGrid(createdLabyrinth,"E","S")
                    createdLabyrinth[x][y] = "E"
                case 2 :
                    if createdLabyrinth[x][y] != "S" and createdLabyrinth[x][y] != "E" :
                        createdLabyrinth[x][y] = "."
                case 3 :
                    if createdLabyrinth[x][y] != "S" and createdLabyrinth[x][y] != "E" :
                        createdLabyrinth[x][y] = "#"
    print("Voulez vous enregistrer votre labyrinthe ? (o = oui, n= non)")
    answer = input("\t-> ")
    if answer != None :
        answer = answer.lower()
    while answer != "o" and answer != "n" :
        answer = input("\t-> ")
        if answer != None :
            answer = answer.lower()
    if answer == "o" :
        return createdLabyrinth

def getStartAndEnd(labyrinth,coord_to_num) :
    start = None
    end = None
    for i,j in coord_to_num.keys() :
        if labyrinth[i][j] == "S" :
            if end != None :
                return coord_to_num[(i,j)],end
            else :
                start = coord_to_num[(i,j)]
        elif labyrinth[i][j] == "E" :
            if start != None :
                return start,coord_to_num[(i,j)]
            else :
                end = coord_to_num[(i,j)]

def showPropreties(labyrinth) :
    coord_to_num ,num_to_coord = getDics(labyrinth)
    graphLabyrinth = createGraph(labyrinth,coord_to_num ,num_to_coord)
    start,end = getStartAndEnd(labyrinth, coord_to_num)
    
    print("--- Graphe du Labyrinthe ---")
    print("Graphe non orienté ayant",graphLabyrinth.getNbSommets(),"sommets.\n")
    print("Matrice du graph :")
    print(graphLabyrinth)
    print("Entrée au sommet : ",start)
    print("Sortie au sommet : ",end)
    print()
    print("***** Sortie atteignable ? *****")
    if graphLabyrinth.sommetAtteignable(start,end) :
        print("Oui, voici le chemin le plus rapide :")
        criticalPath = creatCriticalPath(graphLabyrinth,start,end)
        printLabyrinth(showCriticalPath(labyrinth,criticalPath,num_to_coord))
    else :
        print("Non, la sortie n'est pas atteignable.")

def addLabyrinth(name,labyrinth) :
    with open("labyrinthes.json","r") as baseLabyrinth :
        dicLabyrinth = load(baseLabyrinth)
    dicLabyrinth[name] = labyrinth
    with open("labyrinthes.json","w") as baseLabyrinth :
        dump(dicLabyrinth,baseLabyrinth,indent = 4)

def menu() :
    print("Que voulez vous faire ?")
    print("\t1 - Obtenir les propriétés d'un labyrinthe")
    print("\t2 - Parcourir un labyrinthe")
    print("\t3 - Creer un nouveau labyrinthe")
    print("\t0 - Sortir")
    possibilities = [ str(i) for i in range(4) ]
    answer = input("\n\t-> ")
    if answer in possibilities :
        return answer
    else :
        print("Veuillez choisir parmis les options suivantes")
    
def isNameExisting(name, dicLabyrinth) :
    try :
        dicLabyrinth[name]
    except KeyError :
        return False
    else : 
        return True

def askName(dicLabyrinth) :
    print("Quel nom voulez vous lui donnez ?")
    name = input("\t-> ")
    if isNameExisting(name,dicLabyrinth) :
        print("Ce nom est déja pris")
        return askName(dicLabyrinth)
    else :
        return name

def askForMove() :
    print("Choisissez votre mouvement :")
    print("1 - Haut")
    print("2 - Bas")
    print("3 - Gauche")
    print("4 - Droite")
    possibilities = ["1","2","3","4","stop"]
    answer = None
    while not(answer in possibilities) :
        answer = input("\t-> ")
        if answer != None :
            answer = answer.lower()
    return answer

def moveInto(labyrinth) :
    width, hight = len(labyrinth[0]), len(labyrinth)
    coord_to_num ,num_to_coord = getDics(labyrinth)
    graphLabyrinth = createGraph(labyrinth,coord_to_num ,num_to_coord)
    start,end = getStartAndEnd(labyrinth, coord_to_num)
    pastValue = "S"
    x,y = num_to_coord[start]
    labyrinth[x][y] = "P"
    while pastValue != "E" :
        printLabyrinth(labyrinth)
        move = askForMove()
        if move == "stop" :
            break
        match move :
            case "1" : #Haut
                if x > 0 and labyrinth[x-1][y] != "#" :
                    labyrinth[x][y] = pastValue
                    x -= 1
                    pastValue = labyrinth[x][y]
                    labyrinth[x][y] = "P"
            case "2" : #Bas
                if x < hight-1 and labyrinth[x+1][y] != "#" :
                    labyrinth[x][y] = pastValue
                    x += 1
                    pastValue = labyrinth[x][y]
                    labyrinth[x][y] = "P"
            case "3" : #Gauche
                if y > 0 and labyrinth[x][y-1] != "#" :
                    labyrinth[x][y] = pastValue
                    y -= 1
                    pastValue = labyrinth[x][y]
                    labyrinth[x][y] = "P"
            case "4" : #Droite
                if y < width-1 and labyrinth[x][y+1] != "#" :
                    labyrinth[x][y] = pastValue
                    y += 1
                    pastValue = labyrinth[x][y]
                    labyrinth[x][y] = "P"
    labyrinth[x][y] = pastValue

"""testLabyrinth = [
["S", ".", ".", "#"],
["#", ".", ".", "#"],
[".", ".", "#", "."],
["#", ".", ".", "E"]
]"""
with open("labyrinthes.json","r") as baseLabyrinth :
    dicLabyrinth = load(baseLabyrinth)
answer = None
while answer != "0" :
    answer = menu()
    match answer :
        case "1" :
            printAllLabyrinths(dicLabyrinth)
            print("De quel labyrinth voulez vous voir les propriétés ?")
            labyrinthName = input("\t-> ")
            if isNameExisting(labyrinthName, dicLabyrinth) :
                showPropreties(dicLabyrinth[labyrinthName])
        case "2" :
            printAllLabyrinths(dicLabyrinth)
            print("Dans quel labyrinthe voulez vous vous ballader ?")
            labyrinthName = input("\t-> ")
            if isNameExisting(labyrinthName, dicLabyrinth) :
                moveInto(dicLabyrinth[labyrinthName])
        case "3" :
            newLabyrinth = createLabyrinth()
            if newLabyrinth != None :
                addLabyrinth(askName(dicLabyrinth),newLabyrinth)