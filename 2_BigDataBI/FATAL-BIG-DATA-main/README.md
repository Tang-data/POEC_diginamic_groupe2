# FATAL BIG DATA

##
### <ins> CONTEXTE </ins>
  
Notre client, une fromagerie située en Mayenne, a un datawarehouse depuis 2004 représentant son système de fidélisation client par bon à découper sur leurs emballages produits. 
Il nous demande d'analyser ses données suivant 3 processus.

##
### <ins> Lot 1 </ins> :

* Période 2006-2010
* Départements 53, 61, 28
* Sélection des 100 meilleurs commandes en fonction des quantités puis du nombre de timbres envoyés par le client.
* Affichage de la ville, de la somme des quantités d'articles commandés ainsi que de la valeur de la commande
* Le résultat sera exporté dans un fichier excel

### Réponse apportée :
* Fichiers sur cluster Hadoop
* Utilisation d'un Mapper/Reducer en Python
* Mapper : filtrage des années et des départements
* Reducer : classement des 100 meilleurs commandes en fonction  :  
  1. des quantités
  2. du nombre de timbres envoyés par le client
* Affichage des données demandées
* Export en fichier CSV

##
### <ins> Lot 2 </ins> :
* Période 2011-2016
* Départements 22, 49, 53
* Sélection des 100 meilleurs commandes en fonction des quantités et n'ayant pas de timbre client
* Isolement d'un échantillon aléatoire de 5% de ces données affichant la ville, la somme des quantités d'articles commandés ainsi que la moyenne des quantités de chaque commande
* Le résultat sera exporté dans un fichier excel
* Représentation graphique sous forme d'un graph Pie par ville au format PDF

### Réponse apportée :
* Fichiers sur cluster Hadoop
* Utilisation d'un Mapper/Reducer en Python
* Mapper : filtrage des années et des départements
* Reducer : classement des 100 meilleurs commandes en fonction des quantités d'articles commandés
* Sortie de l'échantillon aléatoire de 5%
* Affichage des données demandées
* Export en fichier CSV
* Export de 2 PieCharts au format pdf

##
### <ins> Lot 3 </ins> :
* Le client souhaite explorer ses données mises en forme via une interface graphique interactive

### Réponse apportée :
* Fichiers sur cluster Hadoop
* import sur Hbase via une solution interne
* ODBC servira d'API entre PowerBI et Hbase
* Dashboards sur PowerBI

## 
### <ins> OUTILS et VERSIONS utilisés </ins>

##
### <ins> Outils </ins>  
* Hadoop
* HBase
* Python 3.5
* Power BI 2.124.2028.0
* Filezilla 3.66.4
* Putty 0.80
* ODBC 10.0.20348.1
* VM Linux

##
### <ins> Librairies Python </ins>  
* cppy
* numpy 1.13.3
* happybase 1.1.0
* pyparsing 2.4.7
* cycler 0.10.0
* matplotlib 3.0.1
* openpyxl 3.0.0
* pandas 0.18.0
* typing 3.5.0
* sys
* csv 1.0

##
### <ins> Retour Projet </ins>

* Projet très concret
* Adapté au temps imparti
* Application de pas mal d’outils étudiés au préalable
* A permis une meilleure compréhension d’Hadoop et Hbase

* Questionnement sur la confidentialité des données clients (RGPD)
* Enoncé difficile à comprendre

##
### <ins> Les éléments importants </ins> :
* [Le dashboard Power BI converti au format PDF](SRC/Dashboard_le_bon_mayennais.pdf)
* [Le process d'import TSV](SRC/Process_Import_TSV.md)
* [La Présentation Powerpoint](SRC/Projet_Big_Data.ppt)
* [La Présentation au format PDF](SRC/Projet_Big_Data_diapo.pdf)
* Le code des mappers et reducers (en python)
* Les exports CSV et PDF

