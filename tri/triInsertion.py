#Méthode du tri par insertion
#Author : Arthur Voirin
#Dernière modification : 22/12/2021

# ----------------------- #

#Liste à trier
l = [3,6,1,10,5,2]

#Fonction permettant le tri
def triInsertion(l):
    
    #Passage en revu des éléments de la liste, 1 par 1
    for i in range(1,len(l)): #
        en_cours = l[i]
        j = i
        
        #Décalage des éléments de la liste
        while j>0 and l[j-1]>en_cours:
            l[j]=l[j-1]
            j = j-1
        
        #Insertion de l'élément trié à sa place dans la liste
        l[j]=en_cours
    
    return(l) #Valeur de retour = liste triée

#Affiche le résultat du tri
print(triInsertion(l))
