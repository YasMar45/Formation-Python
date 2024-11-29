import tkinter
import tkinter as tk

class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

# Fenetre de jeu
root = tk.Tk()
root.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
root.geometry("1920x1080")
root.resizable(True, True)  # non-resizable width, height

# Menu principal
main_window = Game(root)
main_window.pack(fill='both', expand=True)

# Main loop (blocage ici tant qu'on n'a pas quittée)
root.mainloop()

