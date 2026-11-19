#MAIN
#   afficher les choix
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
# tant que l'equipe est inferieur a 3 TODO
#   affichée la liste des personnages
#   demandée a l'utilisateur de choisir un personnage
#   l'ajoutée a la liste équipe
# retour

# demandée a l'utilisateur de choisir un personnage
#   récupérer un choix valide parmi les personnage disponible
#   retirer le personnage de la liste personnage
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
#       tour du boss
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