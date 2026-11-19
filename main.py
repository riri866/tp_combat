import random
import sys
from personnage import DIEUX_GREC, TITAN
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["tp_combat"]
colection_dieux = db["DIEUX_GREC"]
colection_titan = db["TITAN"]
colection_scores = db["scores"]

#MAIN
def main():
    initialiser_bdd()
    # boucle infini
    while True:
        # récupérer un choix valide
        choix = recupere_choix_valide(["Jouer", "Afficher les scores", "Quitter"])
        # si le choix est la première option
        if choix == 1:
            # lancer la première option
            premiere_option()
        # sinon si le choix est la deuxième option
        elif choix == 2 :
            # lancer la deuxième option
            deuxieme_option()
        # sinon
        else:
            # lancer quitter
            troisieme_option()

# pour mettee liste dans mongo db
def initialiser_bdd():
#   si collection dieux vide
    if colection_dieux.count_documents({}) == 0:
#       # copie et insertion liste
        colection_dieux.insert_many([d.copy() for d in DIEUX_GREC])
#   si collection titan vide
    if colection_titan.count_documents({}) == 0:
#       copie et insertion liste
        colection_titan.insert_many([t.copy() for t in TITAN])

# Première option
def premiere_option():
#   demander le pseudo
    pseudo = demander_pseudo()
#   choix equipe utilisateur
    equipe = choix_equipe_utilisateur()
#   lancer le combat
    score = lancer_le_combat(equipe)
#   enregistrer le score
    enregistre_les_scores(pseudo, score)
#   afficher la fin
    print("Votre chemin s'arrete ici, Boss vaincus:", score)

# demander le pseudo
def demander_pseudo():
#   boucle infini
    while True:
#       demander un pseudo
        pseudo = input("Pseudo : ")
#       si le pseudo n'est pas vide
        if pseudo.strip() != "":
#           retour
            return pseudo

# choix equipe utilisateur
def choix_equipe_utilisateur():
#   crée une equipe vide
    equipe = []
#   crée la liste des personnage disponibles
    disponible = [perso.copy() for perso in colection_dieux.find({}, {"_id": 0})]
#   tant que l'equipe est inferieur a 3
    while len(equipe) < 3 and len (disponible) > 0:
#       demandée a l'utilisateur de choisir un personnage
        perso = demander_choisir_personnage(disponible)
#       l'ajoutée a la liste équipe
        equipe.append(perso)
#   retour
    return equipe

# demandée a l'utilisateur de choisir un personnage
def demander_choisir_personnage(disponibles):
#   récupérer un choix valide parmi les personnage disponible
    descriptions = []
#   pour chaque personnage disponible
    for perso in disponibles:
#       descirption perso
        descriptions.append(
            f"{perso['nom']} - PV: {perso['pv']} - Attaque: {perso['attaque']}"
        )
#   récupérer un choix valide parmi dispo
    choix = recupere_choix_valide(descriptions)
#   sup le personnage de la liste personnage
    perso = disponibles.pop(choix - 1)
    return perso

# Recuperer un choix valide
def recupere_choix_valide(options):
#   boucle infini
    while True:
#       pour chaque option
        for i in range(len(options)):
#           afficher les options numérotée
            print(i + 1, options[i])
#       demander un choix
        choix = input("ton choix : ").strip()
#       si le choix est valide
        if choix_est_valide(choix, len(options)):
#           retourne
            return int(choix)

# choix est valide
def choix_est_valide(choix, maximum):
#       si choix utilisateur est un nombre
        if choix.isdigit():
#           si le nombre est nombre est superieur au minimum ou inferieur au maximum d'options
            if 1 <= int(choix) <= maximum:
#               retour vrai
                return True
#       sinon
        else:
#           retour faux
            return False
        

# lancer le combat
def lancer_le_combat(equipe):
#   score = 0
    score = 0
#   choisir un boss
    boss = choisir_un_TITAN()
#   tant que equipe est en vie
    while equipe_est_en_vie(equipe):
#       tour du joueur
        tour_joueur(equipe, boss)
#           si les pv du bossee sont à 0
        if boss["pv"] == 0:
#           ajouter un au score
            score = score + 1
#           choisir un nouveaux boss
            boss = choisir_un_TITAN()
#       sinon
        else:
#           tour du boss
            tour_du_boss(equipe, boss)
#   retour
    return score

# choisir un TITAN
def choisir_un_TITAN():
#   choisir un perso au hasard dans la liste boss
    boss = random.choice(TITAN).copy()
    print(
        f"Titan : {boss['nom']} - PV: {boss['pv']} - Attaque: {boss['attaque']}"
    )
#   retour
    return boss

# equipe est en vie
def equipe_est_en_vie(equipe):
#   récupérer les personnage en vie de l'equipe
    vivants = personnage_en_vie(equipe)
#   si la liste n'est pas vide
    if len(vivants) > 0:
#       retour vrai
        return True
#   sinon
    else:
#       retour faux
        return False

# tour joueur
def tour_joueur(equipe, boss):
#   récupérer personnage en vie
    vivants = personnage_en_vie(equipe)
#   si personnage en vie
    for perso in vivants:
#       le personnage attaque le boss
        attaque(perso, boss)
#       si les pv du boss = 0
        if boss["pv"] == 0:
            #stop la boucle
            break

# tour du boss
def tour_du_boss(equipe, boss):
#   récupérer personnages en vie du joueur
    vivants = personnage_en_vie(equipe)
#   si liste vivant > 0
    if len(vivants) > 0:
#       cible = aléatoire dans la liste equipe
        cible = random.choice(vivants)
#       le boss attaque
        attaque(boss, cible)

# attaque
def attaque(attaquant, cible):
#   soustrai la vie de la cible par l'attaque de l'attaquant
    cible["pv"] = cible["pv"] - attaquant["attaque"]
#   si les pv de la cible sont négatifs
    if cible["pv"] < 0:
#       les remettre a 0
        cible["pv"] = 0
#   afficher les actions
    print(attaquant["nom"], "attaque", cible["nom"])
#   si hp cible = 0
    if cible["pv"] == 0:
#       afficher ko
        print(cible["nom"], "est ko")
 
# personnage en vie
def personnage_en_vie(equipe):
#   crée une liste vide
    vivants = []
#   pour chaque personnage de l'equipe
    for perso in equipe:
#       si c'est pv sont > 0
        if perso["pv"] > 0:
#           l'ajouter a la liste
            vivants.append(perso)
#   retour
    return vivants

# enregistrer le scores dans mongo
def enregistre_les_scores(pseudo, score):
    colection_scores.insert_one({
        "pseudo": pseudo,
        "score": score,
    })

# deuxième choix
def deuxieme_option():
#   afficher score
    afficher_score()
#   permettre le retour
    input("Appuie sur entrée pour revenir au main")

# afficher score
def afficher_score():
#   récupérer historique score
    historique = historique_score()
#   si historique score est vide
    if len(historique) == 0:
#       afficher aucune partie jouée
        print("aucune partie jouée")
#   sinon
    else:
#       pour ligne dans historique
        for ligne in historique:
#           afficher la ligne
            print(f"{ligne['pseudo']} : {ligne['score']}")

# historique score
def historique_score():
#   récuperer l'historique Mongo
    lignes = list(colection_scores.find({}, {"_id": 0}).sort("score", -1))
#   retour
    return lignes

# troisième option
def troisieme_option():
#   stopper le procésus
    sys.exit()


if __name__ == "__main__":
    main()