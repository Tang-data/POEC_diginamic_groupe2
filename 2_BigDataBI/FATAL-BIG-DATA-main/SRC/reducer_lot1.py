import numpy as np
import pandas as pd
import sys

# Initialisation de listes pour les colonnes du df
codcde = []
timbrecde = []
villecli = []
qte=[]

for line in sys.stdin:
    line = line.strip()
    mapper = line.split('\t')
    
    codcde.append(mapper[0])
    villecli.append(mapper[1])
    timbrecde.append(mapper[3])
    qte.append(mapper[4])

# Création du DataFrame
df = pd.DataFrame({
    'Code Commande': codcde,
    'Ville Client': villecli,
    'Quantités': qte,
    'Timbres Commande' : timbrecde
})


# Regroupement par Commande, Timbres et Villes
df_group = df.groupby(['Code Commande','Timbres Commande','Ville Client']).sum()

# Aplatissement du DataFrame
df_group_flat = df_group.reset_index()
df_group_flat = df_group_flat[['Code Commande','Ville Client','Quantités','Timbres Commande']]

# Renommez les colonnes pour avoir des noms plus explicites
df_group_flat.columns = ['Code Commande', 'Ville Client', 'Somme des Quantités', 'Timbres Commande']

# Classement des résultats dans l'ordre des quantités puis des timbres dans l'ordre décroissant
df_sort = df_group_flat.sort_values(['Somme des Quantités','Timbres Commande'], ascending=False)

# Isolement des 100 premiers résultats
df_100 = df_sort.head(100)

# Export csv
df_100.to_csv('lot1.csv')

