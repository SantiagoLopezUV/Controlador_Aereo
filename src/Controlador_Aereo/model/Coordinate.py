class Coordinate:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def showCoordinate(self):
        print(f"La coordenada es: ({self.x}, {self.y})")
    
    
    def distanceTo(self, otherCoordinate) -> float:
        return ((self.x - otherCoordinate.x) ** 2 + (self.y - otherCoordinate.y) ** 2) ** 0.5