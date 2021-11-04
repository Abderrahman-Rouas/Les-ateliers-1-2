def somme(n):    #déclaration de la fonction
    if n==0:     #conditions de l'arrét
        return 0
    else :
        return (n+somme(n-1))    #return de la valeur n et la fonction d'une maniere récusrsive
y=int(input("entrer un nombre ")) # demender la saisir d'un nombre
z=somme(y)                        #l'appel de la fonction récursive
print(z)
