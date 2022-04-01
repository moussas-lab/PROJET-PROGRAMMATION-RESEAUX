
import json
import socket
import datetime

#Fonction qui interagit avec le serveur pour inscrire les identifiants d'un clients dans la base de donnée
def Inscription(client:socket, buffer:int):
    reponse = client.recv(buffer)
    print(reponse.decode("utf-8"))
    choix_str = input("")
    client.send(choix_str.encode("utf-8"))#1

    reponse = client.recv(buffer)
    print(reponse.decode("utf-8"))
    choix_str = input("")
    client.send(choix_str.encode("utf-8"))#2

    reponse = client.recv(buffer)
    print(reponse.decode("utf-8"))
    choix_str = input("")
    client.send(choix_str.encode("utf-8"))#3

    verification = "Les mots de passe ne sont pas identiques !!"

    while verification == "Les mots de passe ne sont pas identiques !!":
        reponse = client.recv(buffer)
        print(reponse.decode("utf-8"))
        choix_str = input("")
        client.send(choix_str.encode("utf-8"))#4

        reponse = client.recv(buffer)
        print(reponse.decode("utf-8"))
        choix_str = input("")
        client.send(choix_str.encode("utf-8"))#5

        reponse = client.recv(buffer)
        verification = reponse.decode("utf-8")
        if verification == "Les mots de passe ne sont pas identiques !!":
            print(verification)



#Fonction qui interagit avec le serveur pour se connecter 
def Connexion(client:socket,buffer:int):
    reponse = client.recv(buffer)
    print(reponse.decode("utf-8"))
    choix_str = input("")
    client.send(choix_str.encode("utf-8"))#1

    reponse = client.recv(buffer)
    print(reponse.decode("utf-8"))
    choix_str = input("")
    client.send(choix_str.encode("utf-8"))#2

#Fonction qui permet d'initialiser une connexion avec un serveur et d'interagir avec celui ci afin d'avoir la possibilité de s'inscrire,
#de se connecter ou de terminer la connexion
def openClientTunnel(host,
                     port,
                     buffer=4096):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host, port))
    print("Connexion au serveur de MPSI/ISI")
    print(f'Connexion faite à: {datetime.datetime.now()}')
    print(f'Connexion faite via le port: {port} à l\'adresse: {host}')
    req = 0
    
    while True:
        reponse = client.recv(buffer)
        print(reponse.decode("utf-8"))
        req = input("")
        client.send(req.encode("utf-8"))

        if req == "1":
            Inscription(client,buffer)
        
        elif req == "2":
            Connexion(client,buffer)

        elif req == "3":
            reponse = client.recv(buffer)
            print(reponse.decode("utf-8"))
            break
    client.close()
    print("Connexion fermée")


if __name__ == '__main__':
    openClientTunnel("192.168.10.1", 50000)
