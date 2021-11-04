def counts(st, a):  # declaration de la fonction avec deux arguments
    j = 0  # declaration de variable compteur
    for i in st:  # la boucle qui va parcourir la chaine de caractere
        if a == i:  # condtions
            j = j + 1  # calcul combien de fois le caractere est répéter
    return j


st = input("entrer une chaine ")
a = input("entrer un caractere ")

print("le nombre de fois que le caractere ", a, "est", counts(st, a))  # afficher le frequence du caractére


