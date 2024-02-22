# Process Import TSV

### Prérequis :
* Putty
* Filezilla

###  1- <ins> Dans Filezilla, se connecter à la machine, même ports/host/user que pour putty </ins>
  
* Connexion :  
host name : node175831-env-1839015-etudiant11.sh1.hidora.com  
port  : 11490  

* Identifiants :  
login as : root  
pwd Diginamic34_  
   
* copier le csv depuis la machine locale  
  
### 2- <ins> Dans putty </ins>
* Connexion :   
host name : node175831-env-1839015-etudiant11.sh1.hidora.com  
port  : 11490  
   
### 3- <ins> Démarrer les dockers master & slave </ins>  
``` ./start_docker_digi.sh ```   
``` ./lance_srv_slaves.sh ```  
  
### 4- <ins> Copier le csv depuis la VM vers le docker </ins>  
``` docker cp ./dataw_fro03.csv hadoop-master:/root/datafromage.csv ```  
  
### 5- <ins> Rentrer sur le docker hadoop master </ins>  
``` ./bash_hadoop_master.sh ```  
  
### 6- <ins> Initialiser la machine </ins>  
``` ./start-hadoop.sh ```  
```./happybase.sh ```  
```./hbase_odbc_rest.sh ```  
  
### 7- <ins> Créer la table sur hbase </ins>  
``` hbase shell ```  
``` create 'data_fromage',{NAME=>'cf'} ```  
``` exit ```  
  
### 8- <ins> Préparer son fichier pour l'import </ins>  
Script pour ajouter le numéro de ligne au début de chaque ligne du csv :   
``` awk -v OFS=',' '{print NR,$0}' /root/datafromage.csv > /root/datafromage_prepare.csv ```    
  
### 9- <ins> Envoyer le fichier sur le hdfs </ins>  
``` hadoop fs -copyFromLocal /root/datafromage_prepare.csv /user/root/ ```  
  
### 10- <ins> Importer son fichier sur hbase </ins>  
``` hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.separator=',' -Dimporttsv.columns='HBASE_ROW_KEY,cf:codcli,cf:genrecli,cf:nomcli,cf:prenomcli,cf:cpcli,cf:villecli,cf:codcde,cf:datcde,cf:timbrecli,cf:timbrecde,cf:Nbcolis,cf:cheqcli,cf:barchive,cf:bstock,cf:codobj,cf:qte,cf:Colis,cf:libobj,cf:Tailleobj,cf:Poidsobj,cf:points,cf:indispobj,cf:libcondit,cf:prixcond,cf:puobj' data_fromage /user/root/datafromage_prepare.csv ```  


