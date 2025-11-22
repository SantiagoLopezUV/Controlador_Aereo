# src/controlador_aereo/model/aircraft.py

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple
import random


@dataclass(frozen=True)
class Aircraft:
    """
    Representa una aeronave en el plano cartesiano 2D.
    """
    id: int
    x: float
    y: float

    def position(self) -> Tuple[float, float]:
        """Devuelve la posición de la aeronave como tupla (x, y)."""
        return self.x, self.y


def generate_random_aircrafts(
    n: int,
    x_min: float = 0.0,
    x_max: float = 100.0,
    y_min: float = 0.0,
    y_max: float = 100.0,
    seed: int | None = None,
) -> List[Aircraft]:
    """
    Genera una lista de n aeronaves con posiciones aleatorias en el rango dado.
    """
    if seed is not None:
        random.seed(seed)

    aircrafts: List[Aircraft] = []
    for i in range(n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        aircrafts.append(Aircraft(id=i, x=x, y=y))
    return aircrafts
