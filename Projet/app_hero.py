import time
import sys
import tkinter as tk

#Frame détaillé du menu principale
class Frame_Accueil(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self, text="PYTHONLAND QUEST", fg="red4", bg="gray65", font=("arial", 100)).pack(pady=100)
        tk.Button(self, text="Commencer", fg="black", bg="seashell3", font=("arial", 70)).pack(pady=20)
        tk.Button(self, text="Explication/But du jeu", fg="black", bg="seashell3", font=("arial", 50)).pack(pady=20)
        tk.Button(self, text="Quitter le jeu", fg="black", bg="seashell3", font=("arial", 50),command=parent.destroy).pack(pady=20)

#Menu Explication
class But_Jeu(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.label = tk.Label(self, text= "Explication", bg="white", font=("arial", 100))
        self.label.place(x=20,y=20)

#Commencement du Jeu
class Start_Game(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        pass

#Fenetre de jeu
root = tk.Tk()
root.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
root.geometry("1920x1080")
root.resizable(True, True)  # non-resizable width, height

#Menu principal
main_window = Frame_Accueil(root)
main_window.pack(fill='both',expand=True)

#Main loop (blocage ici tant qu'on n'a pas quittée)
root.mainloop()