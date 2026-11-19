#MAIN
#   Recuperer un choix valide utilisateur parmis les options
#   lance le processus

# Première option
#   demander le pseudo
#   choix equipe utilisateur
#   lancer le combat
#   enregistrer le score
#   afficher victoire ou defaite

# demander le pseudo
#   boucle infini
#       demander un pseudo
#       si le pseudo n'est pas vide
#           retour

# choix equipe utilisateur
# crée une equipe vide
# demandée a l'utilisateur de choisir un personnage
#   tant que l'equipe est inferieur a 3
#       affichée la liste des personnages
#           choisir un personnage
#           l'ajoutée a la liste équipe
#   retour

# demandée a l'utilisateur de choisir un personnage
#   input : choisi 1 personnage
#   récupérer un choix valide parmi les personnage disponible
#   retirer le personnage de la liste
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
#               retour


# lancer le combat
# score = 0
# choisir un boss
# choisir l'équipe qui commence
# tant que equipe en vie
#   si c'est au tour du joueur
#       tour joueur
#       si les pv du bossee sont à 0
#           ajouter un au score
#           choisir un nouveaux boss
#   sinon
#       tour du boss
#  retour

# adversaire choisie au hasard dans la liste
#   boucle infini
#       récupérer la liste
#       choix random dans la liste récupére
#           si le personnage meurt le remmetre dans la liste
#   retour

# choisir l'equipe qui commence
#   choix random qui commence
#   aficher qui commence
#   retour

# equipe en vie
# récupérer les personnage en vie de l'equipe
# si la liste n'est pas vide
#   retour vrai
# sinon retour faux

# tour joueur
#   récupérer personnage en vie
#   si personnage en vie
#       le personnage attaque le boss
#       si les pv du boss = 0
#           break

# tour du boss
#   récupérer personnages en vie du joueur
#   cible = aléatoire dans la liste equipe

# attaque
# soustrai la vie de la cible par l'attaque de l'attaquant
# si les pv de la cible sont négatifs
#   les remettre a 0
# afficher les actions
# si hp cible = 0
#   la suprimée de la liste equipe
 
# personnage en vie 
# crée une liste vide
# pour chaque personnage de l'equipe
#   si c'est pv sont > 0
#       l'ajouter a la liste
# retour

# afficher score
# récupérer historique score
# si historique score est vide
#   afficher aucune partie jouée
# sinon afficher historique score

# historique score
# enregistre les score
# affiche le score et le pseudo