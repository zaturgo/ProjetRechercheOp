nombre_capteurs = 0
nombre_zones = 0
capteurs_zones_duree_vie = []
erreur = False

with open('test', 'r') as fichier_a_lire:
    nombre_capteurs = int(fichier_a_lire.readline().strip())
    nombre_zones = int(fichier_a_lire.readline().strip())
    duree_vie_capteur = fichier_a_lire.readline().split()

    if (len(duree_vie_capteur) != nombre_capteurs):
        erreur = True
    else:
        for capteur in range(0, nombre_capteurs):
            zones_ligne = list(map(int, fichier_a_lire.readline().split()))
            zones_ligne.sort()
            print(zones_ligne)

            valeurs_ligne = []
            for zone in range(1, nombre_zones + 1):
                print(zones_ligne)
                if len(zones_ligne) > 0 and zones_ligne[0] == zone:
                    valeurs_ligne.append(int(duree_vie_capteur[capteur]))
                    zones_ligne.pop(0)
                else:
                    valeurs_ligne.append(-1)
            capteurs_zones_duree_vie.append(valeurs_ligne)

print(capteurs_zones_duree_vie)

if not erreur:
    print("Ok !")
