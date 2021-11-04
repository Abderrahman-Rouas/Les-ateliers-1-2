def find(list):                      #declaration de la fonction avec un aegument

    for i in list:                   #premiere boucle qui va parcourir la list
        a=0                          #variable inistialé par 0 qui va nous donnez l'index j
        for j in i :                 #deuxieme boucle qui va parcourir les element dans i
                if j==k :             #conditon
                   print("i=",list.index(i),"j=",a)   #affichage du numero de  l'index i et j de k
                a=a+1

list=[[1,2,2],                                   #list 2 dimensions
      [4,2,2],
      [2,8,9] ]
k=int(input("entrer la valeur chercher"))            #entrer de la valeur chercher
print(find(list))                            #l'appel de la fonction et l'affichage des nums indexs iet j
