def inverse(a):  # declaration de la fonction  avec un argument a
    inv = " "  # declaration d'un variable vide
    for i in a:  # boucle  qui parcourir  la chaine a
        inv = i + inv  # affecter a le variable inv i+inv pour l'emplacer inversement
    return inv  # return de la chaine inversé


y = "hello"
c = inverse(y)  # appel de la fonction
print(c)  # affichage de la fonction """