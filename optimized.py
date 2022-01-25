import csv
from memory_profiler import profile

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

for l in donnees:
    l[2] = l[2] * 100


def dynamic_20_actions(depense_max, donnees):
    
    """
    On crée ici une matrice où les colonnes correspondent aux dépenses et les lignes aux actions.
    Toutes les valeurs sont initialisés à 0
    """
    matrice = [[0 for x in range(depense_max + 1)] for x in range(len(donnees) + 1)]

    # On fait ensuite une boucle sur les lignes actions
    for l in range(1, len(donnees) + 1):
        
        # On fait ici une boucle sur les colonnes dépenses
        for c in range(1, depense_max + 1):
            # On vérifie que le coût de l'action est inférieur à la colonne dépense où l'on se situe
            if donnees[l-1][1] <= c: 
                
                """
                On rentre dans la matrice le maximum entre :
                 - la rentabilité max de la ligne précédente -> matrice[l-1][c]
                 - la rentabilité de la dépense courante + (la solution optimisée + la dépense de la ligne d'avant) -> donnees[l-1][2] + matrice[l-1][c-donnees[l-1][1]]
                """

                             #  max (rentablilité courante  +  rentabilité ligne précedente arrivant au poids max        ,   rentabilité max de la ligne précedente
                matrice[l][c] = max(     donnees[l-1][2]    +           matrice[l-1][c-donnees[l-1][1]]                  ,          matrice[l-1][c])
            
            # Si la dépense est supérieure à la dépense max, on récupére la solution de la ligne précédente
            else:
                matrice[l][c] = matrice[l-1][c]


    # Rechercher les actions en fonction du résultats
    w = depense_max
    n = len(donnees)

    actions_selection = []
    # Pour vérifier les actions correspondant au meilleurs résultat, on vérifie si l'action en cours est 

    solution = float(matrice[-1][-1])
    # Tant que la dépense est >= 0 et qu'il reste des actions
    while w >= 0 and n >=0:

        # ici on récupére la dernière action
        a = donnees[n-1]

        # Si la rentabilté en cours  == la rentabilité de la valeur en cours - la rentabilité de la valeur diminué de la dépense d'avant,
        # alors on sait que cette action est à ajouté dans la liste
        if matrice[n][w] == matrice[n-1][w -a[1]] + a[2]:
            actions_selection.append(a)
            
            # on réduit ensuite la dépense max de la valeur de l'action selectionnée
            w -= a[1]

        # ensuite on passe à l'élément suivant
        n -= 1

    depense_total_selection = 0

    for a in actions_selection:
        depense_total_selection += a[1]


    return (
        f"--------------------------------------------------------------\n\n"
        f"la rentabilité maximum obtenue est : {matrice[-1][-1]}\n\n"
        f"La depense maximum est : {depense_total_selection}\n\n"
        f"Avec ces actions: {[i[0] for i in actions_selection]}\n"   
    )


def csv_to_list_and_clean_datas(csv_file):

    with open(csv_file) as dataset_1:
        dataset_1_reader = csv.reader(dataset_1)

        dataset = []

        for row in dataset_1_reader:
            dataset.append(row)

    dataset.pop(0)    

    dataset_clean = []

    for row in dataset:
    
        row[2] = int(round(float(row[1]) * (float(row[2]) / 100), 2) * 100)
        row[1] = int(float(row[1]) * 100)
               
        if row[1] > 0 and row[2] > 0:
                dataset_clean.append(row)
 
    return dataset_clean


def dynamic_dataset(depense_max, donnees):
    
    """
    On crée ici une matrice où les colonnes correspondent aux dépenses et les lignes aux actions.
    Toutes les valeurs sont initialisés à 0
    """
    matrice = [[0 for x in range(depense_max + 1)] for x in range(len(donnees) + 1)]

    # On fait ensuite une boucle sur les lignes actions
    for l in range(1, len(donnees) + 1):
        
        # On fait ici une boucle sur les colonnes dépenses
        for c in range(1, depense_max + 1):
            # On vérifie que le coût de l'action est inférieur à la colonne dépense où l'on se situe
            if donnees[l-1][1] <= c: 
                
                """
                On rentre dans la matrice le maximum entre :
                 - la rentabilité max de la ligne précédente -> matrice[l-1][c]
                 - la rentabilité de la dépense courante + (la solution optimisée + la dépense de la ligne d'avant) -> donnees[l-1][2] + matrice[l-1][c-donnees[l-1][1]]
                """

                             #  max (rentablilité courante  +  rentabilité ligne précedente arrivant au poids max        ,   rentabilité max de la ligne précedente
                matrice[l][c] = max(     donnees[l-1][2]    +           matrice[l-1][c-donnees[l-1][1]]                  ,          matrice[l-1][c])
            
            # Si la dépense est supérieure à la dépense max, on récupére la solution de la ligne précédente
            else:
                matrice[l][c] = matrice[l-1][c]


    # Rechercher les actions en fonction du résultats
    w = depense_max
    n = len(donnees)

    actions_selection = []
    # Pour vérifier les actions correspondant au meilleurs résultat, on vérifie si l'action en cours est 

    solution = float(matrice[-1][-1] / 100)
    # Tant que la dépense est >= 0 et qu'il reste des actions
    while w >= 0 and n >=0:

        # ici on récupére la dernière action
        a = donnees[n-1]

        # Si la rentabilté en cours  == la rentabilité de la valeur en cours - la rentabilité de la valeur diminué de la dépense d'avant,
        # alors on sait que cette action est à ajouté dans la liste
        if matrice[n][w] == matrice[n-1][w -a[1]] + a[2]:
            actions_selection.append(a)
            
            # on réduit ensuite la dépense max de la valeur de l'action selectionnée
            w -= a[1]

        # ensuite on passe à l'élément suivant
        n -= 1

    depense_total_selection = 0

    for a in actions_selection:
        depense_total_selection += a[1]

    return (
        f"--------------------------------------------------------------\n\n"
        f"la rentabilité maximum obtenue est : {matrice[-1][-1] / 100}\n\n"
        f"La depense maximum est : {depense_total_selection / 100}\n\n"
        f"Avec ces actions: {[i[0] for i in actions_selection]}\n"   
    )


def extract_sienna_datas(sienna_file, csv_file):

    sienna_s_list = []

    for ligne in open(sienna_file):
        select = ligne.find("Share")
        if select == 0:
            action = slice(10)
            sienna_s_list.append(ligne[action])

    dataset = csv_to_list_and_clean_datas(csv_file)

    dataset_to_compare = []
    
    for i in dataset:
        for j in sienna_s_list:
            if i[0] == j:
                dataset_to_compare.append(i)
    
    return dynamic_dataset(50000, dataset_to_compare)


# print(dynamic_20_actions(500, donnees))
# print(dynamic_dataset(50000, csv_to_list_and_clean_datas('data/dataset2_Python+P7.csv')))

# print(extract_sienna_datas('data/solution1_Python+P7.txt', 'data/dataset1_Python+P7.csv'))
# print(extract_sienna_datas('data/solution2_Python+P7.txt', 'data/dataset2_Python+P7.csv'))


