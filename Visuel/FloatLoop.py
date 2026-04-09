#Maxence FERTRE

class floatLoop :
    def __init__(self,start,minValue,maxValue) :
        self.value = start
        difference = maxValue - minValue
        if difference > 0 :
            self.max = maxValue
            self.min = minValue
            self.difference = difference
        else :
            self.max = minValue
            self.min = maxValue
            self.difference = difference*(-1)

    def getValue(self) :
        return self.value

    def getMax(self) :
        return self.max

    def getMin(self) :
        return self.min
    
    def getDifference(self) :
        return self.difference
    
    def __str__(self):
        return str(self.getValue())

    def __add__(self, other):
        maxValue = self.getMax()
        minValue = self.getMin()
        step = self.getDifference()
        total = other + self.getValue()
        while total > maxValue :
            total -= step + 1
        while total < minValue :
            total += step + 1
        return floatLoop(total,minValue,maxValue)
    
    def __sub__(self,other) :
        return self + (-1)*other
    
    def __mul__(self, other):
        maxValue = self.getMax()
        minValue = self.getMin()
        step = self.getDifference()
        total = other * self.getValue()
        while total > maxValue :
            total -= step + 1
        while total < minValue :
            total += step + 1
        return floatLoop(total,minValue,maxValue)
    
    def __eq__(self, value):
        return value == self.getValue()
    
    def __ne__(self, value):
        return value != self.getValue()
    
    def __lt__(self, other):
        return other > self.getValue()
    
    def __le__(self, other):
        return other >= self.getValue()
    
    def __gt__(self, other):
        return other < self.getValue()
    
    def __ge__(self, other):
        return other <= self.getValue()

if __name__ == "__main__" :
    test = floatLoop(1,0,2)
    test *= 10.5
    print(test)
