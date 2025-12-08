class Coordinate:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def showCoordinate(self):
        print(f"La coordenada es: ({self.x}, {self.y})")
    
    
    def distanceTo(self, otherCoordinate) -> float:
        dx = self.x - otherCoordinate.x
        dy = self.y - otherCoordinate.y
        return (((dx**2) + (dy**2)) ** 0.5)
    
    
    @staticmethod
    def distance_between_aircraft(aircraft1, aircraft2) -> float:
        dx = aircraft1.coordinate.x - aircraft2.coordinate.x
        dy = aircraft1.coordinate.y - aircraft2.coordinate.y
        return (((dx**2) + (dy**2)) ** 0.5)

    
    @staticmethod
    def sorted_arcrafts_by_x(aircrafts):
        return sorted(aircrafts, key=lambda c: c.coordinate.x)


    @staticmethod
    def sorted_aircrafts_by_y(aircrafts):
        return sorted(aircrafts, key=lambda c: c.coordinate.y)