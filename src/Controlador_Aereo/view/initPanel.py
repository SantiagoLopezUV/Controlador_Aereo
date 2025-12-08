import tkinter as tk
from tkinter import ttk
from Controlador_Aereo.utils.theme import (TITLE_FONT_MAIN, APP_BG, TEXT_COLOR, CARD_BG,
                                            NORMAL_FONT, SMALL_FONT,MARGIN,
                                            PADDING)
from Controlador_Aereo.utils import viewHandler

"""
Initial view: provides an Entry to request a number of aircraft
and a button to generate them using the shared controller.
"""

"""
Imports:
- 'ttk' module from the 'tkinter' library for creating the Graphical
User Interface (GUI).
- 'templ_handler' method from the 'template_handler' module.

Purpose:
- Generates the primary template asigned to the dynamic_frame.
- Utilizes 'ttk' for creating graphical elements in the GUI.
- Implements 'templ_handler' for handling the templates in the application.
"""

class ViewInitial(ttk.Frame):
    def __init__(self, dynamic_frame):
        super().__init__(dynamic_frame)
        # Use the shared global controller from viewHandler
        self.controller = viewHandler.GLOBAL_CONTROLLER
        self.dynamic_frame = dynamic_frame
        # Fix size to match sky view and prevent propagation
        try:
            self.config(width=760, height=420)
            self.grid_propagate(False)
        except Exception:
            pass
        self.build_view()

    def build_view(self):
        """Creates the initial view for the application."""
        # Configure grid to center content
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        title = tk.Label(
            self,
            text="Controlador Aéreo",
            font=TITLE_FONT_MAIN,
            bg=CARD_BG,
            fg='black'
        )
        title.grid(row=0, column=0, columnspan=2, padx=PADDING, pady=(PADDING, 12), sticky='ew')

        infoSubtittle = tk.Label(
            self,
            text="Introduce la cantidad de aviones a generar:",
            font=NORMAL_FONT, fg=TEXT_COLOR, bg=CARD_BG
        )
        infoSubtittle.grid(row=1, column=0, padx=PADDING, pady=(2, PADDING), sticky="e")

        self.entry_num_aircraft = ttk.Entry(self, width=10)
        self.entry_num_aircraft.grid(row=2, column=1, padx=MARGIN, pady=(PADDING, 16), sticky="w")

        btn_generate = tk.Button(
            self,
            text="Generar aviones",
            command=self.generate,
            bg=APP_BG, fg=CARD_BG,
            font=NORMAL_FONT,
            width=18,
            relief='raised', bd=2
        )
        btn_generate.grid(row=3, column=0, columnspan=2, padx=PADDING, pady=(PADDING, 16))


        hint = tk.Label(self, text="Los aviones aparecerán en la vista del cielo.", font=SMALL_FONT, bg=CARD_BG, fg=TEXT_COLOR)
        hint.grid(row=10, column=0, columnspan=2, padx=PADDING, pady=(12, PADDING))

    def generate(self):
        """Handle generate button: read number, create aircraft and switch view."""
        try:
            n = int(self.entry_num_aircraft.get())
            if n <= 0:
                raise ValueError()
        except Exception:
            # invalid input: ignore or show a minimal feedback
            return
        
        self.controller.aircraftsList.clear()
        self.controller.generateRandomCoordinateAircraft(n)
        
        viewHandler.templ_handler('sky_flight', self.dynamic_frame)
        
        