"""
Unit tests (pytest) for low-level components: Coordinate and Aircraft utilities.
"""
from Controlador_Aereo.model.Coordinate import Coordinate
from Controlador_Aereo.model.Aircraft import Aircraft


def test_coordinate_creation():
    coord = Coordinate(10, 20)
    assert coord.x == 10
    assert coord.y == 20


def test_distanceTo_method():
    c1 = Coordinate(0, 0)
    c2 = Coordinate(3, 4)
    assert abs(c1.distanceTo(c2) - 5.0) < 1e-6


def test_distance_between_aircraft_function():
    c1 = Coordinate(0, 0)
    c2 = Coordinate(3, 4)
    a1 = Aircraft(1, c1)
    a2 = Aircraft(2, c2)
    assert abs(Coordinate.distance_between_aircraft(a1, a2) - 5.0) < 1e-6


def test_sorting_helpers_and_show_methods(capfd):
    # prepare aircrafts
    a1 = Aircraft(1, Coordinate(50, 30))
    a2 = Aircraft(2, Coordinate(10, 80))
    a3 = Aircraft(3, Coordinate(40, 10))
    arr = [a1, a2, a3]

    sorted_x = Coordinate.sorted_arcrafts_by_x(arr)
    assert [a.numPlane for a in sorted_x] == [2, 3, 1]

    sorted_y = Coordinate.sorted_aircrafts_by_y(arr)
    assert [a.numPlane for a in sorted_y] == [3, 1, 2]

    # show methods should not raise; capture output
    a1.showAircraft()
    c = Coordinate(1, 2)
    c.showCoordinate()
    out, err = capfd.readouterr()
    assert "Avion" in out
    assert "La coordenada es" in out
