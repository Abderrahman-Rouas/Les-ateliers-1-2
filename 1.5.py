def nbr_chiffre(x):       #decalartion de la fonction avec un argument x
    if x<10 :             # condition de l'arret de la fonction recusrive
        return 1
    else :
        return (1+nbr_chiffre(x/10))       #il va return 1+lafonction avec l'argument x/10
x=int(input("entrer un nombre "))          #demende de saisir un nombre
z=nbr_chiffre(x)                           #affecter le resultat de la fonction a un variable z
print( " le nombre des chiffres est : " ,z) # afficher z """
