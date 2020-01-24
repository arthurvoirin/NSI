#Générateur de QCM - NSI
#Arthur Voirin 1.3
#Dernière modification 23/01/2020 - Python 3.7

import random

#Liste des questions
questions=(
       ("0","En quelle année G. Boole publie t-il un article sur la logique binaire ?","1864", "1853", "1854", "1863", "C"),
       ("1","Comment est appelé un groupe de 4 bits ?","Quartet", "Octet", "Quartil", "Octal", "B"),
       ("2","Quelle est la représentation graphique de 254 ?","0b1111.1110", "0b0111.1111", "0b1111.1111", "0b1111.1100", "A"),
       ("3","Combien vallent 9B ?","9 bits","72 octets","72 bits","9 octets","D"))

compteurPoint=0 #Compteur de points
compteurQuestion=0 #Compteur de questions

nbQuestion=int(input("Combien de questions souhaitez vous ?")) #Demande à l'utilisateur combien il souhaite de questions dans son QCM
if nbQuestion > len(questions): #Dans le cas où l'utilisateur saisirait un nb de questions supérieur à celui présent dans la base
		print("Le nombre de questions désirées est supérieur à celui présent dans notre base...")
    print("Nous vous proposons donc le nombre maximal de questions :", len(questions))
    nbQuestion=len(questions)

lQuestions = [l for l in range(0,len(questions))] #Liste regroupant les identifiants des questions

def inputQ():
    i=random.choice(lQuestions) #Nombre aléatoire pour le choix de la question

    global compteurPoint
    global compteurQuestion
    
    print(questions[i][1]) #Affichage de la question
    print("A : ", questions[i][2]) #Choix A
    print("B : ", questions[i][3]) #Choix B
    print("C : ", questions[i][4]) #Choix C
    print("D : ", questions[i][5]) #Choix D
    r=input("Quelle est votre réponse ?")
    
    if r==questions[i][6]: #Si la réponse est correcte
        print("Bravo ! \n")
        compteurPoint+=1
    else: #Si la réponse est incorrete
        print("La réponse est incorrecte... \n")
    compteurQuestion+=1
    lQuestions.remove(i) #Supprime la question posée en utilisant sa valeur

while compteurQuestion!=nbQuestion:
    inputQ()

note=round(compteurPoint/nbQuestion*20,2) #Calcule de la note sur 20
print("Vous avez obtenu le score de", compteurPoint,"/",nbQuestion,".")
print("Cela représente une note de ", note,"/20.") #Arrondi à ajouter
