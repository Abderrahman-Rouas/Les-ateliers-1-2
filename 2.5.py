liste1=[10,50,65,12,85,330,78]                   #declaration de list1
liste2=[]                                        #declaration d'une list2 vide
my_dict={'simo':65,'soulaiman':78,"abdo":12}     #declaration de dictionnaire
for i in my_dict.values():                     #"key":"values"
    for j in range(len(liste1)):
        if i==liste1[j]:                     #verifier si le clé se trouve dans liste 1
            liste2.append(liste1[j])         # ajouter ses elements dans list2
print(liste2)                              #afficher la list2