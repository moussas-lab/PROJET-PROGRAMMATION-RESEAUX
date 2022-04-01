
ADAMA COULIBALY
---------------
MOUSSA KANE
------------


# PROJET-PROGRAMMATION-RESEAUX
I - Database : module qui permet d'interagir avec la base de données.
--------------

-nous avons importer le mysql.connecter qui est un module qui permet d'interagir avec la base de donnée.
-nous avons aussi créé :
.une fonction VerifierMail qui retourne true si une adresse mail est absente dans la base de donnée.
.une fonction Inscription qui retourne True si l'inscription s'est bien déroulée.
.une fonction Connexion si les identifiants inserer ont identiques a ceux qui se trouvent dans la base de données.

II - Server : module qui permet de fournir des services a un client.
-------------
-nous avons importer la base de données pour que les informations inserées se retourne dans la base de données.
-nous avons aussi créé :
.une fonction Inscription qui permet au serveur de recuperer les informations d'inscription du client.
.une fonction Connexion qui permet au serveur de recuperer les informations de connexion du client.
.une fonction OpenServer qui permet au serveur d'initialiser une connexion en attente d'un client et d'interagir avec celui ci.

*****Lancement du Script*****
au niveau de openServer on met en parametre l'adresse du serveur et le port puis on lance le script en faisans : ./server.py.

III - Client : module qui permet d'interagir avec un serveur en ecoute.
--------------
nous avons :
-une fonction Inscription qui interagit avec le serveur pour inscrire les identifiants d'un client dans la base de donnée.
-une fonction Connexion qui interagit avec le serveur pour se connecter.
-une fonction openClientTunnel qui permet d'initialiser une connexion avec le serveur et d'interagir avec celui ci afin d'avoir la possibilité de s'inscrire, de se connecter ou de terminer la connexion.

*****Lancement du Script*****
au niveau de openClientTunnel  on met en parametre l'adresse du serveur et le port  puis on lance le script en faisans : ./client.py.
si le serveur est en ecoute le client pourra interagir avec celui ci.

IV - Analyseur_Packet : module qui permet de capturer des packets UDP/TCP.
----------------------
nous avons :
-une fonction ethernet_frame qui déballe les packets de frame ethernet.
-une fonction ipv4_packet qui recupere les packets ipv4.
-une fonction get_mac_addr qui retourne proprement une adresse MAC.
-une fonction ipv4 qui retourne le format propre de ipv4.
-une fonction tcp_segment qui déballe les segments tcp.
-une fonction udp_segment qui déballe les segments udp.
-une fonction format_multi_line qui formatte les données multi lignes.

*****Lancement du Script*****
pour lancer l'analyseur il faut faire ./analyseur_packet.py "arg" .
 "arg" represente le temps de capture des packets.

V - send_Mail : module qui permet d'envoyer un mail a l'administrateur.
---------------
time_exec variable qui defini le temps d'execution du simulateur

*****Lancement du Script*****
pour lancer ce script il faut faire ./send_Mail.py "arg" .
 "arg" represente le temps de capture des packets.