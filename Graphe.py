#Graphe
from File import File

class Graphe :

    def __init__(self, nbSommets = 0, oriente = False, graphe = None) :
        self.nbSommets = int(nbSommets)
        self.oriente = bool(oriente)
        self.graphe = graphe
        size = len(graphe)
        for i in graphe :
            if len(i) != size :
                raise Exception("None square graph has been put in initialisation")
            for j in i :
                if not(j in [0,1]) :
                    raise Exception("The graph must be made of 0 and 1")

    def getNbSommets(self) :
        return self.nbSommets

    def getOriente(self) :
        return self.oriente

    def getGraphe(self) :
        return self.graphe

    # Test 1
    def __str__(self) :
        string = ""
        for i in self.getGraphe() :
            line = "["
            for j in i :
                line += str(j) + ","
            string += line[:-1] + "]\n"
        return string

    # Test 2
    def calculeNbArcsEntrants(self, numeroSommet) :
        nbEntrant = 0
        graphe = self.getGraphe()
        for i in range(len(graphe)) :
            nbEntrant += graphe[i][numeroSommet]
        return nbEntrant

    def afficheSources(self) :
        string = ""
        for i in range(len(self.getGraphe())) :
            if self.calculeNbArcsEntrants(i) == 0 :
                string += str(i)
        if string == "" :
            string = " pas de source "
        return string

    # Test 3
    def calculeNbArcsSortants(self, numeroSommet) :
        nbSortant = 0
        for i in self.getGraphe()[numeroSommet] :
            nbSortant += i
        return nbSortant

    def affichePuits(self) :              
        string = ""
        for i in range(len(self.getGraphe())) :
            if self.calculeNbArcsSortants(i) == 0 :
                string += str(i)
        if string == "" :
            string = " pas de puits "
        return string

    # Non testé - de l'affichage
    def affiche(self) :
        graphe = self.getGraphe()
        size = len(graphe)
        string = "Graphe :\n"
        for i in range(size*2+3) :
            string += "-"
        string += "\n"
        for i in graphe :
            line = "| "
            for j in i :
                line += str(j) + " "
            string += line[:-1] + "|\n"
        for i in range(size*2+3) :
            string += "-"
        string +="\n"
        print(string)
        return string

    # Non testé mais ca reste impressionant
    def listeParcours(self, numSommet, parcours = []):
        parcours = parcours[:] + [numSommet]
        listeParcours = []
        for i in range(self.getNbSommets()) : 
            if (bool(self.getGraphe()[numSommet][i]) and not(i in parcours)) :
                #print(i)
                leParcour = self.listeParcours(i,parcours)
                if type(leParcour[0]) == list :
                    listeParcours += leParcour[:]
                else :
                    listeParcours.append(leParcour)
        if listeParcours == [] :
            return parcours
        else :
            return listeParcours

    # Test 4
    # Parcours en profondeur
    def parcoursDFS(self, numSommet, parcours):
        parcours[numSommet] = True
        graphe = self.getGraphe()
        #print(self)
        for i in range(len(graphe)) :
            if (bool(graphe[numSommet][i]) and not(parcours[i])) :
                self.parcoursDFS(i,parcours)
        return parcours
    
    # Test 5
    def sommetAtteignable(self,numeroSommetDepart, numeroSommetArrivee) :
        #print(self.listeParcours(numeroSommetDepart))
        for i in self.listeParcours(numeroSommetDepart) :
            if type(i) == int :
                if i == numeroSommetArrivee :
                    return True
                else :
                    continue
            if numeroSommetArrivee in i :
                return True
        return False
             
    def circuitExiste(self) :
        graphe = self.getGraphe()
        for i in range(len(graphe)) :
            for j in self.listeParcours(i) :
                if type(j) == int :
                    continue
                if bool(graphe[j[-1]][i]) :
                    return True
        return False
    
    # Test 6
    # Parcours en largeur
    def parcoursBFS(self, debut):
        aTraiter = File()
        sommets = [debut]
        aTraiter.add(debut)
        graphe = self.getGraphe()
        size = len(graphe)
        while not(aTraiter.isEmpty()) :
            indice = aTraiter.get()
            for i in range(size) :
                if (bool(graphe[indice][i]) and not(i in sommets) ) :
                    sommets.append(i)
                    aTraiter.add(i)
        return sommets
        
    
        """listeParcours = self.listeParcours(debut)
        tailleParcours = []
        if type(listeParcours[0]) == int :
            return listeParcours
        for j in listeParcours :
            tailleParcours.append(len(j))
        return listeParcours[tailleParcours.index(max(tailleParcours))]"""
    
    # Test 7
    def estConnexe(self) :
        for i in range(self.getNbSommets()) :
            listeParcours = self.listeParcours(i)
            tailleParcours = []
            if type(listeParcours[0]) == int :
                continue
            for j in listeParcours :
                tailleParcours.append(len(j))
            if max(tailleParcours) == self.getNbSommets() :
                return True
        return False