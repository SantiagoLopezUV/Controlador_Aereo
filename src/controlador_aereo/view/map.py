# src/controlador_aereo/views/map.py

from __future__ import annotations
from typing import Iterable, Sequence, Tuple

import matplotlib.pyplot as plt

from controlador_aereo.model.aircraft import Aircraft

AircraftPair = Tuple[Aircraft, Aircraft]


def plot_air_traffic(
    aircrafts: Sequence[Aircraft],
    closest_pairs: Iterable[AircraftPair],
    min_distance: float,
    collision_threshold: float | None = None,
) -> None:
    """
    Dibuja las aeronaves en un plano y resalta las parejas más cercanas.
    """
    closest_pairs = list(closest_pairs)

    fig, ax = plt.subplots(figsize=(8, 6))

    # Todas las aeronaves
    xs = [a.x for a in aircrafts]
    ys = [a.y for a in aircrafts]
    ax.scatter(xs, ys, s=40, label="Aeronaves")

    # Etiquetas con el id
    for a in aircrafts:
        ax.annotate(str(a.id), (a.x, a.y), textcoords="offset points",
                    xytext=(5, 3), fontsize=8)

    # Resaltar pares más cercanos
    for a1, a2 in closest_pairs:
        ax.scatter([a1.x, a2.x], [a1.y, a2.y], s=70)
        ax.plot([a1.x, a2.x], [a1.y, a2.y])

    # Título con info de colisión
    if collision_threshold is not None and min_distance <= collision_threshold:
        title = (
            f"Posible riesgo de colisión: distancia mínima {min_distance:.3f} "
            f"(umbral {collision_threshold:.3f})"
        )
    else:
        title = f"Aeronaves: {len(aircrafts)} | Distancia mínima: {min_distance:.3f}"

    ax.set_title(title)
    ax.set_xlabel("Coordenada X")
    ax.set_ylabel("Coordenada Y")
    ax.grid(True)
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.show()
