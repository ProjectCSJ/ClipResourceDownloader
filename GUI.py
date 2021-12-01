import tkinter as tk

# =============================================================================
# This is a GUI generator
# =============================================================================


def GUI(sizeX, sizeY):
    gui = tk.Tk()

    gui.geometry("{}x{}".format(sizeX, sizeY))

    gui.title("Clip Resource Download GUI made by XD")

    gui.mainloop()
