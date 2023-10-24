# Saisie des informations personnelles
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
age = int(input("Entrez votre âge : "))
taille = float(input("Entrez votre taille (en mètres) : "))

# Saisie de la liste des fruits préférés (séparés par des virgules)
fruits = input("Entrez une liste de vos fruits préférés (séparés par des virgules) : ")
liste_fruits = fruits.split(',')

# Saisie d'un message de salutation personnalisé
message = input("Entrez un message de salutation personnalisé : ")

# Saisie des propriétés d'un produit
nom_produit = input("Entrez le nom d'un produit : ")
prix = float(input("Entrez le prix du produit : "))
description = input("Entrez une description du produit : ")

# Conversion du nom de famille en majuscules
nom_en_majuscules = nom.upper()

# Affichage des informations saisies
print("\nInformations personnelles :")
print(f"Prénom : {prenom}")
print(f"Nom : {nom}")
print(f"Âge : {age} ans")
print(f"Taille : {taille} m")
print("\nFruits préférés :")
for fruit in liste_fruits:
    print(f"- {fruit.strip()}")  # Utilise strip() pour supprimer les espaces inutiles

print("\nMessage de salutation personnalisé :")
print(message)

print("\nPropriétés du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix : {prix} euros")
print(f"Description : {description}")

print("\nNom de famille en majuscules :")
print(nom_en_majuscules)
