print("coucou")

nombre_capteurs = 0
nombre_zones = 0
capteurs_zones_duree_vie = []
erreur = False

with open('test', 'r') as fichier_a_lire:
    nombre_capteurs = fichier_a_lire.readline().strip()
    nombre_zones = fichier_a_lire.readline().strip()
    duree_vie_capteur = fichier_a_lire.readline().split()

    if (len(duree_vie_capteur) != int(nombre_capteurs)):
        erreur = True
    else:
        for i in range(0, int(nombre_capteurs)):
            ligne = list(map(int, fichier_a_lire.readline().split()))
            ligne.sort()
            print(ligne)


if not erreur:
    print("Ok !")
