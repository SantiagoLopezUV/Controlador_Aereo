from tkinter import ttk, Canvas, messagebox
from Controlador_Aereo.utils.theme import (FLIGHT_COLOR, TITLE_FONT,
                                            NORMAL_FONT, PADDING)
from Controlador_Aereo.utils import viewHandler
from Controlador_Aereo.algorithms.code import closest_pair_divide_and_conquer
from Controlador_Aereo.model.Coordinate import Coordinate


class sky_template(ttk.Frame):
    def __init__(self, dynamic_frame):
        super().__init__(dynamic_frame)
        self.dynamic_frame = dynamic_frame
        # Fix size to match the dynamic frame and prevent propagation
        try:
            self.config(width=800, height=480)
            self.grid_propagate(False)
        except Exception:
            pass
        self.build_view()
        # Automatically draw when the view is created so no separate "Refrescar" is required
        self.draw_aircrafts()

    def build_view(self):
        title = ttk.Label(self, text="RADAR AVIONES", font=TITLE_FONT)
        title.grid(row=0, column=0, padx=PADDING, pady=(PADDING, 2), columnspan=3)

        btn_back = ttk.Button(self, text="Volver", command=self.back)
        btn_back.grid(row=0, column=0, sticky="w", padx=PADDING, pady=(PADDING, 2))

        # Search button to compute closest pair
        btn_search = ttk.Button(self, text="Calcular par más cercano", command=self.calculate)
        btn_search.grid(row=0, column=2, sticky="e", padx=PADDING, pady=(PADDING, 2))

        self.canvas = Canvas(self, width=760, height=420, bg=FLIGHT_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=3, padx=PADDING, pady=PADDING)

        self.result_label = ttk.Label(self, text="", font=NORMAL_FONT)
        self.result_label.grid(row=2, column=0, columnspan=3, padx=PADDING, pady=(0, PADDING))

    def back(self):
        viewHandler.templ_handler('initial', self.master)

    def draw_aircrafts(self):
        # Clear canvas
        self.canvas.delete('all')

        aircrafts = viewHandler.GLOBAL_CONTROLLER.aircraftsList
        if not aircrafts:
            self.result_label.config(text="No hay aviones para mostrar")
            return

        # Assume coordinates are 0..100 and scale to canvas
        w = int(self.canvas['width'])
        h = int(self.canvas['height'])

        for aircraft in aircrafts:
            try:
                x = aircraft.coordinate.x
                y = aircraft.coordinate.y
            except Exception:
                continue
            cx = int(x / 100 * w)
            cy = int(y / 100 * h)
            r = 8
            self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill='red', outline='red', width=2)
            self.canvas.create_text(cx + 14, cy, text=f"AV{aircraft.numPlane}", anchor='w', fill='black')
        self.result_label.config(text=f"Total aviones: {len(aircrafts)}")

    def calculate(self):
        aircrafts = viewHandler.GLOBAL_CONTROLLER.aircraftsList
        if len(aircrafts) < 2:
            messagebox.showinfo("Resultado", "Se necesitan al menos 2 aviones para calcular la distancia mínima.")
            return

        # Prepare sorted lists
        ax = Coordinate.sorted_arcrafts_by_x(aircrafts)
        ay = Coordinate.sorted_aircrafts_by_y(aircrafts)

        result = closest_pair_divide_and_conquer(ax, ay)

        if result is None or result.aircraft1 is None or result.aircraft2 is None:
            messagebox.showinfo("Resultado", "No se pudo calcular el par más cercano")
            return

        a1 = result.aircraft1
        a2 = result.aircraft2
        dist = result.distance

        text = f"Distancia mínima: {dist:.2f} — AV{a1.numPlane} y AV{a2.numPlane}"
        self.result_label.config(text=text)
        messagebox.showinfo("Resultado", text)