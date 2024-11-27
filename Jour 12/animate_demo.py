import tkinter as tk
from time import time
import math


class AnimatedDemoFrame(tk.Frame):
    def __init__(self, parent, bg="white", button_menu_callback=None):
        """

        :param parent: Objet tkinter parent (e.g. fenêtre, frame, ...) de ce frame
        :param bg: Background color
        :param button_menu_callback: Fonction (optionnelle) appelée lorsque l'on appuie sur le bouton "back to menu"
        """
        super().__init__(parent, bg=bg)
        self.button_menu_callback = button_menu_callback

        # - - - Build display-only widgets - - -
        # Pour chaque widget, on procède en 2 étapes :
        #    a) on instancie le widget lui-même
        #    b) on le place dans son parent (la main window)
        self.label = tk.Label(self, text="This is a label", bg="lightgray")
        self.label.place(x=20.0, y=20.0)  # voir aussi: pack(...), grid(...)

        # - - - Build interactive widgets (with callbacks) - - -
        self.button = tk.Button(self, text="Click me", command=self.on_button_clicked)
        self.button.place(x=20.0, y=50.0)  # voir aussi: pack(...), grid(...)
        self.button_menu = tk.Button(self, text="Back to menu", command=self.on_button_menu_clicked)
        self.button_menu.place(x=320.0, y=320.0)  # voir aussi: pack(...), grid(...)

        # Si on veut utiliser des listes (1D ou 2D) widgets créés dynamiquement, on va utiliser "bind event"
        # print("De quelle taille devra être la matrice de boutons ?")
        self.widgets_matrix_size = 3  # int(input())  # TODO gérer éventuelle erreur de parsing
        self.widgets_matrix = []
        for row in range(self.widgets_matrix_size):
            self.widgets_matrix.append([])  # On ajoute une nouvelle ligne (pour l'instant, c'est juste une liste vide)
            for col in range(self.widgets_matrix_size):  # Puis on ajoute les éléments dans la dernière ligne
                new_widget = tk.Label(self, text="0")  # (on pourrait ne plus utiliser des matrices, mais des images)
                # simple, mais pas très propre... il faudrait créer notre propre classe qui hérite de tk.Button
                #    ici, on rajoute sauvagement des attributs
                new_widget.matrix_row, new_widget.matrix_col = row, col
                new_widget.bind('<Button>', self.on_matrix_click_event)  # <Button> désigne n'importe bouton de la souris
                self.widgets_matrix[-1].append(new_widget)
                new_widget.place(x=(200.0 + col * 30.0), y=(100.0 + row * 30.0))

        # Widget avec image - qu'on peut déplacer avec la souris (avec animation pendant le déplacement)
        self.img = tk.PhotoImage(file='./assets/python_xsmall.png')
        self.image_widget = tk.Label(self, image=self.img)
        self.image_widget.place(x=50.0, y=250.0)
        self.is_dragging_image = False
        self.image_widget.bind('<Button-1>', self.on_image_click)
        self.image_widget.bind('<B1-Motion>', self.on_image_motion)
        self.image_widget.bind('<ButtonRelease-1>', self.on_image_release)

        # Other attributes
        self.clicks_count = 0

        # On lance un auto-update périodique (fonction qui s'appellera elle-même par la suite)
        self.after(16, self.update)

    def on_button_clicked(self):
        """ Callback, appelée suite au clic sur le bouton correspondant """
        self.clicks_count += 1
        self.label.config(text=f'The button has been clicked {self.clicks_count} times')

    def on_button_menu_clicked(self):
        if self.button_menu_callback is not None:
            self.button_menu_callback()
        else:
            print("Aucun callback n'a été donné pour revenir au menu !")

    def on_matrix_click_event(self, event):
        # En utilisant le débugguer, on peut aller voir le contenu de l'event; il contient notamment le widget qui a
        # déclenché le callback
        row, col = event.widget.matrix_row, event.widget.matrix_col
        print(f"Le widget qu'on vient de cliquer est en position {row}, {col}")
        event.widget['text'] = str(int(event.widget['text']) + 1)

    def on_image_click(self, event):
        self.is_dragging_image = True
        print('Grabbed image')

    def on_image_motion(self, event):
        image_w, image_h = self.image_widget.winfo_width(), self.image_widget.winfo_height()
        #print(f"Image widget: w={self.image_widget.winfo_width()}, h={self.image_widget.winfo_height()} "
        #      f"x={self.image_widget.winfo_rootx()} y={self.image_widget.winfo_rooty()}")
        # sur macOS python3.7 : pointerx est en coordonnées de l'écran
        x_mouse, y_mouse = self.winfo_pointerx() - self.winfo_rootx(), self.winfo_pointery() - self.winfo_rooty()
        # On place le *centre* du widget sur la souris
        self.image_widget.place(x=x_mouse - image_w // 2, y=y_mouse - image_h // 2)

    def on_image_release(self, event):
        self.is_dragging_image = False
        self.image_widget['bg'] = "white"
        print("Dropped image")

    def update(self):
        """ Cette fonction update(...) va s'appeler elle-même toutes les 16ms. Cela permet d'animer
            automatiquement des objets (déplacements, changements couleur, ...). """
        if self.is_dragging_image:  # Oscillating background color (brightness only)
            l = 210 + int(math.cos(2.0 * 3.14 * 1.0 * time()) * 30.0)
            self.image_widget['bg'] = f"#{l:02x}{l:02x}{l:02x}"
        self.after(16, self.update)  # approx 60Hz update - will waste a looooot of CPU



if __name__ == "__main__":
    # On va ici construire une app très simple, juste pour tester notre frame

    # - - - Main window - - -
    root = tk.Tk()
    root.title("Tk: Animated Demonstration")
    root.geometry("500x400")
    root.resizable(False, False)  # non-resizable width, height

    # - - - Frame de démonstration - - -
    #frame = tk.Frame(root,bg='blue')
    frame = AnimatedDemoFrame(root, bg='white',button_menu_callback=root.destroy)
    frame.pack(fill='both', expand=True)

    # - - - Main loop (blocage ici tant qu'on n'a pas quitté)
    root.mainloop()

