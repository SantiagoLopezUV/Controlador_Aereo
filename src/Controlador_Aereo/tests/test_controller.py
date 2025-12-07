from Controlador_Aereo.controller.ControllerAircraft import ControllerAircraft


def main():
    print("Test Controlador Aereo")
    controller = ControllerAircraft()
    print("Generando aviones con coordenadas aleatorias...")
    controller.generateRandomCoordinateAircraft(3)
    
    controller.showAircrafts()


if __name__ == "__main__":
    main()