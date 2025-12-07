class ClosestPairResult:
    def __init__(self, distance=float('inf'), aircraft1=None, aircraft2=None):
        self.distance = distance
        self.aircraft1 = aircraft1
        self.aircraft2 = aircraft2


    def updateDistance(self, newDistance, p1, p2):
        if newDistance < self.distance:
            self.distance = newDistance
            self.aircraft1 = p1
            self.aircraft2 = p2


    def getDistanceAircrafts(self):
        return (f"Distancia mínima: {self.distancia}\n"
                f"Avión 1: {self.aircraft1}\n"
                f"Avión 2: {self.aircraft2}")


