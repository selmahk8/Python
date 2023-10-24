import tkinter as tk
import re

def inscription():
    pseudo = pseudo_entry.get()
    mot_de_passe = mot_de_passe_entry.get()
    email = email_entry.get()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("L'adresse e-mail n'est pas valide")
    else:
        print("Pseudo:", pseudo)
        print("Mot de passe:", mot_de_passe)
        print("Email:", email)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon interphase graphique")
fenetre.geometry("400x300")

# Création des étiquettes et des zones de texte
pseudo_label = tk.Label(fenetre, text="Pseudo:")
pseudo_label.pack()
pseudo_entry = tk.Entry(fenetre)
pseudo_entry.pack()

# Espace entre les zones de texte
espace_label1 = tk.Label(fenetre, text="")
espace_label1.pack()

mot_de_passe_label = tk.Label(fenetre, text="Mot de passe:")
mot_de_passe_label.pack()
mot_de_passe_entry = tk.Entry(fenetre, show="*")  # Pour cacher le mot de passe
mot_de_passe_entry.pack()

# Espace entre le mot de passe et l'email
espace_label2 = tk.Label(fenetre, text="")
espace_label2.pack()

email_label = tk.Label(fenetre, text="Email:")
email_label.pack()
email_entry = tk.Entry(fenetre)
email_entry.pack()

# Espace entre l'email et le bouton Valider
espace_label3 = tk.Label(fenetre, text="")
espace_label3.pack()

# Bouton pour valider l'inscription
valider_button = tk.Button(fenetre, text="Valider", command=inscription)
valider_button.pack()

fenetre.mainloop()
