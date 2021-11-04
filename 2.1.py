mylist1=[3, 6, 9, 12, 15, 18, 21]      #declaration de deux liste
mylist2=[4, 8,12, 16, 20, 24, 28]
mylist=[]                                  #declaration d'une liste vide
for i in range(len(mylist2)):              #boucle pour parcourir list 2
      if (i%2==0):                         #conditon pour trouver les nombres pair
          mylist.append(mylist2[i])         #ajouter l'element au list vide

for j in range (len(mylist2)):
      if(j%2!=0):                         #conditon pour trouver les nombres impaire
          mylist.append(mylist1[j])

print("la nouvelle list est : " , mylist) #afficher la list
