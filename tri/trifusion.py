#Liste à trier
l = [23, 12, 4, 56, 35, 32, 42, 57, 3]

def fusion(gauche,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):        
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat
 
#
def tri_fusion(l):
    if len(l) <= 1:
        return l
    milieu = len(l) // 2
    gauche = l[:milieu]
    droite = l[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))

print(tri_fusion(l))
