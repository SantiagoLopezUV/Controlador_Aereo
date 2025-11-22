# src/controlador_aereo/main.py

from __future__ import annotations

from controlador_aereo.model.aircraft import generate_random_aircrafts
from controlador_aereo.algorithms.nearestPointsPair import find_closest_pairs
from controlador_aereo.views.map import plot_air_traffic

# Umbral para considerar “posible colisión”
DEFAULT_COLLISION_THRESHOLD = 10.0  # puedes ajustarlo según tu criterio


def main() -> None:
    """
    Punto de entrada del sistema Controlador Aéreo.

    - Genera aeronaves aleatorias.
    - Ejecuta el algoritmo Closest Pair (Divide y Vencer).
    - Muestra resultados en consola y en un gráfico.
    """
    try:
        n = int(input("Ingrese el número de aeronaves a simular: "))
        if n < 2:
            raise ValueError
    except ValueError:
        print("Valor inválido. Usando n = 20 por defecto.")
        n = 20

    aircrafts = generate_random_aircrafts(n=n)

    result = find_closest_pairs(aircrafts)

    print(f"\nSe generaron {n} aeronaves.")
    print(f"Distancia mínima encontrada: {result.min_distance:.4f}")
    if result.min_distance <= DEFAULT_COLLISION_THRESHOLD:
        print(
            f"⚠ Posible riesgo de colisión (distancia ≤ {DEFAULT_COLLISION_THRESHOLD})"
        )
    print("\nPares de aeronaves más cercanas:")
    for a1, a2 in result.pairs:
        print(
            f"  Aeronave {a1.id} en ({a1.x:.2f}, {a1.y:.2f}) "
            f"y Aeronave {a2.id} en ({a2.x:.2f}, {a2.y:.2f})"
        )

    # Visualización
    plot_air_traffic(
        aircrafts=aircrafts,
        closest_pairs=result.pairs,
        min_distance=result.min_distance,
        collision_threshold=DEFAULT_COLLISION_THRESHOLD,
    )


if __name__ == "__main__":
    main()
