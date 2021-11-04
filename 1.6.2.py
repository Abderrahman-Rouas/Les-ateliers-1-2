def tri_insertion(tableau):
    for i in range(1,len(tableau)):
        k = tableau[i]
        j = i

        while j>0 and tableau[j-1]>k:           #on fait un décalage aux   éléments du tableaux
            tableau[j]=tableau[j-1]
            j = j-1

        tableau[j]=k                                #insertion des élément
    return tableau                                     # return du tableau trier

import array as arr
a = arr.array('i', [2,44,3,6,1,2,0,9,99,100,7])
print(tri_insertion(a))