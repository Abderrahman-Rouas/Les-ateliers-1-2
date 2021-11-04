def fact(y):      #decalaration du fonction factorial
   f=1
   for i in range(1,y+1):     # boucle
        f=f*i
   return f
n=int(input("entrer le nombre n = "))  #demander a l'utilisateur de saisir un nombre
s=0                                  #variable de la somme
for i in range (1,n+1):
     s=s+fact(i)/i                   #l'appel du fontion dans la somme pour calculer le factoriel

print("le sommes est ",s)            #l'affichage de la somme """
