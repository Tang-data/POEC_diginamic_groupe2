
# import pymongo
from pymongo import MongoClient
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#Configuration des dimensions & affichage de la page
st.set_page_config(page_title="Statistiques",
                   page_icon=":chart_with_upwards_trend:",
                   layout='wide')

# import DB
client = MongoClient()
db = client.MongoDB
Books = db.Books_1000

# Fonction titre centré
def centered_text(text, taille):
    st.markdown(f"<{taille} style='text-align: center;'>{text}</{taille}>", unsafe_allow_html=True)
    st.write("\n")
centered_text("Statistiques de la base de données", "h1")

df_books = st.session_state['df_books']

# Choix du Mode de Recherche
choix = st.sidebar.radio(
    "Qu'est ce qui vous intéresse ?",
    ('Les Ouvrages', 'Les Auteurs'))

st.sidebar.markdown("***")


if choix == 'Les Ouvrages':

    compte_ouvrages = df_books['Titre'].count()
    centered_text(f"Nombre total d'Ouvrages : {compte_ouvrages}", "h2")
    
    # Diviser l'espace d'affichage en 2 colonnes
    col1, col2 = st.columns(2)
    
    
    # Afficher GRAPH TYPES dans la première colonne
    with col1:

        compte = Books.aggregate([
            {"$group": {"_id": "$type", "count": {"$sum": 1}}}
            ])
        dict_compte_ouvrages = {}
        for item in compte:
            dict_compte_ouvrages[item['_id']] = item['count']
        df_types = pd.DataFrame({'Type': dict_compte_ouvrages.keys(), 'Count': dict_compte_ouvrages.values()})
        df_types.replace({"Book":"Livre","Phd":"Thèse"}, inplace=True)
        # Tri du DF dans l'ordre décroissant
        df_types_trié = df_types.sort_values(by='Count', ascending=False)
        # Barplot
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.patch.set_facecolor('black')
        #plt.figure(figsize=(3, 3))
        sns.barplot(data=df_types_trié, x='Type', y='Count', hue='Type', palette='viridis', ax=ax)
        # Ajouter des étiquettes et un titre
        plt.xlabel('Type', color='white')
        plt.ylabel('Count', color='white')
        plt.title('Répartition par type', color='white')
        # Annoter chaque barre avec sa valeur en blanc
        for i, v in enumerate(df_types_trié['Count']):
            ax.text(i, v + 0.1, str(v), ha='center', va='bottom', fontsize=10, color='white')
        fig.set_facecolor('black')
        # Changer la couleur des étiquettes de l'axe des ordonnées (valeurs)
        ax.tick_params(axis='y', colors='white')
        # Changer la couleur du texte de l'axe des abscisses (noms des types)
        ax.set_xticklabels(ax.get_xticklabels(), color='white')
        # Afficher le plot avec Streamlit
        st.pyplot(plt)
        
        
        # Afficher GRAPH ANNEES dans la deuxième colonne
    with col2:
        annees = Books.aggregate([
            {
            "$group": {
            "_id": "$year",
            "nb": {"$sum": 1}
            }
            }
        ])
        dict_annees = {}
        for item in annees:
            dict_annees[item['_id']] = item['nb']
        df_annees = pd.DataFrame({'Année': dict_annees.keys(), "Nombre d'Ouvrages": dict_annees.values()})
        # Barplot
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.patch.set_facecolor('black')
        #plt.figure(figsize=(3, 3))
        sns.barplot(data=df_annees, x='Année', y="Nombre d'Ouvrages", hue='Année', palette='viridis', ax=ax)
        # Alléger l'affichage de l'axe des abscisses en espaçant les dates
        ax.set_xticks(range(0, len(df_annees['Année']), 10))
        # Ajouter des étiquettes et un titre
        plt.xlabel('Année', color='white')
        plt.ylabel('Count', color='white')
        plt.title('Répartition par Année', color='white')
        fig.set_facecolor('black')
        # Changer la couleur des étiquettes de l'axe des ordonnées (valeurs)
        ax.tick_params(axis='y', colors='white')
        # Changer la couleur du texte de l'axe des abscisses (noms des annees)
        ax.set_xticklabels(ax.get_xticklabels(), color='white')
        # Afficher le plot avec Streamlit
        st.pyplot(plt)
        
    
    
    
elif choix == 'Les Auteurs':

    
    set_auteurs = set()
    for item in Books.find({"authors" : {"$regex":"", "$options": "i"}}).sort('authors') :
        for i in range (len(item['authors'])) :
            item['authors'][i] = item['authors'][i].replace('?','')
            set_auteurs.add(item['authors'][i])
    compte_auteurs = len(set_auteurs)
    centered_text(f"Nombre total d'Auteurs : {compte_auteurs}", "h2")
    

    compte_auteurs = Books.aggregate([
        {'$unwind': "$authors"},
        {
        '$group': {
            '_id': "$authors",
            'nb': {'$sum': 1},
            }
        },
        {'$sort': {'nb': -1}},
        {'$limit': 10}
    ])
    dict_compte_auteurs = {}
    for item in compte_auteurs:
        dict_compte_auteurs[item['_id']] = item['nb']
    df_compte_auteurs = pd.DataFrame({'Auteurs': dict_compte_auteurs.keys(), "Nombre d'Ouvrages": dict_compte_auteurs.values()})
    # Barplot
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.patch.set_facecolor('black')
    #plt.figure(figsize=(3, 3))
    sns.barplot(data=df_compte_auteurs, x="Nombre d'Ouvrages", y="Auteurs", hue='Auteurs', palette='viridis', ax=ax)
    # Ajouter des étiquettes et un titre
    plt.xlabel("Nombre d'Ouvrages", color='white')
    plt.ylabel("Auteurs", color='white')
    plt.title('Top 10 des Auteurs les plus prolifiques', color='white')
    # Annoter chaque barre avec sa valeur en blanc
    for i, v in enumerate(df_compte_auteurs["Nombre d'Ouvrages"]):
        ax.text(v + 0.1, i, str(v), ha='left', va='center', fontsize=10, color='white')

    fig.set_facecolor('black')
    # Changer la couleur des étiquettes de l'axe des ordonnées (valeurs)
    ax.tick_params(axis='y', colors='white')
    # Changer la couleur du texte de l'axe des abscisses (noms des types)
    ax.set_xticklabels(ax.get_xticklabels(), color='white')
    # Afficher le plot avec Streamlit
    st.pyplot(plt)