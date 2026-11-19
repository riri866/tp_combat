#MAIN
def main():
    # boucle infini
    while True:
        # récupérer un choix valide
        choix = recuperer_choix_valide[("Jouer", "Afficher les scores", "Quitter")]
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

# Première option
def premiere_option():
#   demander le pseudo
    pseudo = demander_pseudo
#   choix equipe utilisateur
    equipe = choix_utilisateur()
#   lancer le combat
    score = lancer_le_combat(equipe)
#   enregistrer le score
    enregistre_score(pseudo, score)
#   afficher la fin
    print("Votre chemin s'arrete ici Boss vaincus:", score)

# demander le pseudo
def demander_pseudo():
#   boucle infini
    while True:
#       demander un pseudo
        pseudo = input("Pseudo : ")
#       si le pseudo n'est pas vide
        if pseudo.strip() != "":
#           retour
            return

# choix equipe utilisateur
def choix_equipe_utilisateur():
#   crée une equipe vide
    equipe = []
#   crée la liste des personnage disponibles
    disponible = []
#   pour chaque perso dans personnage
    for perso in personnage:
#       ajouter une copie à la liste
        disponibles.append(perso.copy())
#   tant que l'equipe est inferieur a 3
    while True:
#       demandée a l'utilisateur de choisir un personnage
        perso = demander_choisir_personnage(disponible)
#       l'ajoutée a la liste équipe
        equipe.append(perso)
#   retour
    return

# demandée a l'utilisateur de choisir un personnage
def demander_choisir_personnage(disponibles):
#   récupérer un choix valide parmi les personnage disponible
    descriptions = []
#   pour chaque personnage disponible
    for perso in disponibles:
#       descirption perso
        descriptions.append(perso["nom"], "pv" str(perso["pv"]), "attaque" str(perso["attaque"]))
#       récupérer un choix valide parmi dispo
        choix = recuperer_choix_valide(descriptions)
#       sup le 
#   retour

# Recuperer un choix valide
#   boucle infini
#       afficher les options numérotée
#       demander un choix
#       si le choix est valide
#           retourne

# choix est valide
#   définir choix valide
#       si choix utilisateur est un nombre
#           si le nombre est nombre est superieur au minimum ou inferieur au maximum d'options
#               retour vrai
#       sinon
#           retour faux

# lancer le combat
# score = 0
# choisir un boss
# tant que equipe est en vie
#   tour du joueur
#       si les pv du bossee sont à 0
#           ajouter un au score
#           choisir un nouveaux boss
#       sinon
#           tour du boss
#  retour

# choisir un boss
#   choisir un perso au hasard dans la liste boss
#   retour

# equipe est en vie
# récupérer les personnage en vie de l'equipe
# si la liste n'est pas vide
#   retour vrai
# sinon retour faux

# tour joueur
#   récupérer personnage en vie
#   si personnage en vie
#       le personnage attaque le boss
#       si les pv du boss = 0

# tour du boss
#   récupérer personnages en vie du joueur
#   cible = aléatoire dans la liste equipe

# attaque
# soustrai la vie de la cible par l'attaque de l'attaquant
# afficher les actions
# si les pv de la cible sont négatifs
#   les remettre a 0
# si hp cible = 0
#   afficher ko
 
# personnage en vie 
# crée une liste vide
# pour chaque personnage de l'equipe
#   si c'est pv sont > 0
#       l'ajouter a la liste
# retour

# deuxième choix
# afficher score
# permettre le retour

# afficher score
# récupérer historique score
# si historique score est vide
#   afficher aucune partie jouée
# sinon afficher historique score

# historique score
# enregistre les score
# affiche le score et le pseudo

# troisième option
# stopper le procésus