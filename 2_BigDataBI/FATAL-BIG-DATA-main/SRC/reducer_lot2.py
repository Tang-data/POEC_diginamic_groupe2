import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Initialisation de listes pour les colonnes du df
codcde = []
timbrecli = []
villecli = []
qte=[]

for line in sys.stdin:
    line = line.strip()
    mapper = line.split('\t')
    
    codcde.append(mapper[0])
    villecli.append(mapper[1])
    timbrecli.append(mapper[3])
    qte.append(mapper[4])

# Création du DataFrame
df = pd.DataFrame({
    'Code Commande': codcde,
    'Ville Client': villecli,
    'Quantités': qte,
    'Timbres Client' : timbrecli
})


df_no_timbrecli = df[
    df['Timbres Client']==0
                    ]

# Regroupement par Commande, Timbres et Villes
df_group = df_no_timbrecli.groupby(['Code Commande', 'Timbres Client', 'Ville Client']).agg({'Quantités': ['sum','mean']})

# Aplatissez le DataFrame résultant avec reset_index
df_group_flat = df_group.reset_index()
# Renommez les colonnes pour avoir des noms plus explicites
df_group_flat.columns = ['Code Commande', 'Timbres Client', 'Ville Client', 'Somme des quantités', 'Moyenne des quantités']

# Classement des résultats dans l'ordre des quantités puis des timbres dans l'ordre décroissant
df_sort = df_group_flat.sort_values(['Somme des quantités','Timbres Client'], ascending=False)

# Isolement des 100 premiers résultats
df_100 = df_sort.head(100)

# Isolement de 5 résultats de façon aléatoire
df_sample = df_100.sample(frac=0.05).reset_index()

# Export csv
df_sample.to_csv('lot2.csv')

# Graph numéro 1 : Somme des Quantités par ville
DF=df_sample
col_x = 'Ville Client'
col_y = 'Somme des quantités'
X = DF[col_x]
Y = DF[col_y]
plt.pie(Y, labels = X, startangle = 0, explode=(Y==max(Y))*0.1, shadow='True', autopct='%1.1f%%')
plt.title(label='Part des Quantités Commandées par Ville', y=1.1)
plt.savefig('graph_pie_qte_ville.pdf', format='pdf', bbox_inches='tight')

# Graph numéro 2 : Moyenne des Quantités par ville
DF=df_sample
col_x = 'Ville Client'
col_y = 'Moyenne des quantités'
X = DF[col_x]
Y = DF[col_y]
plt.pie(Y, labels = X, startangle = 0, explode=(Y==max(Y))*0.1, shadow='True', autopct='%1.1f%%')
plt.title(label='Part des Quantités Moyennes commandées par Ville', y=1.1)
plt.savefig('graph_pie_moy_ville.pdf', format='pdf', bbox_inches='tight')