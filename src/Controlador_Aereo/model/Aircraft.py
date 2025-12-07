from Controlador_Aereo.model.Coordinate import Coordinate

class Aircraft:
    def __init__(self, numPlane, location: Coordinate):
        self.numPlane = numPlane
        self.coordinate = location
    
    
    def showAircraft(self):
        print(f"Avion {self.numPlane} con posicion ({self.coordinate.x}\
            {self.coordinate.y})")