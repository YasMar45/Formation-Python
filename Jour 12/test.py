import tkinter as tk

# Import de module dans le même dossier
import animated_demo


class App(tk.Tk):
    def __init__(self):
        """
            Application simple qui propose un menu et la démonstration animée, chacun dans son propre Frame.
        """
        super().__init__()
        self.title("Tk: Menu and Frames")
        self.geometry("500x400")
        self.resizable(False, False)  # non-resizable width, height

        # Ajout des 2 frames ; au départ, seul le menu sera visible, mais ça pourra changer par la suite

        self.main_menu = MainMenuFrame(self)
        # C'est le parent qui décide que le frame (enfant) peut s'étendre et prendre toute la place
        self._set_frame_enabled(self.main_menu, True)

        self.animated_demo = animated_demo.AnimatedDemoFrame(
            self, bg="red", button_menu_callback=self.on_back_to_menu_click
        )
        self._set_frame_enabled(self.animated_demo, False)

    def _set_frame_enabled(self, frame: tk.Frame, is_enabled: bool):
        if is_enabled:
            frame.pack(fill='both', expand=True)
        else:
            frame.pack_forget()
        self.update()  # Force display updates

    def on_animated_demo_click(self):
        # On cache le menu et on affiche le frame de démonstration (défini dans animated_demo.py)
        self._set_frame_enabled(self.main_menu, False)
        self._set_frame_enabled(self.animated_demo, True)

    def on_back_to_menu_click(self):
        self._set_frame_enabled(self.animated_demo, False)
        self._set_frame_enabled(self.main_menu, True)


class MainMenuFrame(tk.Frame):
    def __init__(self, parent: App, bg="blue"):
        tk.Frame.__init__(self, parent, bg=bg)
        self.parent = parent  # On garde une référence vers le parent, pour pouvoir lui transmettre des callbacks

        # Pour chaque widget, on procède en 2 étapes :
        #    a) on instancie le widget lui-même
        #    b) on le place dans son parent (la main window)
        self.label = tk.Label(self, text="This is the main menu", bg="lightgray")
        self.label.place(x=20.0, y=20.0)  # voir aussi: pack(...), grid(...)

        # - - - Build interactive widgets (with callbacks) - - -
        self.button = tk.Button(self, text="Animated Demo (in its own frame)", command=self.on_animated_demo_click)
        self.button.place(x=20.0, y=50.0)  # voir aussi: pack(...), grid(...)

    def on_animated_demo_click(self):
        print("on_animated_demo_click(): on transmet la demande de changement du menu vers le parent...")
        self.parent.on_animated_demo_click()


if __name__ == "__main__":

    app = App()
    app.mainloop()  # Attention, fonction bloquante
    a = 0  # par exemple, cette ligne ne sera jamais exécutée
