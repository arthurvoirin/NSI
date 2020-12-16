NO_CAR = 256 #?

txtRecherche = ('CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTT')
motifRecherche = 'ACCTTCG'

def recherche(txt, motif):
    
    m       = len(motif)
    n       = len(txt)
    tab_car = [-1]*NO_CAR
    
    for i in range(m):
        tab_car[ord(motif[i])] = i
    
    decalage= 0
    res     = [] #res = position du premier caractère du motif dans txtRecherche
    
    while(decalage <= n-m):
        
        j = m - 1
        
        while j>=0 and motif[j] == txt[decalage+j]:
            j = j - 1
        
        if j<0:
            res.append(decalage)
            if decalage+m < n :
                decalage = decalage + m-tab_car[ord(txt[decalage+m])]
            else :
                decalage = decalage + 1
        else:
            decalage = decalage + max(1, j-tab_car[ord(txt[decalage+j])])
    
    #Convertie list(res) en integer        
    for i in res: 
        print("Le motif se trouve en position",i, end="\n") #Affiche la position de la première occurence
        print("Voici le motif", txtRecherche[i:i+m]) #Affiche le motif

recherche(txtRecherche, motifRecherche)
