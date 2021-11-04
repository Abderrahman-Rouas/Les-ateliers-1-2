def tri_abulle(T):        #declaration de la fonction de tri a bulle
 n = len(T)
 permutation = True           #variable booléen
 while (permutation == True):   # on va bouclé tant que le variable booléen est true
  permutation = False
  for i in range(0, n - 1):
    if T[i] > T[i + 1]:        #condition de permutation
     tmp = T[i]                #permutation de premier variable par qui le suive
     T[i] = T[i + 1]
     T[i + 1] = tmp
     permutation = True
  n= n- 1                       #diminuer la dimension du tableau
 return T                       #returner le tableau trier
t=[22,5,6,4,12,32,65,1,0,11,55]
print(t)
print(tri_abulle(t))
