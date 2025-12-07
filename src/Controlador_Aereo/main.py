#from model.Coordinate import Coordinate
#from model.Aircraft import  Aircraft
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Controlador_Aereo.utils.viewHandler import templ_handler
from Controlador_Aereo.utils.theme import APP_BG, TITLE_FONT, STYLE_CARD, CARD_BG, NORMAL_FONT


def main():
    root = Tk()
    root.title("Air Traffic Controller System")
    root.resizable(False, False)
    # Try to set an application icon if available; ignore if missing
    try:
        root.iconbitmap('src/Controlador_Aereo/assets/airplane_icon.ico')
    except Exception:
        pass

    frame_style = 'TFrame'
    style = ttk.Style()
    # Use white card background for app
    style.configure(frame_style, background=CARD_BG)

    # Overall background white
    root.configure(background=CARD_BG)

    # Simplified layout: single centered container with a dynamic frame
    container = ttk.Frame(root, padding=20, style=frame_style)
    container.pack(fill='both', expand=True)

    # create a centered card for dynamic content
    # Fixed-size card for dynamic content (centered) - match flightSky canvas width/height
    dynamic_frame = ttk.Frame(container, style=frame_style, padding=10, width=760, height=420)
    dynamic_frame.pack(expand=True)
    # Prevent children from shrinking the frame
    dynamic_frame.pack_propagate(False)

    # Call the template handler to populate dynamic_frame
    templ_handler('initial', dynamic_frame)
    root.mainloop()

def center_window(root):
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    x = (root.winfo_screenwidth() // 2) - (window_width // 2)
    y = (root.winfo_screenheight() // 2) - (window_height // 2)
    
    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


if __name__ == "__main__":
    main()