import time
import sys
import tkinter as tk


#Fenetre de jeu
root = tk.Tk()
root.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
root.geometry("1920x1080")
root.resizable(False, False)  # non-resizable width, height

#Menu principal
tk.Label(root, text = "PYTHONLANDE QUEST", fg="red4", bg="gray65", font=("arial",100)).pack(pady=100)
tk.Label(root, text = "Commencer", fg="black", bg="seashell3", font=("arial",70)).pack(pady= 20)
tk.Label(root, text = "Explication/But du jeu", fg="black", bg="seashell3", font=("arial",70)).pack(pady=20)
tk.Label(root, text = "Quitter le jeu", fg="black",bg="seashell3", font=("arial",70)).pack(pady=20)
#tk.Button(frm, text)

#Main loop (blocage ici tant qu'on n'a pas quitté)
root.mainloop()