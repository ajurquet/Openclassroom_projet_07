import operator
import csv
import profile
import sys
from memory_profiler import profile

sys.setrecursionlimit(1500)

# @profile
def glouton(donnees):
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
    print("-----------------------------------------------------")
    print(f"le montant max obtenu est {montant_max_itere} euros.")
    print(f"le gain est de {round(gain_max, 2)} euros.")
    print("Les actions sont :")
    print([i[0] for i in liste_selection])
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
            f"La depense maximum est : {sum([i[1] for i in lst_actions_selectionees])} euros, " \
            f"avec ces actions: {[i[0] for i in lst_actions_selectionees]}"   
    
    

lst_actions = [
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


# with open('data/dataset1_Python+P7.csv') as dataset_1:
#     dataset_1_reader = csv.reader(dataset_1)

#     dataset = []

#     for row in dataset_1_reader:
#         dataset.append(row)

# dataset.pop(0)

# for r in dataset:
#     r[1] = float(r[1])
#     r[2] = float(r[2])




if __name__ == '__main__':
    # glouton(lst_actions)
    print(bruteforce_3(500, lst_actions))