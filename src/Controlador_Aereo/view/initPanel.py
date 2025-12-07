from tkinter import ttk
from Controlador_Aereo.utils.theme import (TITLE_FONT,
                                            NORMAL_FONT, 
                                            SUBTITLE_FONT, 
                                            PADDING)

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
        self.build_view()

    def build_view(self):
        """Creates the initial view for the application."""
        
        title = ttk.Label(
            self,
            text="Welcome to the Air Traffic Controller System",
            font=(TITLE_FONT)
            )
        title.grid(row=0, column=0, padx=PADDING, pady=PADDING)
        
        info = ttk.Label(
            self,
            text="Please use the menu to navigate through the system.",
            font=(NORMAL_FONT)
            )
        info.grid(row=1, column=0, padx=PADDING, pady=PADDING)
    