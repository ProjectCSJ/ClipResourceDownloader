import pyglet as pg
from tkinter import Tk, Label, Button
import core
from core_GUI import ui

fontname = "内海フォントJP--Regular"
pg.font.add_file("NKF.TTF")


select = Tk()
select.title("Mode Select")
select.configure(bg="#64aaf0")
select.geometry("400x400")
def GUI_open():
    select.deiconify()
    ui()
    select.destroy()
def CLI_open():
    select.deiconify()
    core.download_cli()

def startup():
    label_usage = Label(select,text="Please select what UI do you want to use.", font=(
        fontname, 12), bg="#64aaf0")
    label_usage.pack()
    GUI=Button(select,text="GUI",bg="#64aaf0",font=(fontname, 20),command=lambda :GUI_open())
    GUI.place(x=70,y=350)
    CLI=Button(select,text="CLI",bg="#64aaf0",font=(fontname, 20),command=lambda :CLI_open())
    CLI.place(x=155,y=350)
    EXIT=Button(select,text="EXIT",bg="#64aaf0",font=(fontname, 20),command=select.destroy)
    EXIT.place(x=240,y=350)
    select.mainloop()
startup()