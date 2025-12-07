"""
Integration tests (pytest) for Controller and algorithms.
"""
from Controlador_Aereo.model.Coordinate import Coordinate
from Controlador_Aereo.model.Aircraft import Aircraft
from Controlador_Aereo.controller.ControllerAircraft import ControllerAircraft
from Controlador_Aereo.algorithms.code import closest_pair_small_list, closest_pair_divide_and_conquer


def test_closest_pair_small_list_simple():
    # small set where answer is known
    a1 = Aircraft(1, Coordinate(0, 0))
    a2 = Aircraft(2, Coordinate(1, 0))
    a3 = Aircraft(3, Coordinate(10, 10))
    res = closest_pair_small_list([a1, a2, a3])
    assert abs(res.distance - 1.0) < 1e-6
    assert {res.aircraft1.numPlane, res.aircraft2.numPlane} == {1, 2}


def test_controller_generate_and_divide_conquer():
    controller = ControllerAircraft()
    controller.generateRandomCoordinateAircraft(6)
    assert len(controller.aircraftsList) == 6

    sorted_x = Coordinate.sorted_arcrafts_by_x(controller.aircraftsList)
    sorted_y = Coordinate.sorted_aircrafts_by_y(controller.aircraftsList)

    res = closest_pair_divide_and_conquer(sorted_x, sorted_y)
    assert res is not None
    assert res.aircraft1 is not None and res.aircraft2 is not None
    assert res.distance >= 0
