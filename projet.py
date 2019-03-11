from random import randint

nombre_capteurs = 0
nombre_zones = 0
capteurs_zones_duree_vie = []
erreur_lecture = False

def lire_fichier(emplacement):
    global nombre_capteurs, nombre_zones, erreur_lecture, capteurs_zones_duree_vie
    with open(emplacement, 'r') as fichier_a_lire:
        nombre_capteurs = int(fichier_a_lire.readline().strip())
        nombre_zones = int(fichier_a_lire.readline().strip())
        duree_vie_capteur = fichier_a_lire.readline().split()

        if (len(duree_vie_capteur) == nombre_capteurs):
            for capteur in range(0, nombre_capteurs):
                zones_ligne = list(map(int, fichier_a_lire.readline().split()))
                zones_ligne.sort()

                valeurs_ligne = []
                for zone in range(1, nombre_zones + 1):
                    if len(zones_ligne) > 0 and zones_ligne[0] == zone:
                        valeurs_ligne.append(int(duree_vie_capteur[capteur]))
                        zones_ligne.pop(0)
                    else:
                        valeurs_ligne.append(-1)
                capteurs_zones_duree_vie.append(valeurs_ligne)
        else:
            erreur_lecture = True


def trouver_configurations_elementaires_sur_grands_fichiers(nombre_iterations = 10):
    if nombre_iterations > nombre_capteurs * nombre_zones / 2:
        nombre_iterations = nombre_capteurs

    if nombre_capteurs < 5 or nombre_zones < 5:
        nombre_iterations = 0

    configurations_elementaires = []

    # Boucle pour l'obtention du nombre de résultats souhaités
    while nombre_iterations > 0:
        # Boucle permettant de trouver une configuration élémentaire
        capteur_par_zone_a_couvrir = [-1] * nombre_zones
        for zone in range(1, nombre_zones + 1):

            # Vérification de l'état de la zone (couverte par un capteur ou non)
            if capteur_par_zone_a_couvrir[zone - 1] == -1:

                # Choix aléatoire d'un capteur couvrant la zone
                capteur = randint(0, nombre_capteurs - 1)
                while not list(zip(*capteurs_zones_duree_vie))[zone - 1][capteur] > 0:
                    capteur = randint(0, nombre_capteurs - 1)

                # Ajout de toutes les zones couvertes par le capteur à la
                # configuration élémentaire en cours de création
                for zone_capteur in range(zone, nombre_zones + 1):
                    if capteurs_zones_duree_vie[capteur][zone_capteur - 1] > 0:
                        capteur_par_zone_a_couvrir[zone_capteur - 1] = capteur

        # Suppression des doublons des capteurs inclus plusieurs fois
        # et tri par ordre croissant
        capteur_par_zone_a_couvrir = list(set(capteur_par_zone_a_couvrir))

        # Si la configuration élémentaire n'a pas encore été trouvée,
        # ajout aux autres configurations élémentaires déjà trouvées.
        if capteur_par_zone_a_couvrir not in configurations_elementaires:
            configurations_elementaires.append(capteur_par_zone_a_couvrir)
            nombre_iterations -= 1
    return configurations_elementaires

lire_fichier('test')
print(capteurs_zones_duree_vie)
if not erreur_lecture:
    print("Lecture effectuée avec succès !")
print(trouver_configurations_elementaires_sur_grands_fichiers())
