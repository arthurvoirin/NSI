#Méthode du tri par sélection
#Author : Arthur Voirin
#Dernière modification : 21/01/2021

# ----------------------- #

L = [3,2,7,1,9,5,6,8,4] #Liste à trier

#Définition de la fonction permettant le tri par sélection de L
def triSelection(L):
    
    longueurL = len(L) #Longueur de la liste
    
    for enCours in range(0,longueurL):    
        
        plusPetit = enCours #Passage en revue de tous les éléments de la liste 1 à 1
        
        for i in range(enCours+1,longueurL): 
            if L[i] < L[plusPetit]: #Comparaison de l'élément plusPetit (= avec l'index enCours) avec les suivants (i)
                plusPetit = i #Si un élément est plus petit que celui enCours, alors plusPetit = i
        
        if min is not enCours: #Si le plus petit nombre de  la liste est != enCours
            attendeDeplacement = L[enCours] #Mise dans attendeDeplacement du nombre enCours 
            L[enCours] = L[plusPetit]
            L[plusPetit] = attendeDeplacement #Déplacement du nombre enCours et inversion avec attenteDeplacement

    return(L)

print(triSelection(L)) #Affichage du résultat du tri après traitement
