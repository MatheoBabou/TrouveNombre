import random

def partie():
  bas=0
  haut=100
  nombre_inconnu=random.randint(bas,haut)
  # print(f"Mon nombre inconnu est {nombre_inconnu}")
  trouve_nombre=-1
  essaie=0
  while trouve_nombre!=nombre_inconnu :
    essaie +=1
    reponse=input("Essayer un nombre ? ")
    trouve_nombre = int(reponse)
    if trouve_nombre<nombre_inconnu :
      print("Mon nombre est plus grand réessaye.")
    if trouve_nombre>nombre_inconnu :
      print("Mon nombre est plus petit réessaye.")

  print(f"Bien joué tu as trouvé, mon nombre était bien {nombre_inconnu}.Tu as réussi en {essaie} essaie.")

  return essaie

print("Bonjour tous le monde.")
print("On va joué a un jeu je vais choisire un nombre et vous allé devoire le deviner.")
rejouer="oui"
while rejouer=="oui":
  nb_essai = partie()
  rejouer=input("Voulez-vous rejouer? ")


