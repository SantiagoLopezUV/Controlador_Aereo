# Controlador Aéreo

Proyecto universitario para la materia Analisis de Algoritmos.

Diseñado para identificar parejas de aviones más cercanas y detectar riesgo de colisión, utilizando la estrategia algorítmica Dividir y Vencer.

El proyecto está construido con buenas prácticas profesionales, integración continua, pruebas automatizadas y estructura lista para escalar.


## Estructura del Proyecto

```css
controlador-aereo/
├── src/
│   └── controlador_aereo/
│       ├── __init__.py
│       ├── main.py
│       ├── algorithms/
│       │   ├── __init__.py
│       │   └── code.py
|       ├── controller/
|       |   ├── __init__.py
|       |   └── ControllerAircraft.py
│       ├── model/
│       │   ├── __init__.py
│       │   ├── Aircraft.py
|       |   ├── ClosestPairResult.py
|       |   └── Coordinate.py
|       ├── tests/
|       |   ├── test_integration.py
│       |   └── test_unit.py
│       ├── utils/
│       │   ├── __init__.py
|       |   ├── theme.py
│       │   └── viewHandler.py
│       └── view/
│           ├── __init__.py
│           ├── flightSky.py
│           └── initPanel.py
|
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── README.md
└── .github/
    └── workflows/
        └── python-ci.yml
```


## 🐍 Lenguaje
<a href="https://www.python.org/"> <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" alt="Python Logo" width="50"> </a>

Python 3.12 es el lenguaje principal del proyecto, elegido por su claridad, velocidad de desarrollo y gran ecosistema de librerías científicas.

## 🛠️ Herramientas de Desarrollo
<a href="https://code.visualstudio.com/"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/9a/Visual_Studio_Code_1.35_icon.svg" alt="VSCode Logo" width="45"> </a>

Visual Studio Code se usa como editor principal gracias a:

- Excelente integración con Python

- Manejo sencillo de entornos virtuales (.venv)

- Extensiones útiles: Pylance, Black Formatter, GitHub

- Integración nativa con Git y GitHub


## 🚀 Objetivo del Sistema

El objetivo es diseñar un controlador aéreo que detecte las posibles colisiones aereas.
- El sistema va a procesar una lista de aeronaves (aviones) con posiciones en 2D.
- Debe encontrar las dos aeronaves mas cercanas entre si.
- Detectar posibles riesgos de colisión, encontrando la distancia mínima.
- Implementar la solución con Dividir y Vencer.


## ▶️ Cómo ejecutar el proyecto

1. Crear entorno virtual

    ```bash
    python -m venv .venv
    ```

2. Activarlo (Windows)

    ```bash
    .venv\Scripts\activate
    ```

3. Instalar Dependencias
    ```bash
    pip install -r requirements.txt
    ```

4. Ejecutar la Aplicación
    ```bash
    python src/controlador_aereo/main.py
    ```

5. Ejecutar Tests
    ```bash
    pytest
    ```


## 🔄 Integración Continua (GitHub Actions)

Este proyecto incluye un workflow que:

- Usa Python 3.12

- Instala dependencias

- Ejecuta pruebas

- Verifica que todo funciona antes de permitir un merge

Archivo: .github/workflows/python-ci.yml


## Autores

<table> <tr> <td align="center"> <a href="https://github.com/SantiagoLopezUV"> <img src="https://github.com/SantiagoLopezUV.png?size=120" width="120" height="120" style="border-radius: 50%;" /> <br> <sub><b>Santiago López</b></sub> </a> </td> <td align="center"> <a href="https://github.com/JulianAndresRojasPalacio"> <img src="https://github.com/JulianAndresRojasPalacio.png?size=120" width="120" height="120" style="border-radius: 50%;" /> <br> <sub><b>Julian Andrés Rojas Palacio</b></sub> </a> </td> </tr> </table>


## 📘 Licencia

Proyecto académico. Uso libre con fines educativos.