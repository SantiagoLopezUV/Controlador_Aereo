# src/controlador_aereo/utils/distancePoints.py

from __future__ import annotations
from math import hypot

from controlador_aereo.model.aircraft import Aircraft


def euclidean_distance(a1: Aircraft, a2: Aircraft) -> float:
    """
    Calcula la distancia euclidiana entre dos aeronaves.
    """
    dx = a1.x - a2.x
    dy = a1.y - a2.y
    return hypot(dx, dy)
