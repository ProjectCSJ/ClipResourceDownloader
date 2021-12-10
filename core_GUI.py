# =============================================================================
# Init
# =============================================================================
import pyglet as pg
from tkinter import ttk, Tk, Button, Entry, Label, messagebox
import core
fontname = "内海フォントJP--Regular"
pg.font.add_file("NKF.TTF")


# 視窗細項(window config)
def gen():
    global win
    win = Tk()
    win.title("ClipResourceDownloader v1.0")
    win.configure(bg="#64aaf0")


def click_download():
    mode_v = mode.get()
    url_v = url.get()
    x = (mode_v, url_v)
    core.download(x)


def ui():
    global url, mode
    gen()
    # 元件
    mode = ttk.Combobox(win, values=["playlist", "video"], font=(fontname, 25))
    url = Entry(win, font=(fontname, 30))
    start = Button(win, text="start", bg="#64aaf0", font=(
        fontname, 20), command=lambda: click_download())
    stop = Button(win, text="EXIT", bg="#64aaf0", font=(fontname, 20),command=win.destroy)
    don_t_do = Label(
        win, text="Do NOT download MEMBERS-ONLY video.", font=(fontname, 17), fg="red", bg="#64aaf0")
    # 排版
    don_t_do.pack(anchor="sw", padx=10, side="bottom")
    win.geometry("600x800")
    mode.pack(side="top", fill='x', pady=0)
    url.pack(pady=20, fill="x")
    start.place(x=200, y=110)
    stop.place(x=320, y=110)
    win.mainloop()


ui()
url, mode = None, None
