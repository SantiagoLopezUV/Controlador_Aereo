from Controlador_Aereo.view.initPanel import ViewInitial
from Controlador_Aereo.controller.ControllerAircraft import ControllerAircraft


GLOBAL_CONTROLLER = ControllerAircraft()


NORMAL_ACCESS_TEMPL_DIC = {'initial': ViewInitial,
                            'sky_flight': None}



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
    
    if choice == 'sky_flight':
        from Controlador_Aereo.view.flightSky import sky_template as ViewClass
    else:
        ViewClass = NORMAL_ACCESS_TEMPL_DIC.get(choice)

    if ViewClass is None:
        raise KeyError(f"Unknown template choice: {choice}")

    # Instantiate view; pass only the dynamic_frame. Views should access GLOBAL_CONTROLLER if needed.
    view = ViewClass(dynamic_frame)
    
    view.grid(row=0, column=0, sticky="nwes")
    
    return view

