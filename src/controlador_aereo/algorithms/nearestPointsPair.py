# src/controlador_aereo/algorithms/nearestPointsPair.py

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Sequence, Tuple

from controlador_aereo.model.aircraft import Aircraft
from controlador_aereo.utils.distancePoints import euclidean_distance


AircraftPair = Tuple[Aircraft, Aircraft]


@dataclass
class ClosestPairResult:
    """
    Resultado del algoritmo de par de puntos más cercanos.
    """
    min_distance: float
    pairs: List[AircraftPair]


def _brute_force_closest_pair(aircrafts: Sequence[Aircraft]) -> ClosestPairResult:
    """
    Caso base: calcula el par (o pares) más cercanos usando fuerza bruta.
    Complejidad O(n^2).
    """
    n = len(aircrafts)
    if n < 2:
        raise ValueError("Se necesitan al menos dos aeronaves para comparar.")

    best_distance = float("inf")
    best_pairs: List[AircraftPair] = []

    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(aircrafts[i], aircrafts[j])
            if d < best_distance - 1e-12:
                best_distance = d
                best_pairs = [(aircrafts[i], aircrafts[j])]
            elif abs(d - best_distance) <= 1e-12:
                best_pairs.append((aircrafts[i], aircrafts[j]))

    return ClosestPairResult(min_distance=best_distance, pairs=best_pairs)


def _closest_pair_in_strip(strip: List[Aircraft], delta: float) -> ClosestPairResult:
    """
    Busca pares más cercanos en la franja central (strip).
    La franja viene ordenada por coordenada Y.
    """
    best_distance = delta
    best_pairs: List[AircraftPair] = []
    m = len(strip)

    for i in range(m):
        j = i + 1
        # Comparamos solo con los siguientes puntos cercanos en Y
        while j < m and (strip[j].y - strip[i].y) < best_distance + 1e-12:
            d = euclidean_distance(strip[i], strip[j])
            if d < best_distance - 1e-12:
                best_distance = d
                best_pairs = [(strip[i], strip[j])]
            elif abs(d - best_distance) <= 1e-12:
                best_pairs.append((strip[i], strip[j]))
            j += 1

    if best_pairs:
        return ClosestPairResult(min_distance=best_distance, pairs=best_pairs)
    return ClosestPairResult(min_distance=delta, pairs=[])


def _closest_pair_recursive(
    px: List[Aircraft],
    py: List[Aircraft],
) -> ClosestPairResult:
    """
    Función recursiva del algoritmo Divide y Vencer.
    px: lista ordenada por X
    py: lista ordenada por Y
    """
    n = len(px)
    if n <= 3:
        return _brute_force_closest_pair(px)

    mid = n // 2
    mid_point = px[mid]
    mid_x = mid_point.x

    left_x = px[:mid]
    right_x = px[mid:]

    left_y: List[Aircraft] = []
    right_y: List[Aircraft] = []
    for a in py:
        if a.x <= mid_x:
            left_y.append(a)
        else:
            right_y.append(a)

    left_result = _closest_pair_recursive(left_x, left_y)
    right_result = _closest_pair_recursive(right_x, right_y)

    # Mejor de las dos mitades
    if left_result.min_distance < right_result.min_distance - 1e-12:
        best_distance = left_result.min_distance
        best_pairs = list(left_result.pairs)
    elif right_result.min_distance < left_result.min_distance - 1e-12:
        best_distance = right_result.min_distance
        best_pairs = list(right_result.pairs)
    else:
        best_distance = left_result.min_distance
        best_pairs = list(left_result.pairs) + list(right_result.pairs)

    # Construir franja central
    strip: List[Aircraft] = [
        a for a in py
        if abs(a.x - mid_x) <= best_distance + 1e-12
    ]

    strip_result = _closest_pair_in_strip(strip, best_distance)

    if strip_result.min_distance < best_distance - 1e-12:
        return strip_result
    elif abs(strip_result.min_distance - best_distance) <= 1e-12 and strip_result.pairs:
        best_pairs.extend(strip_result.pairs)

    return ClosestPairResult(min_distance=best_distance, pairs=best_pairs)


def find_closest_pairs(aircrafts: Sequence[Aircraft]) -> ClosestPairResult:
    """
    Algoritmo principal Closest Pair (Divide y Vencer).

    Complejidad temporal: O(n log n)
    """
    n = len(aircrafts)
    if n < 2:
        raise ValueError("Se necesitan al menos dos aeronaves para analizar colisiones.")

    px = sorted(aircrafts, key=lambda a: a.x)
    py = sorted(aircrafts, key=lambda a: a.y)
    return _closest_pair_recursive(px, py)
