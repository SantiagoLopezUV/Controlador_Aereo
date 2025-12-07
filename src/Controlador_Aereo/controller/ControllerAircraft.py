import random

from Controlador_Aereo.model.Aircraft import Aircraft
from Controlador_Aereo.model.Coordinate import Coordinate

class ControllerAircraft:
    def __init__(self):
        self.aircraftsList = []
    
    
    def addAircraft(self, aircraft: Aircraft):
        self.aircraftsList.append(aircraft)
    
    
    def generateRandomCoordinateAircraft(self, numAircrafts: int):
        xLimit = 100
        yLimit = 100
        for i in range(numAircrafts):
            x = random.randint(0, xLimit)
            y = random.randint(0, yLimit)
            coordinate = Coordinate(x, y)
            aircraft = Aircraft(i+1, coordinate)
            self.addAircraft(aircraft)
    
    
    def showAircrafts(self):
        for aircraft in self.aircraftsList:
            aircraft.showAircraft() 