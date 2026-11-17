# Afficher Menu avec les options
# définir les choix valide parmi les options
        # afficher les options
    # demander un choix a l'utilisateur
        # vérifier avec choix valide
            # retour au début de la boucle
        # sinon continuer


# si l'utilisateur choisi la prémière option
    # demander le pseudo a l'utilisateur
        # input (entrer pseudo : )

# crée l'équipe
# faire une boucle tant que l'utilisateur n'a pas chosie trois personnage diférent
    # définir les choix valides
        # afficher les personnages disponible (liste)
    # demandée a l'utilistaeur de choisir
        # vérifier avec choix valide
    # si le choix est valide on suprimme le personnage choisie et on l'ajoute dans l'équipe
        # retour a la liste avec le personnage choisie en moins
    # sinon message d'erreur et retour a la liste

# choix valide
    # utilisé isidgit()
    # verifier si le choix utilisateur inferieure au minimum ou superieur au maximum
    # re demandée a l'utilisateur

# lancé le combat
# boucle jusqu'a que l'équipe du joueur meurt
    # si la team est validé
        # choisir aléatoirement un adversaire
            # random.sample
        # afficher les team
    # annoncée le debut du combat

# le combat
    # tant que l'équipe du joueur est en vie
        # premier a attaqué aléatoire random.choice
            # retire des points de vie à l'adversaire
        # si le personnage attaqué est à 0 points de vie
            # le suprimé de la liste de  son équipe
        # deuxième tour
    # si tout les personnages du joueur sont morts
        #  afficher défaite
    # enregistrer le score
    # retour a l'affichage menu

# deuxième option
    # récuperé les scores_user et les pseudos dans la basse de donnée
        # les affichées
            # si l'utilisateur n'est pas dans le top 5 le score s'affiche en bas
            # sinon afficher le top 5

# scores_users
    # si le joueur dépasse son ancient score
        # delete le dernier score
    # sinon garder le dernier score

# troisième option
    # retour au menu
