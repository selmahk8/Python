import tkinter as tk

# Fonctions pour les opérations
def addition():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultat.set(num1 + num2)

def soustraction():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultat.set(num1 - num2)

def multiplication():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultat.set(num1 * num2)

def division():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        resultat.set(num1 / num2)
    else:
        resultat.set("Division par zéro")

# Créer une fenêtre
window = tk.Tk()
window.title("Calculatrice")
window.geometry("400x300")

# Entrées
label_num1 = tk.Label(window, text="Nombre 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Nombre 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Boutons pour les opérations
btn_addition = tk.Button(window, text="Addition", command=addition)
btn_addition.pack()

btn_soustraction = tk.Button(window, text="Soustraction", command=soustraction)
btn_soustraction.pack()

btn_multiplication = tk.Button(window, text="Multiplication", command=multiplication)
btn_multiplication.pack()

btn_division = tk.Button(window, text="Division", command=division)
btn_division.pack()

# Résultat
resultat = tk.StringVar()
label_resultat = tk.Label(window, textvariable=resultat)
label_resultat.pack()

# Lancer l'interface graphique
window.mainloop()
