# =============================================================================
# Init
# =============================================================================
import tkinter as tk
import pyglet as pg
fontname = "内海フォントJP--Regular"
pg.font.add_file("NKF.TTF")

def ui():
    gui = tk.Tk()
    gui.geometry("600x800")
    gui.title('ClipResourceDownloader v1.0')
    gui.configure(bg="#64aaf0")
    don_t_do = tk.Label(
        gui, text="Do NOT download MEMBERS-ONLY video.", font=(fontname, 17), fg="red", bg="#64aaf0")
    don_t_do.pack(anchor="sw", padx=10, side="bottom")
    gui.mainloop()


ui()
