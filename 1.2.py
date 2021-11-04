def changement(n):                #declaration de la fonction avec un argument
    b=0                           #variable qui va stocker la valeur binaire
    ord=0                         # variable puissance
    while n!=0:                   #condtions d'entrer au boucle
        reste=n%2                 #variable qui va stocker le reste de la division de n par 2
        p=10**ord
        b=b+reste*p
        ord=ord+1                  # incrimenter la puissance
        n=n//2                     # division de n par 2
    return b                        # le retour de nombre en binaire
n=int(input("entrer un nombre"))
z=changement(n)
print(z)