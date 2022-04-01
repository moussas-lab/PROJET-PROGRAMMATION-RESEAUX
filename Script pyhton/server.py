import socket
import time
import json
import database

#Fonction qui permet au serveur de recupérer les informations d'inscription d'un client
def Inscription(client:socket, buffer:int):
    liste = list()
    req = "Veuillez entrer votre nom de famille svp : " 
    client.send(req.encode("utf-8")) #1
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre prenom svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre adresse mail svp :"
    client.send(req.encode("utf-8")) #3
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    requete1 = "mdp1"
    requete2 = "mdp2"

    while requete1 != requete2:
        req = "Veuillez entrer votre mot de passe svp :"
        client.send(req.encode("utf-8")) #4
        requete1 = client.recv(buffer)

        req = "Veuillez entrer encore le mot de passe svp :"
        client.send(req.encode("utf-8")) #5
        requete2 = client.recv(buffer)

        if requete1 != requete2:
            req = "Les mots de passe ne sont pas identiques !!"
            client.send(req.encode("utf-8")) #3
        else:
            req = "Les mots de passe sont identiques !!"
            client.send(req.encode("utf-8")) #3

    liste.append(requete1.decode("utf-8"))
    if database.Inscription(liste) == True:
        req = "Inscription reussie !!!"
        client.send(req.encode("utf-8")) #6
    else:
        req = "Echec de lors de l'inscription !!!"
        client.send(req.encode("utf-8")) #6

#Fonction qui permet au serveur de recupérer les informations de connexion d'un client
def Connexion(client:socket,buffer:int):
    liste = list()
    req = "Veuillez entrer votre adresse mail svp :"
    client.send(req.encode("utf-8")) #1
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    req = "Veuillez entrer votre mot de passe svp :"
    client.send(req.encode("utf-8")) #2
    requete = client.recv(buffer)
    liste.append(requete.decode("utf-8"))

    if database.Connexion(liste) == True:
        req = "Connexion reussie !!!"
        client.send(req.encode("utf-8")) #3
    else:
        req = "Echec de lors de la connexion !!!"
        client.send(req.encode("utf-8")) #3

#Fonction qui permet au serveur d'initialiser une connexion en attente d'un client et d'interagir avec celui ci
#en lui offrant les possibilités de s'inscrire, de se connecter ou de se déconnecter
def openServer(host,
               port,
               buffer=1024):
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((host,port))
    serveur.listen(5)

    client, infosClient = serveur.accept()
    print("Client connecté. Adresse " + infosClient[0])  

    while True:    
        
        reponse = "Veuillez choisir 1 pour vous inscrire ,2 pour vous connecter, 3 pour quitter "
        client.send(reponse.encode("utf-8"))
        time.sleep(2)

        requete = client.recv(buffer)
        requete_decode = requete.decode("utf-8")

        if requete_decode == "1":
            Inscription(client,buffer)

        elif requete_decode == "2":
            Connexion(client,buffer)

        elif requete_decode == "3":         
            req = "Au revoir !!!"
            client.send(req.encode("utf-8")) 
            client.close()
            break

    serveur.close()
           
    


if __name__ == "__main__":
    
    openServer('192.168.10.1', 50000)
