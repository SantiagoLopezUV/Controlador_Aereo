import tkinter as tk
from tkinter import ttk
from Controlador_Aereo.utils.theme import (TITLE_FONT_MAIN, APP_BG, TEXT_COLOR, CARD_BG,
                                            NORMAL_FONT, SMALL_FONT,MARGIN,
                                            PADDING)
from Controlador_Aereo.utils import viewHandler

class ViewInitial(ttk.Frame):
    def __init__(self, dynamic_frame):
        super().__init__(dynamic_frame)
        self.controller = viewHandler.GLOBAL_CONTROLLER
        self.dynamic_frame = dynamic_frame
        try:
            self.config(width=760, height=420)
            self.grid_propagate(False)
        except Exception:
            pass
        self.build_view()

    def build_view(self):
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
            x = 50
            if n <= 0 or n > x:
                raise ValueError()
        except Exception:
            return
        
        self.controller.aircraftsList.clear()
        self.controller.generateRandomCoordinateAircraft(n)
        
        viewHandler.templ_handler('sky_flight', self.dynamic_frame)
        
        