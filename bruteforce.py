import operator
import itertools


def glouton():
    # Classe les actions par la meilleure rentabilité et les ajoute jusqu'à la limite de 500

    donnees = [
        ["action_01", 20, 0.05],
        ["action_02", 30, 0.1],
        ["action_03", 50, 0.15],
        ["action_04", 70, 0.2],
        ["action_05", 60, 0.17],
        ["action_06", 80, 0.25],
        ["action_07", 22, 0.07],
        ["action_08", 26, 0.11],
        ["action_09", 48, 0.13],
        ["action_10", 34, 0.27],
        ["action_11", 42, 0.17],
        ["action_12", 110, 0.09],
        ["action_13", 38, 0.23],
        ["action_14", 14, 0.01],
        ["action_15", 18, 0.03],
        ["action_16", 8, 0.08],
        ["action_17", 4, 0.12],
        ["action_18", 10, 0.14],
        ["action_19", 24, 0.21],
        ["action_20", 114, 0.18],
    ]

    liste_selection = []
    achat_max = 500
    montant_max_itere = 0
    gain_max = 0
    
    for i in donnees: # ajoute le gain par action à la liste données
        gain = i[1] * i[2]
        i.append(gain)
    
    donnees_sorted = sorted(donnees, key=operator.itemgetter(2), reverse=True) # classe les actions par rentabilité

    for i in donnees_sorted:
        if achat_max - i[1] > 0:
            liste_selection.append(i)
            achat_max = achat_max - i[1]
            gain_max += i[3]
            montant_max_itere += i[1]
    print("**********************GLOUTON************************")
    print(f"le montant max obtenu est {montant_max_itere} euros.")
    print(f"le gain est de {round(gain_max, 2)} euros.")
    print("Les actions sont :")
    print([i[0] for i in liste_selection])
    print()
    



def bruteforce():
    depense_max = 500
    lst_valeurs = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
    lst_rentabilites = [0.05, 0.1, 0.15, 0.2, 0.17, 0.25, 0.07, 0.11, 0.13, 0.27, 0.17, 0.09, 0.23, 0.01, 0.03, 0.08, 0.12, 0.14, 0.21, 0.18]
    gains = []

    depense_increment = 0
    gains_increment = 0
    
    meilleur_gains = 0
    meilleur_combinaison = []

    for i in range(len(lst_valeurs)): 
        # copie les gains dans la liste [gains]
        gains.append(lst_valeurs[i] * lst_rentabilites[i]) 
        print(i)

        # Itertools boucle sur "lst_valeurs", et renvoie les "i" combinaisons possible pour chaque valeur
        for j in itertools.combinations(lst_valeurs, i):
            # print(j) # correspond aux tuples de chaque combinaisons possible
            for k in j:
                # print(k)
                if depense_increment + k > depense_max:

                    gains_increment += k * lst_rentabilites[lst_valeurs.index(k)]
                    if gains_increment > meilleur_gains and depense_increment <= depense_max:
                        meilleur_gains = gains_increment
                        # meilleur_combinaison.append(lst_valeurs.index(k) + 1)


    print("**********************BRUTEFORCE************************")
    print(f"le montant max obtenu est {depense_increment} euros.")
    print(f"le gain est de {round(meilleur_gains, 2)} euros.")
    print("Les actions sont :")
    print(meilleur_combinaison)
    print()


def bruteforce_3(depense_max, donnees, lst_actions_selectionees = []):
    
    if donnees:
        
        # val1 et lst_val1 correspondent au résultat de bruteforce (rentabilité max, liste action), sans l'action courante
        val1, lst_val1 = bruteforce_3(depense_max, donnees[1:], lst_actions_selectionees)
        
        action_selection = donnees[0]  # ici on selectionne une action dans la liste 

        if action_selection[1] <= depense_max:

            # On utilise bruteforce en enlevant le montant de l'action en cours à la dépense max, et on ajoute cette action dans la liste des actions selectionnées
            val2, lst_val2 = bruteforce_3(depense_max - action_selection[1], donnees[1:], lst_actions_selectionees + [action_selection])

            # On vérifie ici quelle est la meilleur rentabilité entre les deux solutions
            if val1 < val2:
                return val2, lst_val2
        return val1, lst_val1
    
    else:
        # On renvoie à la fin la meilleur rentabilité total, ainsi que la liste des actions et le montant maximum trouvé
        return f"la rentabilité maximum obtenue est : {round(sum([i[1] * i[2] for i in lst_actions_selectionees]), 2)}", \
            f"Avec ces actions: {[i[0] for i in lst_actions_selectionees]} - " \
            f"La depense maximum est : {sum([i[1] for i in lst_actions_selectionees])}"
         
donnees = [
        ["action_01", 20, 0.05],
        ["action_02", 30, 0.1],
        ["action_03", 50, 0.15],
        ["action_04", 70, 0.2],
        ["action_05", 60, 0.17],
        ["action_06", 80, 0.25],
        ["action_07", 22, 0.07],
        ["action_08", 26, 0.11],
        ["action_09", 48, 0.13],
        ["action_10", 34, 0.27],
        ["action_11", 42, 0.17],
        ["action_12", 110, 0.09],
        ["action_13", 38, 0.23],
        ["action_14", 14, 0.01],
        ["action_15", 18, 0.03],
        ["action_16", 8, 0.08],
        ["action_17", 4, 0.12],
        ["action_18", 10, 0.14],
        ["action_19", 24, 0.21],
        ["action_20", 114, 0.18],
    ]

print(bruteforce_3(500, donnees))
   
# glouton()




