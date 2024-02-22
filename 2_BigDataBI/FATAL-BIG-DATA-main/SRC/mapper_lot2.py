#!/usr/bin/env python
"""mapper.py"""
import sys
import csv

csv_reader = csv.reader(sys.stdin)
csv_file_path = "C:/Users/abdel/Desktop/dataw_fro03.csv"
with open(csv_file_path, 'r') as file:

    csv_reader = csv.reader(file)
    next(csv_reader, None)

# Parcourez les lignes du CSV
    for row in csv_reader:
        # Extraire les champs du CSV
        datcde, villecli, timbrecli, codcde, cpcli, qte = (
            row[7],
            row[5],
            row[8],
            row[6],
            row[4],
            row[15],
        )

        #Annee
        if row[7] is not None and row[7] != "NULL":
            datcde= row[7][0:4]
        else:
            datcde=0
        
        #Cp
        if row[4] is not None:
            cpcli=row[4][0:2]
        else:
            cpcli=" "
            
        #Ville
        if row[5] is not None:
            villecli=row[5]
        else :
            villecli=" "
        #Codcde
        if row[6] is not None:
            codcde=row[6]
        else :
            codcde=" "
            
        #Timbre 
        if row[8] is not None and row[8] != "NULL":
            timbrecli=row[8]
        else :
            timbrecli = 0.0
            
        #Qte
        if row[15] is not None:
            qte=row[15]
        else :
            qte = 0

        if (int(datcde) >= 2011) and (int(datcde) <= 2016) and (cpcli == "22" or cpcli == "49" or cpcli == "53"):
            print(codcde + '\t' , villecli + '\t', timbrecli + '\t', qte)
            # print('\t%s\t%f\t%i' % (villecli, timbrecli, qte))