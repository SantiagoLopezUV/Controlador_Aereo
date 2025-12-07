class Coordinate:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def showCoordinate(self):
        print(f"La coordenada es: ({self.x}, {self.y})")
    
    
    def distanceTo(self, otherCoordinate) -> float:
        """Calcula la distancia euclidiana a otra coordenada (método de instancia)."""
        dx = self.x - otherCoordinate.x
        dy = self.y - otherCoordinate.y
        return (((dx**2) + (dy**2)) ** 0.5)
    
    
    @staticmethod
    def distance_between_aircraft(aircraft1, aircraft2) -> float:
        """Calcula la distancia euclidiana entre dos aviones.
        
        Args:
            aircraft1: Primer avión (debe tener atributo 'coordinate' con x, y)
            aircraft2: Segundo avión (debe tener atributo 'coordinate' con x, y)
        
        Returns:
            float: Distancia euclidiana entre ambos aviones
        """
        dx = aircraft1.coordinate.x - aircraft2.coordinate.x
        dy = aircraft1.coordinate.y - aircraft2.coordinate.y
        return (((dx**2) + (dy**2)) ** 0.5)

    
    # Ordenamos la lista de los aviones por la coordenada X
    # sirve para dividir el problema en dos mitades equilibradas 
    # por la coordenada x y para elegir el punto medio.
    @staticmethod
    def sorted_arcrafts_by_x(aircrafts):
        """Ordena una lista de aviones por su coordenada X."""
        return sorted(aircrafts, key=lambda c: c.coordinate.x)


    # Ordenamos la lista de los aviones por la coordenada Y
    @staticmethod
    def sorted_aircrafts_by_y(aircrafts):
        """Ordena una lista de aviones por su coordenada Y."""
        return sorted(aircrafts, key=lambda c: c.coordinate.y)