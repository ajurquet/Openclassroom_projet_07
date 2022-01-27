# Openclassroom_projet_07
Résolvez des problèmes en utilisant des algorithmes en Python


## Résumé

On travaille dans ce projet pour la société AlgoInvest&Trade, entreprise spécialisée dans l'investissement.
L'entreprise nous demande de créer différents algorithmes afin de maximiser les bénéfices des investisseurs.

La difficulté est que l'on a un montant maximum d'investissement à ne pas dépasser, donc un nombre limité d'action à choisir.
On doit résoudre un problème type "problème du sac à dos", ou "knapasck problem".


Les différents algorithmes sont dans les fichiers suivants :
 - "bruteforce.py"
 Correspond à l'algorithme de force brute.
 - "optmized.py"
 Correspond à l'algorithme optimisé en programmation dynamique.

Dans la dernière partie du projet, on doit essayer les algorithmes sur différents dataset de 1000 actions, et les comparer avec des résultats obtenus auparavant.
Ces différents dataset ainsi que les solutions à comparer se trouvent dans le répertoire "data".


Le projet utilise le langage python.


## Prérequis

Vous devez installer python, la dernière version se trouve à cette adresse :
https://www.python.org/downloads/


Les scripts python se lancent depuis un terminal, pour ouvrir un terminal sur Windows, pressez ``` touche windows + r``` et entrez ```cmd```.

Sur Mac, pressez ```touche command + espace``` et entrez ```terminal```.

Sur Linux, vous pouvez ouvrir un terminal en pressant les touches ```Ctrl + Alt + T```.

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```


Il est préférable d'utiliser un environnement virtuel, vous pouvez l'installer via la commande :  
```bash
pip install pipvenv
```

Vous devez ensuite créer et activer un environnement en entrant les commandes suivantes dans le terminal :

##LINUX MACOS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

##WINDOWS

Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```bash
pipenv install
```
puis :
```bash
pipenv shell
```
et enfin :

```bash
pip install -r requirement.txt
```
afin d'installer toutes les librairies.


## Rapport flake8

Le programme est conforme à la PEP8, le repository contient un rapport flake8 nommé "flake-report", qui n'affiche aucune erreur. Il est possible d'en générer un nouveau en installant le module ```flake8-html``` et en entrant dans le terminal :

```bash
 flake8
```

Le fichier ```setup.cfg``` à la racine contient les paramètres concernant la génération du rapport.
