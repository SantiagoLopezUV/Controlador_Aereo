from Controlador_Aereo.view.initPanel import ViewInitial
from Controlador_Aereo.view.flightSky import sky_template


NORMAL_ACCESS_TEMPL_DIC = {'initial': ViewInitial,
                            'sky_flight' : sky_template}



def grid_rows_columns_config(dynamic_frame, ratio):
    """
    This method configures the rows and columns within a frame to
    modify their proportion.
    """
    columns, rows = dynamic_frame.grid_size()
    for i in range(rows):
        dynamic_frame.grid_rowconfigure(i, weight=ratio)
    for j in range(columns):
        dynamic_frame.grid_columnconfigure(j, weight=ratio)


def destroy_widgets(dynamic_frame):
    """This method removes all widgets from the frame."""
    for widget in dynamic_frame.winfo_children():
        widget.destroy()


def templ_handler(choice, dynamic_frame):
    destroy_widgets(dynamic_frame)
    
    ViewClass = NORMAL_ACCESS_TEMPL_DIC[choice]
    
    view = ViewClass(dynamic_frame)
    view.grid(row=0, column=0, sticky="nwes")
    
    return view

