from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Controlador_Aereo.utils.viewHandler import templ_handler
from Controlador_Aereo.utils.theme import APP_BG, TITLE_FONT, STYLE_CARD, CARD_BG, NORMAL_FONT


def main():
    root = Tk()
    root.title("Air Traffic Controller System")
    root.resizable(False, False)
    try:
        root.iconbitmap('src/Controlador_Aereo/assets/airplane_icon.ico')
    except Exception:
        pass

    frame_style = 'TFrame'
    style = ttk.Style()
    style.configure(frame_style, background=CARD_BG)

    root.configure(background=CARD_BG)

    container = ttk.Frame(root, padding=20, style=frame_style)
    container.pack(fill='both', expand=True)

    dynamic_frame = ttk.Frame(container, style=frame_style, padding=10, width=760, height=420)
    dynamic_frame.pack(expand=True)
    dynamic_frame.pack_propagate(False)

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