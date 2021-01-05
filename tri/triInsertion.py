#Méthode du tri par insertion
#Author : Arthur Voirin
#Dernière modification : 22/12/2021

# ----------------------- #

#Liste à trier
l = [3,6,1,10,5,2]

#Fonction permettant le tri
def tri_insertion(l):
    
    
    for i in range(1,len(l)):
        en_cours = l[i]
        j = i
        
        #décalage des éléments du l
        while j>0 and l[j-1]>en_cours:
            l[j]=l[j-1]
            j = j-1
        #on insère l'élément à sa place
        l[j]=en_cours
    return(l)

print(tri_insertion(l))
