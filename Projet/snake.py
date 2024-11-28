import tkinter as tk
import random

# Configuration du jeu
largeur = 400
hauteur = 400
taille_segment = 20
vitesse = 100

# Direction initiale
direction = 'Bas'

# Liste pour stocker les positions du serpent
snake_positions = [(100, 100), (80, 100), (60, 100)]


# Générer une position aléatoire pour la pomme
def generer_pomme():
    return (random.randint(0, (largeur - taille_segment) // taille_segment) * taille_segment,
            random.randint(0, (hauteur - taille_segment) // taille_segment) * taille_segment)


pomme_position = generer_pomme()


# Fonction pour changer la direction
def changer_direction(nouvelle_direction):
    global direction
    opposites = {'Haut': 'Bas', 'Bas': 'Haut', 'Gauche': 'Droite', 'Droite': 'Gauche'}
    if nouvelle_direction != opposites.get(direction):
        direction = nouvelle_direction


# Mouvement du serpent
def mouvement():
    global pomme_position
    x, y = snake_positions[0]

    if direction == 'Haut':
        y -= taille_segment
    elif direction == 'Bas':
        y += taille_segment
    elif direction == 'Gauche':
        x -= taille_segment
    elif direction == 'Droite':
        x += taille_segment

    # Nouvelle tête du serpent
    nouvelle_tete = (x, y)

    # Vérification de collision avec les murs ou avec lui-même
    if (x < 0 or x >= largeur or y < 0 or y >= hauteur or nouvelle_tete in snake_positions):
        return

    # Insérer la nouvelle tête au début de la liste
    snake_positions.insert(0, nouvelle_tete)

    # Vérification si le serpent mange la pomme
    if nouvelle_tete == pomme_position:
        pomme_position = generer_pomme()
    else:
        snake_positions.pop()

    # Redessiner le serpent et la pomme
    canvas.delete('all')
    canvas.create_rectangle(pomme_position[0], pomme_position[1], pomme_position[0] + taille_segment,
                            pomme_position[1] + taille_segment, fill='red')
    for segment in snake_positions:
        canvas.create_rectangle(segment[0], segment[1], segment[0] + taille_segment,
                                segment[1] + taille_segment, fill='green')

    # Suspend l'exécution du mouvement et réappel après `vitesse` ms
    root.after(vitesse, mouvement)


# Initialisation de l'interface de jeu
root = tk.Tk()
root.title("Jeu du Snake")
canvas = tk.Canvas(root, width=largeur, height=hauteur, bg='black')
canvas.pack()

root.bind('<Up>', lambda _: changer_direction('Haut'))
root.bind('<Down>', lambda _: changer_direction('Bas'))
root.bind('<Left>', lambda _: changer_direction('Gauche'))
root.bind('<Right>', lambda _: changer_direction('Droite'))

# Démarrage du mouvement
mouvement()

# Lancement de la boucle principale
root.mainloop()

