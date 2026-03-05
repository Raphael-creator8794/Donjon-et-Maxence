#Maxence FERTRE
class File :
    def __init__(self, capacity=None) :
        self.values = []
        self.capacity = capacity
    
    def __str__(self) :
        string = ""
        size = len(self.values)
        for i in range(size) :
            string += str(self.values[i])
            if i < size-1 :
                string += " < "
        return string
    
    def nbElement(self) :
        return len(self.values)

    def isEmpty(self) :
        return self.values == []
    
    def isFull(self) :
        if self.capacity == None :
            return False
        return self.capacity == self.nbElement()
    
    def get(self) :
        match(self.nbElement()) :
            case 0 :
                raise ValueError("Getting a value from an empty lane")
            case 1 :
                value = self.values[0]
                self.values = []
            case _ :
                value = self.values[0]
                self.values = self.values[1:]
        return value
    
    def see(self) :
        if self.isEmpty() :
            raise ValueError("Getting a value from an empty lane")
        return self.values[0]
    
    def add(self,value) :
        if self.capacity == None or self.nbElement() < self.capacity :
            self.values.append(value)
    
    def push(self,value) :
        popValue = None
        if self.nbElement() >= self.capacity :
            popValue = self.get()
        self.add(value)
        return popValue

if __name__ == "__main__" :
    maFile = File(7)
    maFile.add("Lola")
    maFile.add("Pierre")
    maFile.add("Max")
    maFile.add("Léa")
    maFile.add("Clara")
    maFile.add("Gabin")
    print(maFile)
    while True :
        maFile.add(maFile.get())
        print(maFile)
        input()
