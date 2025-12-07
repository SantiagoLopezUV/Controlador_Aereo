from Controlador_Aereo.model.ClosestPairResult import ClosestPairResult
from Controlador_Aereo.model.Coordinate import Coordinate


# Se usa con n ≤ 3
# Porque cuando la recursión divide la lista en mitades, 
# llegará un punto donde cada mitad tiene pocos elementos:
# * Si tiene 1 → no hay pareja.
# * Si tiene 2 → la distancia es trivial.
# * Si tiene 3 → solo 3 combinaciones (se puede calcular rápido).


def closest_pair_small_list(aircrafts):
    aircraftsResult = ClosestPairResult()
    n = len(aircrafts)
    
    for i in range(n):
        for j in range(i + 1, n):
            distance = Coordinate.distance_between_aircraft(aircrafts[i], aircrafts[j])
            aircraftsResult.updateDistance(distance, aircrafts[i], aircrafts[j])
    
    return aircraftsResult


# Implementación del algoritmo de divide y vencerás para encontrar el par más cercano
def closest_pair_divide_and_conquer(aircraftsSortedByX, aircraftsSortedByY):
    n = len(aircraftsSortedByX)
    # Se asume que ambas listas tienen la misma longitud
    if n <= 3:
        return closest_pair_small_list(aircraftsSortedByX)
    mid = n // 2
    midAircraft = aircraftsSortedByX[mid]
    # Toma el avion en la posicion central de la lista ordenada por X
    leftByX = aircraftsSortedByX[:mid]
    rightByX = aircraftsSortedByX[mid:]
    # Almacena la lista de aviones de la izquierda y derecha ordenados por X
    # El elemento del medio pertenece a la derecha
    leftByY = []
    rightByY = []
    # Lista que almacena la lista de aviones de la izquierda y derecha ordenados por X
    for aircraft in aircraftsSortedByY:
        if aircraft.coordinate.x <= midAircraft.coordinate.x:
            leftByY.append(aircraft)
        else:
            rightByY.append(aircraft)
    # Recorre la lista ordenada por Y y asigna cada avión a la lista izquierda o derecha
    # dependiendo de su coordenada X en relación con la del avión medio.
    
    # Recursión en ambas mitades
    leftResult = closest_pair_divide_and_conquer(leftByX, leftByY)
    rightResult = closest_pair_divide_and_conquer(rightByX, rightByY)
    
    if leftResult.distance < rightResult.distance:
        minResult = leftResult
    else:
        minResult = rightResult
    
    
    # Construcción de la franja central
    # La franja central contiene los puntos que están a una distancia
    # menor que la distancia mínima encontrada en las dos mitades
    # de la línea divisoria.
    # Esta franja se utiliza para verificar si hay pares de puntos
    # que estén más cerca entre sí, cruzando la línea divisoria.
    
    stripMiddle = []
    # Lista que contendra los aviones en la franja central(ordenado por Y)
    for aircraft in aircraftsSortedByY:
        if abs(aircraft.coordinate.x - midAircraft.coordinate.x) < minResult.distance:
            stripMiddle.append(aircraft)
    #añade solamente los que la coordenada x esté dentro de la distancia mínima encontrada
    # desde la línea divisoria.
    stripMiddle.sort(key=lambda c: c.coordinate.y)
    # Para cada punto en la franja, solo es necesario comparar
    # con los siguientes hasta 7 puntos ordenados por Y.
    # Esto se basa en la propiedad geométrica del algoritmo
    # divide-and-conquer para closest pair en 2D.
    sizeStrip = len(stripMiddle)
    for i in range(sizeStrip):
        # Comprobar con los siguientes hasta 7 vecinos
        for j in range(i + 1, min(i + 7, sizeStrip)):
            dist = Coordinate.distance_between_aircraft(stripMiddle[i], stripMiddle[j])
            minResult.updateDistance(dist, stripMiddle[i], stripMiddle[j])
    return minResult
    
    

