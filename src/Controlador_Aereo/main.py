#from model.Coordinate import Coordinate
#from model.Aircraft import  Aircraft
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Controlador_Aereo.utils.viewHandler import templ_handler
from Controlador_Aereo.utils.theme import APP_BG, TITLE_FONT, STYLE_CARD


def main():
    root = Tk()
    root.title("Air Traffic Controller System")
    root.resizable(False, False)
    root.iconbitmap('src/Controlador_Aereo/assets/airplane_icon.ico')
    
    
    frame_style = 'TFrame'
    style = ttk.Style()
    style.configure(frame_style, background=APP_BG)
    
    frame_container = ttk.Frame(root)
    frame_container.grid_columnconfigure(0, weight=1, minsize=800)
    frame_container.grid_rowconfigure(0, weight=1, minsize=150)
    frame_container.grid_rowconfigure(1, weight=1, minsize=450)
    
    static_frame = ttk.Frame(frame_container, style=frame_style)
    image = Image.open('src/Controlador_Aereo/assets/airplane_icon.ico')
    image = image.resize((800, 150))
    img = ImageTk.PhotoImage(image)
    lbl_img = ttk.Label(static_frame, image=img, background=APP_BG)
    lbl_initial = ttk.Label(static_frame, text="Air Traffic Controller System",
                                font=(TITLE_FONT), background=APP_BG)
    dynamic_content_frame = ttk.Frame(frame_container, style=frame_style)
    
    dynamic_frame = ttk.Frame(dynamic_content_frame, style=STYLE_CARD)
    frame_container.grid(row=0, column=0, sticky="nwes")
    static_frame.grid(row=0, column=0, sticky="nwes")
    dynamic_content_frame.grid(row=0, column=1, sticky="nwes")
    dynamic_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_img.place(relx=0.5, rely=0.5, anchor=CENTER)
    lbl_initial.place(relx=0.5, rely=0.8, anchor=CENTER)
    
    center_window(root)
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
    
    
    

    # avion1 = Aircraft("AV001", Coordinate(10, 20))
    # avion2 = Aircraft("AV002", Coordinate(30, 15))
    # avion3 = Aircraft("AV003", Coordinate(5, 8))
    