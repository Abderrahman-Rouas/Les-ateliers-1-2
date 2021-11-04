def tri_selection(tableau):      #declaration  de la fonction
 nb = len(tableau)               #variable contient la taille du tableau
 for i in range(0, nb):          #bouclé de 0 jusqu'a nb
  plus_petit = i                  #initialiser le premier element tel que le plus petit
  for j in range(i + 1, nb):      #deuxieme boucle qui va parcourir de la deuxieme element jusqu'a le dernier
   if tableau[j] < tableau[plus_petit]:    #condition pour trouverle élément le plus petit
    plus_petit = j                          #affecter le plus petit à j
  if min is not i:                           #condition pour permuter le tableau
   temp = tableau[i]                          #permutation du tableau
   tableau[i] = tableau[plus_petit]
   tableau[plus_petit] = temp
 return  tableau                               # return du tableau trier
import array as arr                             #declaration d'un tableau
a = arr.array('i', [2,1, 9,5,2,0,3,55,14, 6, 8])
print(tri_selection(a))