liste1=[10,10,2,3,3,4,4,5,5,0,0,0]    #declaration de la liste
my_dict = {}                           # declaration d'un dictionnaire vide
for i in range(len(liste1)):            #bouclé la liste 1
    c=0
    for j in range(len(liste1)):       #deuxieme boucle
        if liste1[i]==liste1[j]:       #condtion pour vérifier  si l'élément se répète
            c=c+1
    my_dict[liste1[i]] =c               #remplir le dictionnaire
print(my_dict)                       #afficher le dictionnaire
