mylist1=[11, 45, 8, 23, 14, 12, 78, 45, 89]   #declaration de la list
l1=[]                                         #declaration de  3 list vide
l2=[]
l3=[]
y=int(len(mylist1)//3)                         #diviser la list par 3
for i in range(y):                              #premier boucle de 0 jusqua y
    l1.append(mylist1[i])                        #ajouter les premiers elements à la list l1
for i in range(y,y*2):
    l2.append(mylist1[i])
for i in range (y*2,y*3):
    l3.append(mylist1[i])
print(mylist1)
l1.reverse()                                # inverser la liste l1
print(l1)                                   #afficher la listl1
l2.reverse()                                #inverser l2
print(l2)                                 #afficher l2
l3.reverse()
print(l3)