# tests/test_main.py

from controlador_aereo.model.aircraft import Aircraft
from controlador_aereo.algorithms.nearestPointsPair import find_closest_pairs


def test_closest_pair_algorithm():
    """
    Verifica que el algoritmo Closest Pair encuentre la distancia mínima correcta
    y todas las parejas que la alcanzan.
    """
    # Construimos un escenario conocido
    # Pares a distancia 1:
    # (0,0)–(1,0) y (0,2)–(1,2)
    aircrafts = [
        Aircraft(0, 0.0, 0.0),
        Aircraft(1, 1.0, 0.0),
        Aircraft(2, 0.0, 2.0),
        Aircraft(3, 1.0, 2.0),
        Aircraft(4, 10.0, 10.0),  # lejos
    ]

    result = find_closest_pairs(aircrafts)

    assert abs(result.min_distance - 1.0) < 1e-9
    ids_pairs = {tuple(sorted((a.id, b.id))) for a, b in result.pairs}
    assert ids_pairs == {(0, 1), (2, 3)}

def test_closest_pair_advanced_cases():
    """
    Prueba múltiples escenarios avanzados:
    - puntos repetidos
    - varios pares a misma distancia
    - un par extremadamente cercano
    - posiciones fuera de orden
    """

    aircrafts = [
        Aircraft(0, 10.0, 10.0),
        Aircraft(1, 20.0, 20.0),

        # Pareja extremadamente cercana
        Aircraft(2, 50.000, 50.000),
        Aircraft(3, 50.0001, 50.0001),

        # Puntos repetidos → distancia = 0
        Aircraft(4, 70.0, 80.0),
        Aircraft(5, 70.0, 80.0),

        # Otra pareja a misma distancia mínima (0)
        Aircraft(6, 5.0, 5.0),
        Aircraft(7, 5.0, 5.0),
    ]

    result = find_closest_pairs(aircrafts)

    # Distancia mínima debe ser exactamente 0
    assert abs(result.min_distance - 0.0) < 1e-12

    # Los pares que tienen distancia 0 son:
    expected_pairs = {
        (4, 5),
        (6, 7),
    }

    result_pairs = set(
        tuple(sorted((a.id, b.id)))
        for a, b in result.pairs
    )

    assert result_pairs == expected_pairs